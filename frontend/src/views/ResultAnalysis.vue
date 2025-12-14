<template>
  <div class="result-analysis">
    <nav class="navbar">
      <div class="nav-brand">
        <router-link to="/runtime">← 返回运行控制台</router-link>
      </div>
      <h1>📊 结果分析与可视化</h1>
    </nav>

    <div class="content">
      <div class="page-header">
        <h2>AI运行结果分析</h2>
        <p>观察者模式：AI结果变化时，图表自动更新</p>
      </div>

      <div v-if="result" class="results-container">
        <div class="result-card">
          <h3>📈 性能指标</h3>
          <div class="metrics-grid">
            <div class="metric-box" v-for="(value, key) in result.metrics" :key="key">
              <span class="metric-name">{{ getMetricName(key) }}</span>
              <span class="metric-value">{{ formatMetric(key, value) }}</span>
            </div>
          </div>
        </div>

        <div class="result-card">
          <h3>📊 预测结果可视化</h3>
          <div class="chart-container">
            <canvas ref="chartCanvas"></canvas>
          </div>
        </div>

        <div class="result-card">
          <h3>🔍 详细数据</h3>
          <div class="data-display">
            <div class="data-item">
              <span class="data-label">任务类型：</span>
              <span class="data-value">{{ result.type }}</span>
            </div>
            <div class="data-item">
              <span class="data-label">模型：</span>
              <span class="data-value">{{ result.predictions.model }}</span>
            </div>
            <div class="data-item">
              <span class="data-label">置信度：</span>
              <span class="data-value">{{ (result.predictions.confidence * 100).toFixed(1) }}%</span>
            </div>
          </div>
        </div>

        <div class="result-card compare-section">
          <h3>🔄 策略对比</h3>
          <p>选择多个策略进行性能对比</p>
          <div class="strategy-selector">
            <label v-for="strategy in strategies" :key="strategy.id" class="checkbox-label">
              <input
                type="checkbox"
                :value="strategy.id"
                v-model="selectedStrategies"
              />
              {{ strategy.name }}
            </label>
          </div>
          <button @click="compareStrategies" :disabled="selectedStrategies.length < 2" class="compare-btn">
            开始对比
          </button>

          <div v-if="comparisonData.length > 0" class="comparison-results">
            <h4>对比结果</h4>
            <div class="comparison-chart">
              <canvas ref="comparisonCanvas"></canvas>
            </div>
          </div>
        </div>
      </div>

      <div v-else class="no-results">
        <div class="empty-icon">📊</div>
        <h3>暂无结果数据</h3>
        <p>请先在运行控制台执行AI模型</p>
        <button @click="goToRuntime" class="go-runtime-btn">前往运行控制台</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue'
import { useRouter } from 'vue-router'
import { useSystemStore } from '../stores/system'
import { Chart, registerables } from 'chart.js'

Chart.register(...registerables)

const router = useRouter()
const store = useSystemStore()

const result = ref(null)
const strategies = ref([])
const selectedStrategies = ref([])
const comparisonData = ref([])
const chartCanvas = ref(null)
const comparisonCanvas = ref(null)
let chartInstance = null
let comparisonChartInstance = null

onMounted(async () => {
  await store.fetchResults()
  result.value = store.latestResult

  await store.fetchStrategies()
  strategies.value = store.strategies

  if (result.value && result.value.chart_data) {
    await nextTick()
    renderChart()
  }
})

const getMetricName = (key) => {
  const names = {
    accuracy: '准确度',
    precision: '精确度',
    recall: '召回率',
    f1_score: 'F1分数',
    training_time: '训练时间'
  }
  return names[key] || key
}

const formatMetric = (key, value) => {
  if (key === 'training_time') {
    return `${value}s`
  }
  return (value * 100).toFixed(1) + '%'
}

const renderChart = () => {
  if (!chartCanvas.value) return

  if (chartInstance) {
    chartInstance.destroy()
  }

  const ctx = chartCanvas.value.getContext('2d')
  chartInstance = new Chart(ctx, {
    type: 'line',
    data: {
      labels: result.value.chart_data.labels,
      datasets: [{
        label: '预测值',
        data: result.value.chart_data.values,
        borderColor: '#667eea',
        backgroundColor: 'rgba(102, 126, 234, 0.1)',
        tension: 0.4,
        fill: true
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: true,
          position: 'top'
        }
      },
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  })
}

const compareStrategies = async () => {
  if (selectedStrategies.value.length < 2) return

  comparisonData.value = await store.compareResults(selectedStrategies.value)

  await nextTick()
  renderComparisonChart()
}

const renderComparisonChart = () => {
  if (!comparisonCanvas.value) return

  if (comparisonChartInstance) {
    comparisonChartInstance.destroy()
  }

  const ctx = comparisonCanvas.value.getContext('2d')

  const datasets = comparisonData.value.map((item, index) => {
    const colors = ['#667eea', '#764ba2', '#10b981', '#f59e0b']
    return {
      label: item.strategy,
      data: Object.values(item.result.metrics).slice(0, 4),
      backgroundColor: colors[index % colors.length]
    }
  })

  comparisonChartInstance = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['准确度', '精确度', '召回率', 'F1分数'],
      datasets: datasets
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: true,
          position: 'top'
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          max: 1
        }
      }
    }
  })
}

const goToRuntime = () => {
  router.push('/runtime')
}
</script>

<style scoped>
.result-analysis {
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.navbar {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  padding: 1.5rem 3rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
}

.nav-brand a {
  color: white;
  text-decoration: none;
  font-weight: 600;
}

.navbar h1 {
  color: white;
  font-size: 1.5rem;
}

.content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 3rem 2rem;
}

.page-header {
  text-align: center;
  color: white;
  margin-bottom: 3rem;
}

.page-header h2 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.page-header p {
  opacity: 0.9;
  font-size: 1.1rem;
}

.results-container {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.result-card {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.result-card h3 {
  color: #333;
  margin-bottom: 1.5rem;
  font-size: 1.3rem;
}

.metrics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

.metric-box {
  display: flex;
  flex-direction: column;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 8px;
  border-left: 4px solid #667eea;
}

.metric-name {
  font-size: 0.875rem;
  color: #666;
  margin-bottom: 0.5rem;
}

.metric-value {
  font-size: 1.5rem;
  font-weight: 700;
  color: #667eea;
}

.chart-container {
  height: 300px;
  position: relative;
}

.data-display {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.data-item {
  display: flex;
  justify-content: space-between;
  padding: 0.75rem;
  background: #f8f9fa;
  border-radius: 8px;
}

.data-label {
  font-weight: 600;
  color: #333;
}

.data-value {
  color: #667eea;
  font-weight: 500;
}

.compare-section p {
  color: #666;
  margin-bottom: 1rem;
}

.strategy-selector {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: #f8f9fa;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.3s;
}

.checkbox-label:hover {
  background: #e9ecef;
}

.checkbox-label input {
  cursor: pointer;
}

.compare-btn {
  padding: 0.75rem 2rem;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s;
}

.compare-btn:hover:not(:disabled) {
  background: #5568d3;
  transform: scale(1.05);
}

.compare-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.comparison-results {
  margin-top: 2rem;
  padding-top: 2rem;
  border-top: 2px solid #e9ecef;
}

.comparison-results h4 {
  color: #333;
  margin-bottom: 1rem;
}

.comparison-chart {
  height: 350px;
  position: relative;
}

.no-results {
  background: white;
  border-radius: 16px;
  padding: 4rem 2rem;
  text-align: center;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.empty-icon {
  font-size: 5rem;
  margin-bottom: 1rem;
}

.no-results h3 {
  color: #333;
  margin-bottom: 0.5rem;
}

.no-results p {
  color: #666;
  margin-bottom: 2rem;
}

.go-runtime-btn {
  padding: 0.75rem 2rem;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s;
}

.go-runtime-btn:hover {
  background: #5568d3;
  transform: scale(1.05);
}
</style>

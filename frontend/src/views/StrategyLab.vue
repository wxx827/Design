<template>
  <div class="strategy-page">
    <div class="page-header">
      <div>
        <h1 class="page-title">策略配置</h1>
        <p class="page-desc">策略模式：动态选择不同的AI算法实现，运行时灵活切换</p>
      </div>
    </div>

    <div class="strategies-grid">
      <div
        v-for="strategy in strategies"
        :key="strategy.id"
        class="strategy-card"
        :class="{ 'active': selectedStrategy === strategy.id }"
        @click="selectStrategy(strategy.id)"
      >
        <div class="strategy-header">
          <h3>{{ strategy.name }}</h3>
          <div v-if="selectedStrategy === strategy.id" class="active-badge">
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
              <path d="M4 8L7 11L12 5" stroke="white" stroke-width="2"/>
            </svg>
          </div>
        </div>

        <p class="strategy-desc">{{ strategy.description }}</p>

        <div class="metrics-grid">
          <div class="metric-item">
            <span class="metric-label">准确度</span>
            <div class="progress-bar">
              <div class="progress-fill" :style="{ width: (strategy.accuracy * 100) + '%' }"></div>
            </div>
            <span class="metric-value">{{ (strategy.accuracy * 100).toFixed(0) }}%</span>
          </div>

          <div class="metric-item">
            <span class="metric-label">运行速度</span>
            <span class="metric-badge" :class="'speed-' + strategy.speed">
              {{ getSpeedText(strategy.speed) }}
            </span>
          </div>

          <div class="metric-item">
            <span class="metric-label">内存占用</span>
            <span class="metric-badge" :class="'memory-' + strategy.memory">
              {{ getMemoryText(strategy.memory) }}
            </span>
          </div>

          <div class="metric-item">
            <span class="metric-label">复杂度</span>
            <span class="metric-badge" :class="'complexity-' + strategy.complexity">
              {{ getComplexityText(strategy.complexity) }}
            </span>
          </div>
        </div>
      </div>
    </div>

    <div class="comparison-card">
      <h3>策略对比分析</h3>
      <div class="comparison-chart">
        <div v-for="strategy in strategies" :key="strategy.id" class="chart-item">
          <div class="bar-container">
            <div
              class="bar"
              :style="{
                height: (strategy.accuracy * 250) + 'px',
                background: selectedStrategy === strategy.id ? '#1890ff' : '#e0e0e0'
              }"
            ></div>
          </div>
          <span class="bar-label">{{ strategy.name.replace('模型', '') }}</span>
          <span class="bar-value">{{ (strategy.accuracy * 100).toFixed(0) }}%</span>
        </div>
      </div>
    </div>

    <div class="action-bar" v-if="selectedStrategy">
      <button @click="proceedToRuntime" class="btn-primary">
        开始运行AI模型 →
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useSystemStore } from '../stores/system'

const router = useRouter()
const store = useSystemStore()

const strategies = ref([])
const selectedStrategy = ref(null)

onMounted(async () => {
  await store.fetchStrategies()
  strategies.value = store.strategies
  selectedStrategy.value = store.currentStrategy
})

const selectStrategy = (strategyId) => {
  selectedStrategy.value = strategyId
  store.setStrategy(strategyId)
}

const getSpeedText = (speed) => {
  const map = { fast: '快速', medium: '中等', slow: '较慢' }
  return map[speed] || speed
}

const getMemoryText = (memory) => {
  const map = { low: '低', medium: '中', high: '高' }
  return map[memory] || memory
}

const getComplexityText = (complexity) => {
  const map = { low: '简单', medium: '中等', high: '复杂' }
  return map[complexity] || complexity
}

const proceedToRuntime = () => {
  router.push('/runtime')
}
</script>

<style scoped>
.strategy-page {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.page-title {
  font-size: 28px;
  font-weight: 600;
  color: #1a1a1a;
  margin-bottom: 8px;
}

.page-desc {
  font-size: 14px;
  color: #999;
}

.strategies-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.strategy-card {
  background: white;
  border-radius: 12px;
  padding: 24px;
  cursor: pointer;
  transition: all 0.3s;
  border: 2px solid #e8e8e8;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.strategy-card:hover {
  border-color: #1890ff;
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.12);
  transform: translateY(-4px);
}

.strategy-card.active {
  border-color: #1890ff;
  background: linear-gradient(to bottom, #ffffff, #f0f5ff);
  box-shadow: 0 4px 12px rgba(24, 144, 255, 0.25);
}

.strategy-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.strategy-header h3 {
  font-size: 18px;
  font-weight: 600;
  color: #1a1a1a;
}

.active-badge {
  width: 24px;
  height: 24px;
  background: #1890ff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.strategy-desc {
  font-size: 14px;
  color: #666;
  line-height: 1.6;
  margin-bottom: 20px;
}

.metrics-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

.metric-item {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.metric-label {
  font-size: 12px;
  color: #999;
  font-weight: 500;
}

.progress-bar {
  width: 100%;
  height: 6px;
  background: #f0f0f0;
  border-radius: 3px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: #1890ff;
  border-radius: 3px;
  transition: width 0.5s ease;
}

.metric-value {
  font-size: 16px;
  font-weight: 600;
  color: #1890ff;
}

.metric-badge {
  padding: 4px 12px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
  width: fit-content;
}

.speed-fast, .memory-low, .complexity-low {
  background: #f6ffed;
  color: #52c41a;
}

.speed-medium, .memory-medium, .complexity-medium {
  background: #fff7e6;
  color: #fa8c16;
}

.speed-slow, .memory-high, .complexity-high {
  background: #fff1f0;
  color: #f5222d;
}

.comparison-card {
  background: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.comparison-card h3 {
  font-size: 18px;
  font-weight: 600;
  color: #1a1a1a;
  margin-bottom: 24px;
}

.comparison-chart {
  display: flex;
  justify-content: space-around;
  align-items: flex-end;
  height: 300px;
  padding: 20px 0;
}

.chart-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  flex: 1;
}

.bar-container {
  height: 250px;
  display: flex;
  align-items: flex-end;
}

.bar {
  width: 60px;
  border-radius: 6px 6px 0 0;
  transition: all 0.5s ease;
}

.bar-label {
  font-size: 13px;
  color: #666;
  text-align: center;
  font-weight: 500;
}

.bar-value {
  font-size: 14px;
  color: #1890ff;
  font-weight: 600;
}

.action-bar {
  display: flex;
  justify-content: center;
}

.btn-primary {
  padding: 12px 32px;
  font-size: 15px;
  background: #1890ff;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.3s;
}

.btn-primary:hover {
  background: #40a9ff;
  box-shadow: 0 4px 12px rgba(24, 144, 255, 0.3);
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .strategies-grid {
    grid-template-columns: 1fr;
  }

  .metrics-grid {
    grid-template-columns: 1fr;
  }
}
</style>

<template>
  <div class="ai-runtime">
    <nav class="navbar">
      <div class="nav-brand">
        <router-link to="/strategy">← 返回策略选择</router-link>
      </div>
      <h1>⚙ AI运行与监控</h1>
    </nav>

    <div class="content">
      <div class="page-header">
        <h2>模型运行控制台</h2>
        <p>模板方法模式：加载数据 → 预处理 → 推理 → 输出结果</p>
      </div>

      <div class="runtime-panel">
        <div class="current-config">
          <h3>当前配置</h3>
          <div class="config-item">
            <span class="label">任务类型：</span>
            <span class="value">{{ currentTask || '未选择' }}</span>
          </div>
          <div class="config-item">
            <span class="label">AI策略：</span>
            <span class="value">{{ currentStrategy || '未选择' }}</span>
          </div>
        </div>

        <div class="control-section">
          <button
            @click="runModel"
            :disabled="isRunning || !currentTask || !currentStrategy"
            class="run-btn"
          >
            {{ isRunning ? '运行中...' : '🚀 开始运行' }}
          </button>
        </div>

        <div v-if="progress.length > 0" class="progress-section">
          <h3>执行进度</h3>
          <div class="progress-steps">
            <div
              v-for="(step, index) in progress"
              :key="index"
              class="step-item"
              :class="{ 'completed': step.status === 'completed' }"
            >
              <div class="step-icon">{{ step.status === 'completed' ? '✓' : '○' }}</div>
              <span class="step-text">{{ step.step }}</span>
            </div>
          </div>
        </div>

        <div v-if="isRunning" class="loading-animation">
          <div class="spinner"></div>
          <p>AI模型正在运行中...</p>
        </div>

        <div v-if="completed" class="completion-message">
          <div class="success-icon">✓</div>
          <h3>运行完成！</h3>
          <p>模型已成功完成推理，请查看结果分析</p>
          <button @click="goToResults" class="results-btn">
            查看结果分析 →
          </button>
        </div>

        <div v-if="systemState" class="state-display">
          <h3>系统状态监控</h3>
          <div class="state-grid">
            <div class="state-item">
              <span class="state-label">初始化状态</span>
              <span class="state-value">{{ systemState.initialized ? '已初始化' : '未初始化' }}</span>
            </div>
            <div class="state-item">
              <span class="state-label">运行状态</span>
              <span class="state-value">{{ systemState.running ? '运行中' : '就绪' }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useSystemStore } from '../stores/system'

const router = useRouter()
const store = useSystemStore()

const currentTask = ref(null)
const currentStrategy = ref(null)
const isRunning = ref(false)
const completed = ref(false)
const progress = ref([])
const systemState = ref(null)

onMounted(async () => {
  await store.fetchConfig()
  currentTask.value = store.currentTask
  currentStrategy.value = store.currentStrategy
})

const runModel = async () => {
  if (!currentTask.value || !currentStrategy.value) return

  isRunning.value = true
  completed.value = false
  progress.value = []

  const steps = [
    { step: '数据加载', status: 'pending' },
    { step: '数据预处理', status: 'pending' },
    { step: 'AI推理', status: 'pending' },
    { step: '结果生成', status: 'pending' }
  ]

  for (let i = 0; i < steps.length; i++) {
    await new Promise(resolve => setTimeout(resolve, 800))
    steps[i].status = 'completed'
    progress.value = [...steps]
  }

  try {
    await store.runModel(currentTask.value, currentStrategy.value)
    isRunning.value = false
    completed.value = true
  } catch (error) {
    console.error('Model execution failed:', error)
    isRunning.value = false
  }
}

const goToResults = () => {
  router.push('/results')
}
</script>

<style scoped>
.ai-runtime {
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
  max-width: 900px;
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

.runtime-panel {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.current-config {
  margin-bottom: 2rem;
  padding: 1.5rem;
  background: #f8f9fa;
  border-radius: 12px;
}

.current-config h3 {
  color: #333;
  margin-bottom: 1rem;
}

.config-item {
  margin: 0.5rem 0;
  color: #666;
}

.label {
  font-weight: 600;
  color: #333;
}

.value {
  color: #667eea;
  font-weight: 500;
}

.control-section {
  text-align: center;
  margin: 2rem 0;
}

.run-btn {
  padding: 1rem 3rem;
  font-size: 1.2rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s;
}

.run-btn:hover:not(:disabled) {
  transform: scale(1.05);
  box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
}

.run-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.progress-section {
  margin: 2rem 0;
}

.progress-section h3 {
  color: #333;
  margin-bottom: 1.5rem;
  text-align: center;
}

.progress-steps {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.step-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 8px;
  transition: all 0.3s;
}

.step-item.completed {
  background: #e8f5e9;
  border-left: 4px solid #10b981;
}

.step-icon {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: #e0e0e0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  color: #666;
}

.step-item.completed .step-icon {
  background: #10b981;
  color: white;
}

.step-text {
  font-weight: 500;
  color: #333;
}

.loading-animation {
  text-align: center;
  margin: 2rem 0;
}

.spinner {
  width: 60px;
  height: 60px;
  border: 6px solid #e0e0e0;
  border-top-color: #667eea;
  border-radius: 50%;
  margin: 0 auto 1rem;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.loading-animation p {
  color: #666;
  font-size: 1.1rem;
}

.completion-message {
  text-align: center;
  padding: 2rem;
  background: #e8f5e9;
  border-radius: 12px;
  margin: 2rem 0;
}

.success-icon {
  width: 80px;
  height: 80px;
  background: #10b981;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
  margin: 0 auto 1rem;
}

.completion-message h3 {
  color: #10b981;
  margin-bottom: 0.5rem;
}

.completion-message p {
  color: #666;
  margin-bottom: 1.5rem;
}

.results-btn {
  padding: 0.75rem 2rem;
  background: #10b981;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s;
}

.results-btn:hover {
  transform: scale(1.05);
  box-shadow: 0 5px 15px rgba(16, 185, 129, 0.3);
}

.state-display {
  margin-top: 2rem;
  padding: 1.5rem;
  background: #f8f9fa;
  border-radius: 12px;
}

.state-display h3 {
  color: #333;
  margin-bottom: 1rem;
}

.state-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

.state-item {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.state-label {
  font-size: 0.875rem;
  color: #666;
}

.state-value {
  font-weight: 600;
  color: #667eea;
}
</style>

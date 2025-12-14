<template>
  <div class="dashboard-page">
    <div class="page-header">
      <div>
        <h1 class="page-title">系统概览</h1>
        <p class="page-desc">基于多设计模式融合的智能决策平台</p>
      </div>
      <div class="header-actions">
        <button @click="refreshData" class="btn-refresh">
          <span class="icon">🔄</span>
          刷新数据
        </button>
      </div>
    </div>

    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-icon blue">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
            <path d="M12 2L2 7L12 12L22 7L12 2Z" stroke="currentColor" stroke-width="2"/>
            <path d="M2 17L12 22L22 17" stroke="currentColor" stroke-width="2"/>
            <path d="M2 12L12 17L22 12" stroke="currentColor" stroke-width="2"/>
          </svg>
        </div>
        <div class="stat-content">
          <div class="stat-value">{{ stats.total_tasks || 4 }}</div>
          <div class="stat-label">任务总数</div>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon green">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
            <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/>
            <path d="M8 12L11 15L16 9" stroke="currentColor" stroke-width="2"/>
          </svg>
        </div>
        <div class="stat-content">
          <div class="stat-value">{{ stats.completed_tasks || 0 }}</div>
          <div class="stat-label">已完成任务</div>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon orange">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
            <rect x="3" y="3" width="18" height="18" rx="2" stroke="currentColor" stroke-width="2"/>
            <path d="M3 9H21" stroke="currentColor" stroke-width="2"/>
            <path d="M9 3V21" stroke="currentColor" stroke-width="2"/>
          </svg>
        </div>
        <div class="stat-content">
          <div class="stat-value">{{ stats.strategies || 4 }}</div>
          <div class="stat-label">可用策略</div>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon purple">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
            <path d="M13 2L3 14H12L11 22L21 10H12L13 2Z" stroke="currentColor" stroke-width="2"/>
          </svg>
        </div>
        <div class="stat-content">
          <div class="stat-value">{{ stats.avg_accuracy || 87.5 }}%</div>
          <div class="stat-label">平均准确率</div>
        </div>
      </div>
    </div>

    <div class="content-grid">
      <div class="card large-card">
        <div class="card-header">
          <h3>当前系统配置</h3>
          <span class="status-badge success">运行中</span>
        </div>
        <div class="card-body">
          <div class="config-grid">
            <div class="config-item">
              <span class="config-label">当前任务</span>
              <span class="config-value">{{ currentTask || '未选择' }}</span>
            </div>
            <div class="config-item">
              <span class="config-label">当前策略</span>
              <span class="config-value">{{ currentStrategy || '未选择' }}</span>
            </div>
            <div class="config-item">
              <span class="config-label">执行次数</span>
              <span class="config-value">{{ stats.total_executions || 0 }}次</span>
            </div>
            <div class="config-item">
              <span class="config-label">运行状态</span>
              <span class="config-value status-normal">正常</span>
            </div>
          </div>
        </div>
      </div>

      <div class="card">
        <div class="card-header">
          <h3>设计模式应用</h3>
        </div>
        <div class="card-body">
          <div class="pattern-list">
            <div class="pattern-item">
              <div class="pattern-icon">🎯</div>
              <div class="pattern-info">
                <div class="pattern-name">策略模式</div>
                <div class="pattern-desc">AI算法动态切换</div>
              </div>
            </div>
            <div class="pattern-item">
              <div class="pattern-icon">🏭</div>
              <div class="pattern-info">
                <div class="pattern-name">工厂模式</div>
                <div class="pattern-desc">模型统一创建</div>
              </div>
            </div>
            <div class="pattern-item">
              <div class="pattern-icon">📋</div>
              <div class="pattern-info">
                <div class="pattern-name">模板方法</div>
                <div class="pattern-desc">流程标准化</div>
              </div>
            </div>
            <div class="pattern-item">
              <div class="pattern-icon">👁️</div>
              <div class="pattern-info">
                <div class="pattern-name">观察者模式</div>
                <div class="pattern-desc">状态实时同步</div>
              </div>
            </div>
            <div class="pattern-item">
              <div class="pattern-icon">🔒</div>
              <div class="pattern-info">
                <div class="pattern-name">单例模式</div>
                <div class="pattern-desc">全局配置管理</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="action-cards">
      <div class="action-card" @click="goToTasks">
        <div class="action-icon">📊</div>
        <h3>任务中心</h3>
        <p>选择并管理AI任务类型</p>
        <span class="action-arrow">→</span>
      </div>
      <div class="action-card" @click="goToStrategy">
        <div class="action-icon">⚙️</div>
        <h3>策略配置</h3>
        <p>选择和对比AI策略</p>
        <span class="action-arrow">→</span>
      </div>
      <div class="action-card" @click="goToDesign">
        <div class="action-icon">🏗️</div>
        <h3>系统架构</h3>
        <p>查看设计模式详解</p>
        <span class="action-arrow">→</span>
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
const stats = ref({
  total_tasks: 4,
  completed_tasks: 0,
  strategies: 4,
  avg_accuracy: 87.5,
  total_executions: 0
})

onMounted(async () => {
  await refreshData()
})

const refreshData = async () => {
  await store.fetchConfig()
  await store.fetchStats()
  currentTask.value = store.currentTask
  currentStrategy.value = store.currentStrategy
  stats.value = store.stats
}

const goToTasks = () => router.push('/tasks')
const goToStrategy = () => router.push('/strategy')
const goToDesign = () => router.push('/design')
</script>

<style scoped>
.dashboard-page {
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

.header-actions {
  display: flex;
  gap: 12px;
}

.btn-refresh {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background: white;
  border: 1px solid #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  color: #666;
  transition: all 0.2s;
}

.btn-refresh:hover {
  color: #1890ff;
  border-color: #1890ff;
}

.icon {
  font-size: 16px;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 16px;
}

.stat-card {
  background: white;
  padding: 24px;
  border-radius: 8px;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
  display: flex;
  align-items: center;
  gap: 16px;
  transition: all 0.2s;
}

.stat-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transform: translateY(-2px);
}

.stat-icon {
  width: 48px;
  height: 48px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.stat-icon.blue { background: #1890ff; }
.stat-icon.green { background: #52c41a; }
.stat-icon.orange { background: #fa8c16; }
.stat-icon.purple { background: #722ed1; }

.stat-content {
  flex: 1;
}

.stat-value {
  font-size: 28px;
  font-weight: 600;
  color: #1a1a1a;
  line-height: 1;
  margin-bottom: 8px;
}

.stat-label {
  font-size: 14px;
  color: #999;
}

.content-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 16px;
}

.card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
  overflow: hidden;
}

.card-header {
  padding: 20px 24px;
  border-bottom: 1px solid #f0f0f0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.card-header h3 {
  font-size: 16px;
  font-weight: 600;
  color: #1a1a1a;
}

.status-badge {
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 500;
}

.status-badge.success {
  background: #f6ffed;
  color: #52c41a;
}

.card-body {
  padding: 24px;
}

.config-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

.config-item {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.config-label {
  font-size: 13px;
  color: #999;
}

.config-value {
  font-size: 15px;
  color: #1a1a1a;
  font-weight: 500;
}

.status-normal {
  color: #52c41a !important;
}

.pattern-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.pattern-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  background: #fafafa;
  border-radius: 6px;
  transition: all 0.2s;
}

.pattern-item:hover {
  background: #f0f5ff;
}

.pattern-icon {
  font-size: 24px;
}

.pattern-info {
  flex: 1;
}

.pattern-name {
  font-size: 14px;
  font-weight: 500;
  color: #1a1a1a;
  margin-bottom: 4px;
}

.pattern-desc {
  font-size: 12px;
  color: #999;
}

.action-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 16px;
}

.action-card {
  background: white;
  padding: 24px;
  border-radius: 8px;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
  cursor: pointer;
  transition: all 0.2s;
  position: relative;
  border: 2px solid transparent;
}

.action-card:hover {
  border-color: #1890ff;
  box-shadow: 0 4px 12px rgba(24, 144, 255, 0.15);
  transform: translateY(-2px);
}

.action-icon {
  font-size: 40px;
  margin-bottom: 16px;
}

.action-card h3 {
  font-size: 16px;
  font-weight: 600;
  color: #1a1a1a;
  margin-bottom: 8px;
}

.action-card p {
  font-size: 14px;
  color: #999;
  margin-bottom: 16px;
}

.action-arrow {
  position: absolute;
  bottom: 24px;
  right: 24px;
  font-size: 20px;
  color: #1890ff;
}

@media (max-width: 1024px) {
  .content-grid {
    grid-template-columns: 1fr;
  }
}
</style>

<template>
  <div class="task-center-page">
    <div class="page-header">
      <div>
        <h1 class="page-title">任务中心</h1>
        <p class="page-desc">工厂模式：根据任务类型创建对应的AI模型实例</p>
      </div>
    </div>

    <div class="tasks-grid">
      <div
        v-for="task in tasks"
        :key="task.id"
        class="task-card"
        :class="{ 'selected': selectedTask === task.id }"
        @click="selectTask(task.id)"
      >
        <div class="task-header">
          <div class="task-icon">{{ task.icon }}</div>
          <div class="task-badges">
            <span class="badge category">{{ task.category }}</span>
            <span class="badge difficulty" :class="'difficulty-' + task.difficulty">
              {{ getDifficultyText(task.difficulty) }}
            </span>
          </div>
        </div>

        <h3 class="task-name">{{ task.name }}</h3>
        <p class="task-desc">{{ task.description }}</p>

        <div v-if="selectedTask === task.id" class="selected-indicator">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
            <circle cx="10" cy="10" r="9" stroke="#1890ff" stroke-width="2"/>
            <path d="M6 10L9 13L14 7" stroke="#1890ff" stroke-width="2"/>
          </svg>
          <span>已选择</span>
        </div>
      </div>
    </div>

    <div class="action-bar" v-if="selectedTask">
      <button @click="proceedToStrategy" class="btn-primary">
        继续选择策略 →
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

const tasks = ref([])
const selectedTask = ref(null)

onMounted(async () => {
  await store.fetchTasks()
  tasks.value = store.tasks
  selectedTask.value = store.currentTask
})

const selectTask = (taskId) => {
  selectedTask.value = taskId
  store.setTask(taskId)
}

const getDifficultyText = (difficulty) => {
  const map = {
    easy: '简单',
    medium: '中等',
    hard: '困难'
  }
  return map[difficulty] || difficulty
}

const proceedToStrategy = () => {
  router.push('/strategy')
}
</script>

<style scoped>
.task-center-page {
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

.tasks-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 20px;
}

.task-card {
  background: white;
  border-radius: 12px;
  padding: 24px;
  cursor: pointer;
  transition: all 0.3s;
  border: 2px solid transparent;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  position: relative;
}

.task-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.12);
}

.task-card.selected {
  border-color: #1890ff;
  box-shadow: 0 4px 12px rgba(24, 144, 255, 0.25);
}

.task-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 16px;
}

.task-icon {
  font-size: 48px;
}

.task-badges {
  display: flex;
  flex-direction: column;
  gap: 6px;
  align-items: flex-end;
}

.badge {
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
}

.badge.category {
  background: #e6f4ff;
  color: #1890ff;
}

.badge.difficulty {
  color: white;
}

.difficulty-easy {
  background: #52c41a;
}

.difficulty-medium {
  background: #fa8c16;
}

.difficulty-hard {
  background: #f5222d;
}

.task-name {
  font-size: 20px;
  font-weight: 600;
  color: #1a1a1a;
  margin-bottom: 12px;
}

.task-desc {
  font-size: 14px;
  color: #666;
  line-height: 1.6;
  margin-bottom: 16px;
}

.selected-indicator {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #1890ff;
  font-size: 14px;
  font-weight: 500;
}

.action-bar {
  display: flex;
  justify-content: center;
  margin-top: 16px;
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
  .tasks-grid {
    grid-template-columns: 1fr;
  }
}
</style>

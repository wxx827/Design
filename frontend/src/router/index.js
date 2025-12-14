import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import TaskCenter from '../views/TaskCenter.vue'
import StrategyLab from '../views/StrategyLab.vue'
import AIRuntime from '../views/AIRuntime.vue'
import ResultAnalysis from '../views/ResultAnalysis.vue'
import SystemDesign from '../views/SystemDesign.vue'

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/tasks',
    name: 'TaskCenter',
    component: TaskCenter
  },
  {
    path: '/strategy',
    name: 'StrategyLab',
    component: StrategyLab
  },
  {
    path: '/runtime',
    name: 'AIRuntime',
    component: AIRuntime
  },
  {
    path: '/results',
    name: 'ResultAnalysis',
    component: ResultAnalysis
  },
  {
    path: '/design',
    name: 'SystemDesign',
    component: SystemDesign
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

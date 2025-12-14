import { defineStore } from 'pinia'
import axios from 'axios'

export const useSystemStore = defineStore('system', {
  state: () => ({
    currentTask: null,
    currentStrategy: null,
    tasks: [],
    strategies: [],
    latestResult: null,
    isLoading: false,
    history: [],
    logs: [],
    stats: {
      totalTasks: 4,
      completedTasks: 0,
      strategies: 4,
      avgAccuracy: 87.5
    }
  }),

  actions: {
    async fetchConfig() {
      try {
        const response = await axios.get('/api/config')
        this.currentTask = response.data.current_task
        this.currentStrategy = response.data.current_strategy
      } catch (error) {
        console.error('Failed to fetch config:', error)
      }
    },

    async setTask(task) {
      try {
        await axios.post('/api/config/task', { task })
        this.currentTask = task
      } catch (error) {
        console.error('Failed to set task:', error)
      }
    },

    async setStrategy(strategy) {
      try {
        await axios.post('/api/config/strategy', { strategy })
        this.currentStrategy = strategy
      } catch (error) {
        console.error('Failed to set strategy:', error)
      }
    },

    async fetchTasks() {
      try {
        const response = await axios.get('/api/tasks')
        this.tasks = response.data
      } catch (error) {
        console.error('Failed to fetch tasks:', error)
      }
    },

    async fetchStrategies() {
      try {
        const response = await axios.get('/api/strategies')
        this.strategies = response.data
      } catch (error) {
        console.error('Failed to fetch strategies:', error)
      }
    },

    async runModel(task, strategy) {
      this.isLoading = true
      try {
        const response = await axios.post('/api/run', { task, strategy })
        this.latestResult = response.data.result
        await this.fetchStats()
        return response.data
      } catch (error) {
        console.error('Failed to run model:', error)
        throw error
      } finally {
        this.isLoading = false
      }
    },

    async fetchResults() {
      try {
        const response = await axios.get('/api/results')
        this.latestResult = response.data
      } catch (error) {
        console.error('Failed to fetch results:', error)
      }
    },

    async compareResults(strategies) {
      try {
        const response = await axios.post('/api/results/compare', { strategies })
        return response.data
      } catch (error) {
        console.error('Failed to compare results:', error)
        throw error
      }
    },

    async fetchHistory(page = 1, pageSize = 10) {
      try {
        const response = await axios.get('/api/history', {
          params: { page, page_size: pageSize }
        })
        this.history = response.data.data
        return response.data
      } catch (error) {
        console.error('Failed to fetch history:', error)
        throw error
      }
    },

    async deleteHistory(taskId) {
      try {
        await axios.delete(`/api/history/${taskId}`)
        await this.fetchHistory()
      } catch (error) {
        console.error('Failed to delete history:', error)
        throw error
      }
    },

    async fetchLogs(level = null, limit = 50) {
      try {
        const response = await axios.get('/api/logs', {
          params: { level, limit }
        })
        this.logs = response.data.data
        return response.data
      } catch (error) {
        console.error('Failed to fetch logs:', error)
        throw error
      }
    },

    async fetchStats() {
      try {
        const response = await axios.get('/api/stats')
        this.stats = response.data
        return response.data
      } catch (error) {
        console.error('Failed to fetch stats:', error)
      }
    },

    async exportData(type = 'json') {
      try {
        const response = await axios.post('/api/export', { type })
        return response.data
      } catch (error) {
        console.error('Failed to export data:', error)
        throw error
      }
    },

    async fetchSystemStatus() {
      try {
        const response = await axios.get('/api/system/status')
        return response.data
      } catch (error) {
        console.error('Failed to fetch system status:', error)
        throw error
      }
    }
  }
})

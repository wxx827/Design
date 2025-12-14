<template>
  <div class="app-layout">
    <header class="top-header">
      <div class="header-content">
        <div class="logo-section">
          <div class="logo">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
              <rect width="32" height="32" rx="6" fill="#1890ff"/>
              <path d="M16 8L20 12H12L16 8Z" fill="white"/>
              <rect x="12" y="14" width="8" height="10" rx="1" fill="white"/>
              <circle cx="16" cy="18" r="2" fill="#1890ff"/>
            </svg>
          </div>
          <span class="logo-text">智能决策系统</span>
        </div>

        <nav class="main-nav">
          <router-link to="/" class="nav-item">首页</router-link>
          <router-link to="/tasks" class="nav-item">任务中心</router-link>
          <router-link to="/strategy" class="nav-item">策略配置</router-link>
          <router-link to="/runtime" class="nav-item">执行控制</router-link>
          <router-link to="/results" class="nav-item">数据分析</router-link>
          <router-link to="/design" class="nav-item">系统架构</router-link>
        </nav>

        <div class="header-actions">
          <span class="user-info">Admin</span>
        </div>
      </div>
    </header>

    <main class="main-content">
      <router-view />
    </main>
  </div>
</template>

<script setup>
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.app-layout {
  min-height: 100vh;
  background: #f5f7fa;
}

.top-header {
  background: #ffffff;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  position: sticky;
  top: 0;
  z-index: 1000;
}

.header-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 24px;
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo-section {
  display: flex;
  align-items: center;
  gap: 12px;
}

.logo svg {
  display: block;
}

.logo-text {
  font-size: 18px;
  font-weight: 600;
  color: #1a1a1a;
}

.main-nav {
  display: flex;
  gap: 4px;
  flex: 1;
  margin: 0 40px;
}

.nav-item {
  padding: 8px 16px;
  color: #666;
  text-decoration: none;
  border-radius: 6px;
  transition: all 0.2s;
  font-size: 14px;
}

.nav-item:hover {
  color: #1890ff;
  background: #f0f5ff;
}

.nav-item.router-link-active {
  color: #1890ff;
  background: #e6f4ff;
  font-weight: 500;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 16px;
}

.user-info {
  color: #666;
  font-size: 14px;
  padding: 6px 16px;
  background: #f5f7fa;
  border-radius: 16px;
}

.main-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 24px;
  min-height: calc(100vh - 64px);
}
</style>

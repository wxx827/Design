<template>
  <div class="system-design">
    <nav class="navbar">
      <div class="nav-brand">
        <router-link to="/">← 返回首页</router-link>
      </div>
      <h1>🧩 系统设计说明</h1>
    </nav>

    <div class="content">
      <div class="page-header">
        <h2>系统架构与设计模式</h2>
        <p>基于多设计模式融合的智能AI决策系统</p>
      </div>

      <div class="design-container">
        <div class="design-card">
          <h3>🎯 系统核心思想</h3>
          <div class="core-concept">
            <p>
              本系统通过<strong>策略模式</strong>实现多AI算法的动态切换，
              通过<strong>工厂模式</strong>统一模型创建，
              通过<strong>观察者模式</strong>实现前端数据与状态的实时更新，
              通过<strong>模板方法模式</strong>规范AI处理流程，
              通过<strong>单例模式</strong>管理全局配置，
              最终构建一个<strong>多页面、可交互、可扩展的智能系统</strong>。
            </p>
          </div>
        </div>

        <div class="design-card">
          <h3>🏗 系统架构</h3>
          <div class="architecture">
            <div class="arch-layer">
              <h4>前端层 (Vue.js)</h4>
              <ul>
                <li>Dashboard - 系统首页</li>
                <li>Task Center - 任务选择</li>
                <li>Strategy Lab - 策略实验室</li>
                <li>AI Runtime - 运行控制台</li>
                <li>Result Analysis - 结果分析</li>
                <li>System Design - 设计说明</li>
              </ul>
            </div>
            <div class="arch-arrow">↓</div>
            <div class="arch-layer">
              <h4>API层 (Flask RESTful)</h4>
              <ul>
                <li>GET /api/config - 获取系统配置</li>
                <li>POST /api/run - 运行AI模型</li>
                <li>GET /api/results - 获取结果</li>
                <li>POST /api/results/compare - 结果对比</li>
              </ul>
            </div>
            <div class="arch-arrow">↓</div>
            <div class="arch-layer">
              <h4>设计模式层</h4>
              <ul>
                <li>单例模式 - 系统配置管理</li>
                <li>策略模式 - AI算法切换</li>
                <li>工厂模式 - 模型创建</li>
                <li>模板方法 - 统一流程</li>
                <li>观察者模式 - 状态通知</li>
              </ul>
            </div>
            <div class="arch-arrow">↓</div>
            <div class="arch-layer">
              <h4>AI模型层</h4>
              <ul>
                <li>数据预测模型</li>
                <li>图像分类模型</li>
                <li>智能推荐模型</li>
                <li>异常检测模型</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="design-card">
          <h3>🧩 设计模式详解</h3>
          <div class="patterns-detail">
            <div class="pattern-item">
              <div class="pattern-header">
                <span class="pattern-badge">策略模式</span>
                <span class="pattern-role">核心模式</span>
              </div>
              <h4>Strategy Pattern</h4>
              <p><strong>作用：</strong>实现多种AI算法的动态切换</p>
              <p><strong>实现：</strong>定义AIStrategy接口，4种具体策略(Baseline, DeepLearning, Attention, Ensemble)</p>
              <p><strong>优势：</strong>算法独立封装，可灵活切换，易于扩展新策略</p>
              <div class="code-block">
                <pre>class AIContext:
    def __init__(self, strategy_type):
        self._strategy = create_strategy(strategy_type)

    def execute_prediction(self, data):
        return self._strategy.predict(data)</pre>
              </div>
            </div>

            <div class="pattern-item">
              <div class="pattern-header">
                <span class="pattern-badge">工厂模式</span>
                <span class="pattern-role">模型创建</span>
              </div>
              <h4>Factory Pattern</h4>
              <p><strong>作用：</strong>根据任务类型创建对应的AI模型</p>
              <p><strong>实现：</strong>AIModelFactory统一创建4种模型实例</p>
              <p><strong>优势：</strong>解耦对象创建，支持多态，便于管理</p>
              <div class="code-block">
                <pre>class AIModelFactory:
    def create_model(self, task_type):
        models = {
            'prediction': PredictionModel,
            'classification': ClassificationModel
        }
        return models[task_type]()</pre>
              </div>
            </div>

            <div class="pattern-item">
              <div class="pattern-header">
                <span class="pattern-badge">模板方法模式</span>
                <span class="pattern-role">流程规范</span>
              </div>
              <h4>Template Method Pattern</h4>
              <p><strong>作用：</strong>定义AI处理的统一流程框架</p>
              <p><strong>实现：</strong>抽象类AIModel定义execute模板方法</p>
              <p><strong>流程：</strong>数据加载 → 预处理 → 推理 → 输出结果</p>
              <div class="code-block">
                <pre>class AIModel(ABC):
    def execute(self, context):
        self.load_data()
        self.preprocess()
        result = self.inference(context)
        return self.output_result()</pre>
              </div>
            </div>

            <div class="pattern-item">
              <div class="pattern-header">
                <span class="pattern-badge">观察者模式</span>
                <span class="pattern-role">实时更新</span>
              </div>
              <h4>Observer Pattern</h4>
              <p><strong>作用：</strong>AI结果变化时，自动通知观察者更新</p>
              <p><strong>实现：</strong>ResultSubject维护观察者列表，结果更新时通知</p>
              <p><strong>优势：</strong>实现发布-订阅，前端图表自动刷新</p>
              <div class="code-block">
                <pre>class ResultSubject:
    def set_result(self, result):
        self._result = result
        self.notify()  # 通知所有观察者

    def notify(self):
        for observer in self._observers:
            observer.update(self._result)</pre>
              </div>
            </div>

            <div class="pattern-item">
              <div class="pattern-header">
                <span class="pattern-badge">单例模式</span>
                <span class="pattern-role">全局配置</span>
              </div>
              <h4>Singleton Pattern</h4>
              <p><strong>作用：</strong>管理系统全局状态和配置</p>
              <p><strong>实现：</strong>SystemConfig单例类，存储当前任务和策略</p>
              <p><strong>优势：</strong>全局唯一实例，状态一致性保证</p>
              <div class="code-block">
                <pre>class SystemConfig:
    _instance = None

    @staticmethod
    def get_instance():
        if SystemConfig._instance is None:
            SystemConfig._instance = SystemConfig()
        return SystemConfig._instance</pre>
              </div>
            </div>
          </div>
        </div>

        <div class="design-card">
          <h3>🔗 页面流程图</h3>
          <div class="flow-diagram">
            <div class="flow-node">Dashboard<br/>系统首页</div>
            <div class="flow-arrow">↓</div>
            <div class="flow-node">Task Center<br/>选择任务类型</div>
            <div class="flow-arrow">↓</div>
            <div class="flow-node">Strategy Lab<br/>选择AI策略</div>
            <div class="flow-arrow">↓</div>
            <div class="flow-node">AI Runtime<br/>运行模型</div>
            <div class="flow-arrow">↓</div>
            <div class="flow-node">Result Analysis<br/>结果分析</div>
          </div>
        </div>

        <div class="design-card highlight-card">
          <h3>✨ 系统亮点</h3>
          <div class="highlights-grid">
            <div class="highlight-item">
              <div class="highlight-icon">🎨</div>
              <h4>5种设计模式融合</h4>
              <p>策略、工厂、模板方法、观察者、单例模式协同工作</p>
            </div>
            <div class="highlight-item">
              <div class="highlight-icon">🔄</div>
              <h4>完整的用户流程</h4>
              <p>从任务选择到结果分析的闭环体验</p>
            </div>
            <div class="highlight-item">
              <div class="highlight-icon">📊</div>
              <h4>可视化数据展示</h4>
              <p>Chart.js图表库实现实时数据可视化</p>
            </div>
            <div class="highlight-item">
              <div class="highlight-icon">🚀</div>
              <h4>前后端分离架构</h4>
              <p>Vue.js + Flask RESTful API设计</p>
            </div>
            <div class="highlight-item">
              <div class="highlight-icon">🔧</div>
              <h4>高可扩展性</h4>
              <p>易于添加新任务类型和AI策略</p>
            </div>
            <div class="highlight-item">
              <div class="highlight-icon">💡</div>
              <h4>实时状态管理</h4>
              <p>Pinia状态管理，响应式更新</p>
            </div>
          </div>
        </div>

        <div class="design-card">
          <h3>🎓 适用课程</h3>
          <ul class="course-list">
            <li>软件设计模式课程设计</li>
            <li>软件工程综合实践</li>
            <li>AI应用系统设计</li>
            <li>前端与后端综合开发</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.system-design {
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding-bottom: 3rem;
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

.design-container {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.design-card {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.design-card h3 {
  color: #333;
  font-size: 1.5rem;
  margin-bottom: 1.5rem;
  border-bottom: 3px solid #667eea;
  padding-bottom: 0.5rem;
}

.core-concept p {
  color: #666;
  line-height: 1.8;
  font-size: 1.05rem;
}

.core-concept strong {
  color: #667eea;
  font-weight: 600;
}

.architecture {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.arch-layer {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 12px;
  border-left: 4px solid #667eea;
}

.arch-layer h4 {
  color: #333;
  margin-bottom: 1rem;
  font-size: 1.1rem;
}

.arch-layer ul {
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 0.5rem;
}

.arch-layer li {
  color: #666;
  padding: 0.5rem;
  background: white;
  border-radius: 6px;
  font-size: 0.95rem;
}

.arch-arrow {
  text-align: center;
  font-size: 2rem;
  color: #667eea;
  font-weight: bold;
}

.patterns-detail {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.pattern-item {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 12px;
  border-left: 4px solid #667eea;
}

.pattern-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.pattern-badge {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.95rem;
}

.pattern-role {
  background: #10b981;
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 6px;
  font-size: 0.875rem;
}

.pattern-item h4 {
  color: #333;
  margin-bottom: 1rem;
  font-size: 1.2rem;
}

.pattern-item p {
  color: #666;
  margin: 0.5rem 0;
  line-height: 1.6;
}

.pattern-item strong {
  color: #333;
}

.code-block {
  background: #282c34;
  color: #abb2bf;
  padding: 1rem;
  border-radius: 8px;
  margin-top: 1rem;
  overflow-x: auto;
}

.code-block pre {
  margin: 0;
  font-family: 'Consolas', 'Monaco', monospace;
  font-size: 0.9rem;
  line-height: 1.5;
}

.flow-diagram {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  padding: 2rem;
}

.flow-node {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 1.5rem 3rem;
  border-radius: 12px;
  font-weight: 600;
  text-align: center;
  min-width: 250px;
  box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
}

.flow-arrow {
  font-size: 2rem;
  color: #667eea;
  font-weight: bold;
}

.highlight-card {
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
  border: 2px solid #667eea;
}

.highlights-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.highlight-item {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  text-align: center;
}

.highlight-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.highlight-item h4 {
  color: #333;
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
}

.highlight-item p {
  color: #666;
  font-size: 0.95rem;
  line-height: 1.6;
}

.course-list {
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
}

.course-list li {
  background: #f8f9fa;
  padding: 1rem;
  border-radius: 8px;
  color: #666;
  border-left: 4px solid #667eea;
  font-weight: 500;
}
</style>

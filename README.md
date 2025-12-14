# 智能决策系统 - Intelligent Decision System

> 基于多设计模式融合的现代化Web应用 | 参考Ant Design设计规范

## 🎨 UI设计重大升级

### 设计风格
- ✅ **现代清爽风格** - 参考Ant Design/阿里云控制台
- ✅ **白色主题** - 去除紫色渐变,采用白色/浅灰背景(#f5f7fa)
- ✅ **蓝色主色调** - 使用#1890ff作为品牌色
- ✅ **卡片化布局** - 白色卡片,轻微阴影,精致hover效果
- ✅ **SVG图标** - 专业的线性图标系统

### 界面组件
- **顶部导航栏** - 白色背景,固定顶部,清晰的路由高亮
- **统计卡片** - 带彩色图标的数据卡片(蓝/绿/橙/紫)
- **操作按钮** - 简洁边框,hover交互
- **状态徽章** - 绿色/橙色/红色状态指示

## 🚀 后端功能大幅增强

### 新增功能模块

#### 1. 任务历史管理
- `GET /api/history?page=1&page_size=10` - 分页查询历史
- `DELETE /api/history/:id` - 删除历史记录
- 自动记录每次任务执行(任务类型/策略/准确率/时间戳)
- 最多保留50条历史记录

#### 2. 系统日志
- `GET /api/logs?level=info&limit=50` - 查询系统日志
- 支持按日志级别过滤(info/success/error)
- 自动记录所有关键操作
- 最多保留100条日志

#### 3. 统计分析
- `GET /api/stats` - 获取系统统计数据
- 实时计算平均准确率
- 任务分布统计
- 执行次数统计

#### 4. 数据管理(CRUD)
- `GET /api/data` - 获取数据记录
- `POST /api/data` - 创建数据记录
- `DELETE /api/data/:id` - 删除数据记录

#### 5. 数据导出
- `POST /api/export` - 导出系统数据
- 支持JSON格式导出
- 包含配置/历史/日志完整数据

#### 6. 系统监控
- `GET /api/system/status` - 系统状态监控
- CPU/内存使用率
- 活跃任务数
- 最后执行记录

## 🏗 技术栈

### 前端
- **框架**: Vue 3.4 (Composition API)
- **路由**: Vue Router 4
- **状态管理**: Pinia
- **图表**: Chart.js
- **HTTP**: Axios
- **构建工具**: Vite 5
- **设计风格**: 参考Ant Design

### 后端
- **框架**: Flask 3.0
- **跨域**: Flask-CORS
- **数据处理**: NumPy + Scikit-learn
- **时间处理**: datetime

## 📦 项目结构

```
├── backend/
│   ├── app.py                    # Flask主应用(含15+个API)
│   ├── patterns/                 # 设计模式实现
│   │   ├── singleton.py          # 单例模式
│   │   ├── strategy.py           # 策略模式
│   │   ├── factory.py            # 工厂模式+模板方法
│   │   └── observer.py           # 观察者模式
│   └── requirements.txt
│
└── frontend/
    ├── src/
    │   ├── App.vue               # 主布局(现代导航栏)
    │   ├── views/                # 页面组件
    │   │   ├── Dashboard.vue     # ✅ 清爽首页
    │   │   ├── TaskCenter.vue    # ✅ 任务中心
    │   │   ├── StrategyLab.vue   # ✅ 策略配置
    │   │   ├── AIRuntime.vue     # ✅ 执行控制
    │   │   ├── ResultAnalysis.vue # ✅ 数据分析
    │   │   └── SystemDesign.vue  # ✅ 系统架构
    │   ├── router/index.js
    │   └── stores/system.js      # ✅ 增强Store(新增8个action)
    ├── index.html                # ✅ 白色主题
    └── vite.config.js
```

## 🚀 快速启动

### Windows
```bash
# 启动后端
start-backend.bat

# 启动前端(新终端)
start-frontend.bat
```

### Linux/Mac
```bash
# 启动后端
chmod +x start-backend.sh
./start-backend.sh

# 启动前端(新终端)
chmod +x start-frontend.sh
./start-frontend.sh
```

访问: http://localhost:3000

## 🎯 核心功能

### 首页Dashboard
- 4个统计卡片(任务总数/完成数/策略数/平均准确率)
- 实时系统配置显示
- 5种设计模式说明
- 快速导航卡片

### 任务中心
- 4种任务类型选择
- 卡片式展示,支持难度/分类标签
- 工厂模式实战应用

### 策略配置
- 4种AI策略(Baseline/DeepLearning/Attention/Ensemble)
- 准确率/速度/内存/复杂度对比
- 可视化对比图表
- 策略模式实战应用

### 执行控制
- 模型运行控制
- 4步执行流程可视化
- 模板方法模式实战应用
- 进度实时监控

### 数据分析
- 性能指标展示(准确率/精确度/召回率/F1)
- Chart.js图表可视化
- 多策略对比功能
- 观察者模式实战应用

### 系统架构
- 完整架构图
- 5种设计模式详解
- 代码示例
- 答辩重点内容

## 📊 API接口完整列表

### 配置管理
- `GET /api/config` - 获取配置
- `POST /api/config/task` - 设置任务
- `POST /api/config/strategy` - 设置策略

### 任务与策略
- `GET /api/tasks` - 获取任务列表
- `GET /api/strategies` - 获取策略列表
- `POST /api/run` - 运行AI模型

### 结果分析
- `GET /api/results` - 获取最新结果
- `POST /api/results/compare` - 策略对比

### 历史与日志(新)
- `GET /api/history` - 获取历史记录
- `DELETE /api/history/:id` - 删除历史
- `GET /api/logs` - 获取系统日志

### 统计与监控(新)
- `GET /api/stats` - 获取统计数据
- `GET /api/system/status` - 系统状态

### 数据管理(新)
- `GET /api/data` - 获取数据列表
- `POST /api/data` - 创建数据
- `DELETE /api/data/:id` - 删除数据
- `POST /api/export` - 导出数据

### 健康检查
- `GET /api/health` - 健康检查

## 🎨 设计模式详解

### 1. 策略模式(核心)
**应用场景**: 4种AI算法动态切换

```python
class AIContext:
    def __init__(self, strategy_type):
        self._strategy = self._create_strategy(strategy_type)

    def execute_prediction(self, data):
        return self._strategy.predict(data)
```

### 2. 工厂模式
**应用场景**: 根据任务类型创建AI模型

```python
class AIModelFactory:
    def create_model(self, task_type):
        models = {
            'prediction': PredictionModel,
            'classification': ClassificationModel,
            'recommendation': RecommendationModel,
            'anomaly': AnomalyDetectionModel
        }
        return models[task_type]()
```

### 3. 模板方法模式
**应用场景**: 统一AI处理流程

```python
class AIModel(ABC):
    def execute(self, context):
        self.load_data()        # 数据加载
        self.preprocess()       # 数据预处理
        result = self.inference(context)  # AI推理
        return self.output_result()       # 结果生成
```

### 4. 观察者模式
**应用场景**: 结果自动更新通知

```python
class ResultSubject:
    def set_result(self, result):
        self._result = result
        self.notify()  # 通知所有观察者
```

### 5. 单例模式
**应用场景**: 全局配置管理

```python
class SystemConfig:
    _instance = None

    @staticmethod
    def get_instance():
        if SystemConfig._instance is None:
            SystemConfig._instance = SystemConfig()
        return SystemConfig._instance
```

## ✨ 系统亮点

### UI/UX
- ✅ 现代化清爽设计,去除过度使用的紫色
- ✅ 专业的白色主题,符合主流产品设计
- ✅ 精致的SVG图标系统
- ✅ 流畅的hover交互效果
- ✅ 响应式布局,适配多种屏幕

### 后端功能
- ✅ 15+ REST API接口
- ✅ 完整的CRUD操作
- ✅ 任务历史记录管理
- ✅ 系统日志追踪
- ✅ 实时统计分析
- ✅ 数据导出功能
- ✅ 系统状态监控

### 架构设计
- ✅ 5种设计模式深度融合
- ✅ 前后端完全分离
- ✅ RESTful API规范
- ✅ Pinia状态管理
- ✅ 模块化组件设计
- ✅ 符合SOLID原则

## 📝 答辩要点

### 核心陈述
> 本系统采用现代化Web架构,前端使用Vue 3构建清爽的用户界面,后端使用Flask提供RESTful API服务。系统深度融合5种经典设计模式,不仅完成了AI功能的实现,还提供了完整的数据管理、历史追踪、日志监控、统计分析等企业级功能,展现了从课程学习到实际应用的完整转化。

### 技术亮点
1. **UI设计** - 参考Ant Design规范,现代化清爽风格
2. **功能完整** - 不只是AI演示,包含完整的数据管理功能
3. **架构清晰** - 前后端分离,RESTful API
4. **模式深度** - 5种设计模式相互配合,解决实际问题
5. **可扩展性** - 易于添加新功能、新策略、新任务

## 🔧 开发建议

### 添加新任务类型
1. 在`patterns/factory.py`添加新Model类
2. 在`app.py`的tasks列表中注册
3. 前端TaskCenter自动展示

### 添加新AI策略
1. 在`patterns/strategy.py`添加新Strategy类
2. 在AIContext的strategies字典中注册
3. 前端StrategyLab自动展示

### 自定义配色
修改`frontend/src/App.vue`和各页面的CSS变量:
- 主色: `#1890ff`
- 成功色: `#52c41a`
- 警告色: `#fa8c16`
- 危险色: `#f5222d`

## 📄 许可证

MIT License

## 👨‍💻 开发者

人工智能与软件工程专业 | 2025

---

**Note**: 本项目为课程设计,展示了设计模式在实际Web应用中的综合运用,同时提供了现代化的UI设计和完整的后端功能,适合作为答辩项目。

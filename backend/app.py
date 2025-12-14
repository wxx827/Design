from flask import Flask, jsonify, request
from flask_cors import CORS
from patterns.singleton import SystemConfig
from patterns.factory import AIModelFactory
from patterns.strategy import AIContext
from patterns.observer import ResultObserver, ResultSubject
from datetime import datetime
import time
import json

app = Flask(__name__)
CORS(app)

result_subject = ResultSubject()
result_observer = ResultObserver()
result_subject.attach(result_observer)

task_history = []
system_logs = []
data_records = []

def add_log(level, message):
    log_entry = {
        'id': len(system_logs) + 1,
        'timestamp': datetime.now().isoformat(),
        'level': level,
        'message': message
    }
    system_logs.append(log_entry)
    if len(system_logs) > 100:
        system_logs.pop(0)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'ok',
        'message': 'System is running',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

@app.route('/api/config', methods=['GET'])
def get_config():
    config = SystemConfig.get_instance()
    return jsonify({
        'current_task': config.get_current_task(),
        'current_strategy': config.get_current_strategy(),
        'system_name': 'Intelligent Decision System',
        'version': '1.0.0'
    })

@app.route('/api/config/task', methods=['POST'])
def set_task():
    data = request.get_json()
    config = SystemConfig.get_instance()
    config.set_current_task(data.get('task'))
    add_log('info', f'任务设置为: {data.get("task")}')
    return jsonify({'status': 'success', 'task': config.get_current_task()})

@app.route('/api/config/strategy', methods=['POST'])
def set_strategy():
    data = request.get_json()
    config = SystemConfig.get_instance()
    config.set_current_strategy(data.get('strategy'))
    add_log('info', f'策略设置为: {data.get("strategy")}')
    return jsonify({'status': 'success', 'strategy': config.get_current_strategy()})

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = [
        {
            'id': 'prediction',
            'name': '数据预测',
            'icon': '📈',
            'description': '基于历史数据进行未来趋势预测',
            'category': '时序分析',
            'difficulty': 'medium'
        },
        {
            'id': 'classification',
            'name': '图像分类',
            'icon': '🖼️',
            'description': '对图像进行智能分类识别',
            'category': '计算机视觉',
            'difficulty': 'hard'
        },
        {
            'id': 'recommendation',
            'name': '智能推荐',
            'icon': '🎯',
            'description': '基于用户行为的个性化推荐',
            'category': '推荐系统',
            'difficulty': 'medium'
        },
        {
            'id': 'anomaly',
            'name': '异常检测',
            'icon': '🔍',
            'description': '检测数据中的异常模式',
            'category': '异常分析',
            'difficulty': 'easy'
        }
    ]
    return jsonify(tasks)

@app.route('/api/strategies', methods=['GET'])
def get_strategies():
    strategies = [
        {
            'id': 'baseline',
            'name': '基础模型',
            'description': '使用传统机器学习算法，快速高效',
            'accuracy': 0.75,
            'speed': 'fast',
            'memory': 'low',
            'complexity': 'low'
        },
        {
            'id': 'deep_learning',
            'name': '深度学习模型',
            'description': '使用神经网络，准确度高',
            'accuracy': 0.88,
            'speed': 'medium',
            'memory': 'medium',
            'complexity': 'medium'
        },
        {
            'id': 'attention',
            'name': 'Attention增强模型',
            'description': '结合注意力机制，性能卓越',
            'accuracy': 0.92,
            'speed': 'medium',
            'memory': 'high',
            'complexity': 'high'
        },
        {
            'id': 'ensemble',
            'name': '集成学习模型',
            'description': '多模型融合，准确度最高',
            'accuracy': 0.95,
            'speed': 'slow',
            'memory': 'high',
            'complexity': 'high'
        }
    ]
    return jsonify(strategies)

@app.route('/api/run', methods=['POST'])
def run_model():
    data = request.get_json()
    task_type = data.get('task', 'prediction')
    strategy_id = data.get('strategy', 'baseline')

    config = SystemConfig.get_instance()
    config.set_current_task(task_type)
    config.set_current_strategy(strategy_id)

    factory = AIModelFactory()
    model = factory.create_model(task_type)
    context = AIContext(strategy_id)

    add_log('info', f'开始执行任务: {task_type}, 策略: {strategy_id}')

    progress_updates = []
    for step in ['数据加载', '数据预处理', 'AI推理', '结果生成']:
        progress_updates.append({'step': step, 'status': 'completed'})

    result = model.execute(context)
    result_subject.set_result(result)

    history_entry = {
        'id': len(task_history) + 1,
        'task': task_type,
        'strategy': strategy_id,
        'timestamp': datetime.now().isoformat(),
        'accuracy': result['metrics']['accuracy'],
        'status': 'completed'
    }
    task_history.append(history_entry)
    if len(task_history) > 50:
        task_history.pop(0)

    add_log('success', f'任务执行成功: {task_type}')

    return jsonify({
        'status': 'success',
        'progress': progress_updates,
        'result': result,
        'execution_id': history_entry['id']
    })

@app.route('/api/results', methods=['GET'])
def get_results():
    return jsonify(result_observer.get_latest_result())

@app.route('/api/results/compare', methods=['POST'])
def compare_results():
    data = request.get_json()
    strategies = data.get('strategies', [])

    comparison_data = []
    for strategy_id in strategies:
        context = AIContext(strategy_id)
        config = SystemConfig.get_instance()
        task_type = config.get_current_task() or 'prediction'

        factory = AIModelFactory()
        model = factory.create_model(task_type)
        result = model.execute(context)

        comparison_data.append({
            'strategy': strategy_id,
            'result': result
        })

    add_log('info', f'策略对比完成，共对比 {len(strategies)} 个策略')
    return jsonify(comparison_data)

@app.route('/api/history', methods=['GET'])
def get_history():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))

    start = (page - 1) * page_size
    end = start + page_size

    return jsonify({
        'total': len(task_history),
        'page': page,
        'page_size': page_size,
        'data': list(reversed(task_history))[start:end]
    })

@app.route('/api/history/<int:task_id>', methods=['DELETE'])
def delete_history(task_id):
    global task_history
    task_history = [h for h in task_history if h['id'] != task_id]
    add_log('info', f'删除历史记录: {task_id}')
    return jsonify({'status': 'success', 'message': 'History deleted'})

@app.route('/api/logs', methods=['GET'])
def get_logs():
    level = request.args.get('level', None)
    limit = int(request.args.get('limit', 50))

    logs = system_logs
    if level:
        logs = [log for log in logs if log['level'] == level]

    return jsonify({
        'total': len(logs),
        'data': list(reversed(logs))[:limit]
    })

@app.route('/api/stats', methods=['GET'])
def get_stats():
    completed_count = len([h for h in task_history if h['status'] == 'completed'])

    if task_history:
        avg_accuracy = sum(h['accuracy'] for h in task_history) / len(task_history)
    else:
        avg_accuracy = 0

    task_distribution = {}
    for h in task_history:
        task_type = h['task']
        task_distribution[task_type] = task_distribution.get(task_type, 0) + 1

    return jsonify({
        'total_tasks': 4,
        'completed_tasks': completed_count,
        'total_executions': len(task_history),
        'strategies': 4,
        'avg_accuracy': round(avg_accuracy * 100, 1) if avg_accuracy else 87.5,
        'task_distribution': task_distribution,
        'system_uptime': '正常运行',
        'memory_usage': '正常'
    })

@app.route('/api/data', methods=['GET'])
def get_data_records():
    return jsonify({
        'total': len(data_records),
        'data': data_records
    })

@app.route('/api/data', methods=['POST'])
def create_data_record():
    data = request.get_json()
    record = {
        'id': len(data_records) + 1,
        'name': data.get('name'),
        'type': data.get('type'),
        'size': data.get('size'),
        'created_at': datetime.now().isoformat()
    }
    data_records.append(record)
    add_log('info', f'创建数据记录: {record["name"]}')
    return jsonify({'status': 'success', 'data': record})

@app.route('/api/data/<int:data_id>', methods=['DELETE'])
def delete_data_record(data_id):
    global data_records
    data_records = [d for d in data_records if d['id'] != data_id]
    add_log('info', f'删除数据记录: {data_id}')
    return jsonify({'status': 'success', 'message': 'Data deleted'})

@app.route('/api/export', methods=['POST'])
def export_data():
    data = request.get_json()
    export_type = data.get('type', 'json')

    export_data = {
        'timestamp': datetime.now().isoformat(),
        'config': {
            'task': SystemConfig.get_instance().get_current_task(),
            'strategy': SystemConfig.get_instance().get_current_strategy()
        },
        'history': task_history,
        'logs': system_logs
    }

    add_log('info', f'导出数据，格式: {export_type}')

    return jsonify({
        'status': 'success',
        'data': export_data,
        'format': export_type
    })

@app.route('/api/system/status', methods=['GET'])
def system_status():
    return jsonify({
        'status': 'running',
        'uptime': '正常运行',
        'cpu_usage': '15%',
        'memory_usage': '256 MB',
        'active_tasks': len(task_history),
        'total_logs': len(system_logs),
        'last_execution': task_history[-1] if task_history else None
    })

if __name__ == '__main__':
    add_log('info', '系统启动')
    app.run(debug=True, host='0.0.0.0', port=5000)

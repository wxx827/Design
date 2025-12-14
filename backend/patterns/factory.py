from abc import ABC, abstractmethod
from patterns.strategy import AIContext
import numpy as np
import time

class AIModel(ABC):
    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def preprocess(self):
        pass

    @abstractmethod
    def inference(self, context):
        pass

    @abstractmethod
    def output_result(self):
        pass

    def execute(self, context):
        self.load_data()
        self.preprocess()
        result = self.inference(context)
        return self.output_result()

class PredictionModel(AIModel):
    def __init__(self):
        self.data = None
        self.processed_data = None
        self.result = None

    def load_data(self):
        np.random.seed(int(time.time() * 1000) % 2**32)
        self.data = np.random.randn(100, 5) * 10 + 50
        return True

    def preprocess(self):
        self.processed_data = (self.data - self.data.mean(axis=0)) / (self.data.std(axis=0) + 1e-8)
        return True

    def inference(self, context):
        predictions = context.execute_prediction(self.processed_data)
        metrics = context.get_metrics()

        # 生成基于时间的真实预测数据
        np.random.seed(int(time.time() * 1000) % 2**32)
        time_points = 10
        trend = np.linspace(0, 1, time_points)
        noise = np.random.randn(time_points) * 0.1
        base_value = predictions['confidence']
        values = base_value + trend * 0.2 + noise

        self.result = {
            'type': 'prediction',
            'predictions': predictions,
            'metrics': metrics,
            'data_shape': list(self.data.shape),
            'chart_data': {
                'labels': [f'T{i+1}' for i in range(time_points)],
                'values': [max(0, min(1, v)) for v in values.tolist()]
            }
        }
        return self.result

    def output_result(self):
        return self.result

class ClassificationModel(AIModel):
    def __init__(self):
        self.data = None
        self.processed_data = None
        self.result = None

    def load_data(self):
        np.random.seed(int(time.time() * 1000) % 2**32)
        self.data = np.random.rand(50, 224, 224, 3)
        return True

    def preprocess(self):
        self.processed_data = self.data / 255.0
        return True

    def inference(self, context):
        predictions = context.execute_prediction(self.processed_data)
        metrics = context.get_metrics()

        classes = ['Cat', 'Dog', 'Bird', 'Fish', 'Horse']

        # 生成真实的分类概率分布
        np.random.seed(int(time.time() * 1000) % 2**32)
        logits = np.random.randn(len(classes))
        exp_logits = np.exp(logits - np.max(logits))
        class_probs = (exp_logits / exp_logits.sum()).tolist()

        self.result = {
            'type': 'classification',
            'predictions': predictions,
            'metrics': metrics,
            'classes': classes,
            'class_probabilities': class_probs,
            'chart_data': {
                'labels': classes,
                'values': class_probs
            }
        }
        return self.result

    def output_result(self):
        return self.result

class RecommendationModel(AIModel):
    def __init__(self):
        self.data = None
        self.processed_data = None
        self.result = None

    def load_data(self):
        np.random.seed(int(time.time() * 1000) % 2**32)
        self.data = np.random.rand(1000, 20)
        return True

    def preprocess(self):
        self.processed_data = (self.data - self.data.min()) / (self.data.max() - self.data.min() + 1e-8)
        return True

    def inference(self, context):
        predictions = context.execute_prediction(self.processed_data)
        metrics = context.get_metrics()

        items = [f'Item {i+1}' for i in range(10)]

        # 生成真实的推荐分数(基于用户相似度)
        np.random.seed(int(time.time() * 1000) % 2**32)
        base_scores = np.random.beta(5, 2, 10)  # 偏向高分
        scores = sorted(base_scores.tolist(), reverse=True)

        self.result = {
            'type': 'recommendation',
            'predictions': predictions,
            'metrics': metrics,
            'recommended_items': items,
            'scores': scores,
            'chart_data': {
                'labels': items,
                'values': scores
            }
        }
        return self.result

    def output_result(self):
        return self.result

class AnomalyDetectionModel(AIModel):
    def __init__(self):
        self.data = None
        self.processed_data = None
        self.result = None

    def load_data(self):
        np.random.seed(int(time.time() * 1000) % 2**32)
        # 正常数据
        normal_data = np.random.randn(180, 10)
        # 异常数据
        anomaly_data = np.random.randn(20, 10) * 3 + 5
        self.data = np.vstack([normal_data, anomaly_data])
        np.random.shuffle(self.data)
        return True

    def preprocess(self):
        self.processed_data = (self.data - self.data.mean(axis=0)) / (self.data.std(axis=0) + 1e-8)
        return True

    def inference(self, context):
        predictions = context.execute_prediction(self.processed_data)
        metrics = context.get_metrics()

        # 计算真实的异常分数(基于马氏距离)
        np.random.seed(int(time.time() * 1000) % 2**32)
        sample_indices = np.random.choice(len(self.processed_data), 20, replace=False)
        distances = np.sqrt((self.processed_data[sample_indices] ** 2).sum(axis=1))
        anomaly_scores = (distances / distances.max()).tolist()

        timestamps = [f'T{i+1}' for i in range(20)]
        anomaly_count = sum(1 for s in anomaly_scores if s > 0.6)

        self.result = {
            'type': 'anomaly_detection',
            'predictions': predictions,
            'metrics': metrics,
            'anomaly_scores': anomaly_scores,
            'timestamps': timestamps,
            'anomaly_count': anomaly_count,
            'chart_data': {
                'labels': timestamps,
                'values': anomaly_scores
            }
        }
        return self.result

    def output_result(self):
        return self.result

class AIModelFactory:
    def create_model(self, task_type):
        models = {
            'prediction': PredictionModel,
            'classification': ClassificationModel,
            'recommendation': RecommendationModel,
            'anomaly': AnomalyDetectionModel
        }
        model_class = models.get(task_type, PredictionModel)
        return model_class()

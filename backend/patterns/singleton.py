class SystemConfig:
    _instance = None

    def __init__(self):
        if SystemConfig._instance is not None:
            raise Exception("This is a singleton class!")
        else:
            self._current_task = None
            self._current_strategy = None
            self._system_state = {
                'initialized': True,
                'running': False
            }

    @staticmethod
    def get_instance():
        if SystemConfig._instance is None:
            SystemConfig._instance = SystemConfig()
        return SystemConfig._instance

    def get_current_task(self):
        return self._current_task

    def set_current_task(self, task):
        self._current_task = task
        return self._current_task

    def get_current_strategy(self):
        return self._current_strategy

    def set_current_strategy(self, strategy):
        self._current_strategy = strategy
        return self._current_strategy

    def get_state(self):
        return self._system_state

    def update_state(self, key, value):
        self._system_state[key] = value

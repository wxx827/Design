from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, result):
        pass

class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class ResultObserver(Observer):
    def __init__(self):
        self._latest_result = None
        self._result_history = []

    def update(self, result):
        self._latest_result = result
        self._result_history.append(result)
        if len(self._result_history) > 10:
            self._result_history.pop(0)

    def get_latest_result(self):
        return self._latest_result

    def get_history(self):
        return self._result_history

class ResultSubject(Subject):
    def __init__(self):
        self._observers = []
        self._result = None

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._result)

    def set_result(self, result):
        self._result = result
        self.notify()

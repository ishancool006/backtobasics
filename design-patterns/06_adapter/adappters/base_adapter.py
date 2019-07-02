from abc import ABC, abstractmethod


class BaseAdapter(ABC):
    @abstractmethod
    def connect(self, parameters=None):
        return "BaseAdapter"

    @abstractmethod
    def execute(self, query):
        return "BaseAdapter"

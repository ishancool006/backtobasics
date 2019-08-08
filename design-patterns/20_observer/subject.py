from abc import ABCMeta, ABC, abstractmethod
from typing import List
from observer import Observer


class Subject(ABC):
    @abstractmethod
    def registerObserver(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def unregisterObserver(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notifyObservers(self) -> None:
        pass


class CricketData(Subject):
    _runs = None
    _overs = None
    _wickets = None

    def __init__(self):
        self._observers: List[Observer] = []

    def registerObserver(self, observer: Observer) -> None:
        self._observers.append(observer)

    def unregisterObserver(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notifyObservers(self) -> None:
        for observer in self._observers:
            observer.update(self._runs, self._wickets, self._overs)

    def __get_latest_runs(self):
        return 90

    def __get_latest_overs(self):
        return 10.2

    def __get_latest_wickets(self):
        return 2

    def data_change(self):
        self._runs = self.__get_latest_runs()
        self._overs = self.__get_latest_overs()
        self._wickets = self.__get_latest_wickets()

        self.notifyObservers()

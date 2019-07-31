from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, runs: int, wickets: int, overs: float):
        pass


class AverageScoreDisplay(Observer):
    _run_rate = None
    _predicted_score = None

    def update(self, runs: int, wickets: int, overs: float):
        self._run_rate = runs / overs
        self._predicted_score = self._run_rate * 50

        self.__display()

    def __display(self):
        print(
            "\nAverage Score Display:\n" + "Run Rate: ",
            self._run_rate,
            "\nPredictedScore:",
            self._predicted_score,
        )


class CurrnetScoreDisplay(Observer):
    _runs = None
    _overs = None
    _wicket = None

    def update(self, runs: int, wickets: int, overs: float):
        self._runs = runs
        self._wickets = wickets
        self._overs = overs

        self.__display()

    def __display(self):
        print(
            "\nCurrent Score Display:\n" + "Runs: ",
            self._runs,
            "\nWickets:",
            self._wickets,
            "\nOvers: ",
            self._overs,
        )

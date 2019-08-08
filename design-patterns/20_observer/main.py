from observer import AverageScoreDisplay, CurrnetScoreDisplay
from subject import CricketData

if __name__ == "__main__":

    observer_a = AverageScoreDisplay()
    observer_b = CurrnetScoreDisplay()

    cricket_data = CricketData()
    cricket_data.registerObserver(observer_a)
    cricket_data.registerObserver(observer_b)

    # cricket_data.data_change()

    cricket_data.unregisterObserver(observer_a)
    cricket_data.data_change()

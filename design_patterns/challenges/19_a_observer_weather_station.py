
from abc import ABC, abstractmethod
from typing import List

"""
Challenge: Weather Station with Observer Pattern

Design a weather station system where weather data (temperature, humidity, pressure) changes,
and multiple display elements (e.g., Current Conditions Display, Statistics Display) need to be updated automatically.

Your task is to:
1.  Define an abstract `WeatherStationSubject` class (Subject interface) with methods:
    -   `register_observer(observer: 'WeatherDisplayObserver')`
    -   `remove_observer(observer: 'WeatherDisplayObserver')`
    -   `notify_observers()`
2.  Define an abstract `WeatherDisplayObserver` class (Observer interface) with an abstract `update(temperature: float, humidity: float, pressure: float)` method.
3.  Implement a `WeatherData` class (Concrete Subject) that inherits from `WeatherStationSubject`.
    -   It should store the current `temperature`, `humidity`, and `pressure`.
    -   It should implement `register_observer`, `remove_observer`, and `notify_observers`.
    -   It should have a `set_measurements(temperature, humidity, pressure)` method that updates the data and calls `notify_observers()`.
4.  Implement concrete display classes (Concrete Observers) that inherit from `WeatherDisplayObserver`:
    -   `CurrentConditionsDisplay`: Displays the current temperature and humidity.
    -   `StatisticsDisplay`: Calculates and displays the average, max, and min temperature.
    Each display should register itself with the `WeatherData` subject in its constructor and implement the `update()` method to refresh its display.

"""

# Subject Interface
class WeatherStationSubject(ABC):
    @abstractmethod
    def register_observer(self, observer: 'WeatherDisplayObserver'):
        pass

    @abstractmethod
    def remove_observer(self, observer: 'WeatherDisplayObserver'):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

# Observer Interface
class WeatherDisplayObserver(ABC):
    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float):
        pass

# Concrete Subject
class WeatherData(WeatherStationSubject):
    def __init__(self):
        self._observers: List[WeatherDisplayObserver] = []
        self._temperature: float = 0.0
        self._humidity: float = 0.0
        self._pressure: float = 0.0

    def register_observer(self, observer: WeatherDisplayObserver):
        # TODO: Implement registration
        pass

    def remove_observer(self, observer: WeatherDisplayObserver):
        # TODO: Implement removal
        pass

    def notify_observers(self):
        # TODO: Implement notification
        pass

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()

# Concrete Observers
class CurrentConditionsDisplay(WeatherDisplayObserver):
    def __init__(self, weather_data: WeatherData):
        self._temperature = 0.0
        self._humidity = 0.0
        self._weather_data = weather_data
        # TODO: Register with weather_data
        pass

    def update(self, temperature: float, humidity: float, pressure: float):
        # TODO: Update internal state and display
        pass

    def display(self):
        print(f"Current conditions: {self._temperature}°F and {self._humidity}% humidity")

class StatisticsDisplay(WeatherDisplayObserver):
    def __init__(self, weather_data: WeatherData):
        self._max_temp = 0.0
        self._min_temp = 200.0
        self._temp_sum = 0.0
        self._num_readings = 0
        self._weather_data = weather_data
        # TODO: Register with weather_data
        pass

    def update(self, temperature: float, humidity: float, pressure: float):
        # TODO: Update internal state (calculate stats) and display
        pass

    def display(self):
        print(f"Avg/Max/Min temperature = {self._temp_sum / self._num_readings:.2f}/{self._max_temp}/{self._min_temp}")


# --- Tests ---
def run_tests():
    print("Running Observer Pattern Weather Station Tests...")

    weather_data = WeatherData()

    current_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)

    # Capture print output for testing
    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        print("\nFirst set of measurements:")
        weather_data.set_measurements(80, 65, 30.4)
    output = f.getvalue()
    assert "Current conditions: 80.0°F and 65.0% humidity" in output
    assert "Avg/Max/Min temperature = 80.00/80.0/80.0" in output
    print("First set of measurements test passed.")

    f = io.StringIO()
    with redirect_stdout(f):
        print("\nSecond set of measurements:")
        weather_data.set_measurements(82, 70, 29.2)
    output = f.getvalue()
    assert "Current conditions: 82.0°F and 70.0% humidity" in output
    assert "Avg/Max/Min temperature = 81.00/82.0/80.0" in output
    print("Second set of measurements test passed.")

    f = io.StringIO()
    with redirect_stdout(f):
        print("\nRemoving statistics display and new measurements:")
        weather_data.remove_observer(statistics_display)
        weather_data.set_measurements(78, 90, 29.2)
    output = f.getvalue()
    assert "Current conditions: 78.0°F and 90.0% humidity" in output
    assert "Avg/Max/Min temperature" not in output # StatisticsDisplay should not update
    print("Remove observer test passed.")

    print("All Observer Pattern Weather Station Tests Passed!")

if __name__ == "__main__":
    run_tests()

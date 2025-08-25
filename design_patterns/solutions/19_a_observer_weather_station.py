
from abc import ABC, abstractmethod
from typing import List

"""
Solution for: Weather Station with Observer Pattern
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
        self._observers.append(observer)

    def remove_observer(self, observer: WeatherDisplayObserver):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

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
        self._weather_data.register_observer(self)

    def update(self, temperature: float, humidity: float, pressure: float):
        self._temperature = temperature
        self._humidity = humidity
        self.display()

    def display(self):
        print(f"Current conditions: {self._temperature}°F and {self._humidity}% humidity")

class StatisticsDisplay(WeatherDisplayObserver):
    def __init__(self, weather_data: WeatherData):
        self._max_temp = 0.0
        self._min_temp = 200.0
        self._temp_sum = 0.0
        self._num_readings = 0
        self._weather_data = weather_data
        self._weather_data.register_observer(self)

    def update(self, temperature: float, humidity: float, pressure: float):
        self._temp_sum += temperature
        self._num_readings += 1
        if temperature > self._max_temp:
            self._max_temp = temperature
        if temperature < self._min_temp:
            self._min_temp = temperature
        self.display()

    def display(self):
        print(f"Avg/Max/Min temperature = {self._temp_sum / self._num_readings:.2f}/{self._max_temp}/{self._min_temp}")

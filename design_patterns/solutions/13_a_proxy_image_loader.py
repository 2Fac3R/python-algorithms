
import time
from abc import ABC, abstractmethod

"""
Solution for: Image Loader Proxy
"""

# Subject Interface
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# Real Subject
class RealImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._load_image_from_disk() # Simulate heavy loading

    def _load_image_from_disk(self):
        print(f"Loading {self.filename} from disk...")
        # Simulate a delay for loading a large image
        time.sleep(1)
        print(f"Finished loading {self.filename}.")

    def display(self):
        return f"Displaying {self.filename}"

# Proxy
class ProxyImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._real_image = None # RealImage is not loaded yet

    def display(self):
        if self._real_image is None:
            print(f"Proxy: Real image for {self.filename} not loaded. Loading now...")
            self._real_image = RealImage(self.filename)
        return self._real_image.display()

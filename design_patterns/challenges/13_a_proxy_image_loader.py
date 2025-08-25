from abc import ABC, abstractmethod

"""
Challenge: Image Loader Proxy

Design an image loading system where loading a large image from disk is a resource-intensive operation.
You want to implement lazy loading, meaning the image is only loaded when it's actually displayed.

Your task is to:
1.  Define an abstract `Image` class (Subject interface) with an abstract `display()` method.
2.  Implement a `RealImage` class (Real Subject) that inherits from `Image`.
    -   Its constructor should take a `filename`.
    -   It should simulate a heavy loading operation (e.g., print "Loading..." and `time.sleep(1)`) in its constructor.
    -   Its `display()` method should return a string indicating it's displaying the image.
3.  Implement a `ProxyImage` class (Proxy) that inherits from `Image`.
    -   Its constructor should take a `filename`.
    -   It should *not* load the `RealImage` in its constructor.
    -   Its `display()` method should check if the `RealImage` has been loaded. If not, it should create a `RealImage` instance (triggering the heavy load) and then delegate the `display()` call to it. If already loaded, it just delegates.

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
        # TODO: Simulate heavy loading here
        pass

    def display(self):
        # TODO: Return display string
        pass

# Proxy
class ProxyImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._real_image = None # RealImage is not loaded yet

    def display(self):
        # TODO: Implement lazy loading logic
        pass


# --- Tests ---
def run_tests():
    print("Running Proxy Pattern Image Loader Tests...")

    # Test RealImage (should load immediately)
    print("\n--- Testing RealImage (direct load) ---")
    import time
    start_time = time.time()
    real_image = RealImage("large_photo.jpg")
    end_time = time.time()
    print(f"RealImage constructor took {end_time - start_time:.2f} seconds.")
    assert real_image.display() == "Displaying large_photo.jpg"
    print("RealImage test passed.")

    # Test ProxyImage (should lazy load)
    print("\n--- Testing ProxyImage (lazy load) ---")
    start_time = time.time()
    proxy_image = ProxyImage("remote_image.png")
    end_time = time.time()
    print(f"ProxyImage constructor took {end_time - start_time:.2f} seconds (should be fast).")
    assert proxy_image._real_image is None, "RealImage should not be loaded yet."

    print("First display call (should trigger load):")
    start_time = time.time()
    assert proxy_image.display() == "Displaying remote_image.png"
    end_time = time.time()
    print(f"First display call took {end_time - start_time:.2f} seconds (should include load time).")
    assert proxy_image._real_image is not None, "RealImage should be loaded after first display."

    print("Second display call (should NOT trigger load):")
    start_time = time.time()
    assert proxy_image.display() == "Displaying remote_image.png"
    end_time = time.time()
    print(f"Second display call took {end_time - start_time:.2f} seconds (should be fast).")

    print("ProxyImage test passed.")

    print("All Proxy Pattern Image Loader Tests Passed!")

if __name__ == "__main__":
    run_tests()

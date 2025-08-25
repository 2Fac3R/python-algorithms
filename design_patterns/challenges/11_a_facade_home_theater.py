
"""
Challenge: Home Theater Facade

Design a home theater system using the Facade pattern. The system consists of several complex components
like a Projector, Screen, Amplifier, and DVD Player. You want to provide a simplified interface
for common tasks like "watching a movie" and "ending a movie".

Your task is to:
1.  Define the following subsystem classes with their respective methods:
    -   `Projector`:
        -   `on()`: Returns "Projector ON"
        -   `off()`: Returns "Projector OFF"
        -   `wide_screen_mode()`: Returns "Projector in widescreen mode"
    -   `Screen`:
        -   `up()`: Returns "Screen UP"
        -   `down()`: Returns "Screen DOWN"
    -   `Amplifier`:
        -   `on()`: Returns "Amplifier ON"
        -   `off()`: Returns "Amplifier OFF"
        -   `set_volume(volume)`: Returns "Amplifier volume set to {volume}"
        -   `set_dvd()`: Returns "Amplifier input set to DVD"
    -   `DVDPlayer`:
        -   `on()`: Returns "DVD Player ON"
        -   `off()`: Returns "DVD Player OFF"
        -   `play(movie)`: Returns "Playing movie: {movie}"
2.  Implement a `HomeTheaterFacade` class that takes instances of the subsystem classes in its constructor.
3.  Implement the following simplified methods in `HomeTheaterFacade`:
    -   `watch_movie(movie: str)`: Orchestrates the subsystem components to start watching a movie.
        (e.g., screen down, projector on, amplifier on, set input, set volume, DVD player on, play movie)
    -   `end_movie()`: Orchestrates the subsystem components to shut down the home theater.
        (e.g., DVD player off, amplifier off, projector off, screen up)

"

# Subsystem Classes
class Projector:
    def on(self):
        return "Projector ON"

    def off(self):
        return "Projector OFF"

    def wide_screen_mode(self):
        return "Projector in widescreen mode"

class Screen:
    def up(self):
        return "Screen UP"

    def down(self):
        return "Screen DOWN"

class Amplifier:
    def on(self):
        return "Amplifier ON"

    def off(self):
        return "Amplifier OFF"

    def set_volume(self, volume):
        return f"Amplifier volume set to {volume}"

    def set_dvd(self):
        return "Amplifier input set to DVD"

class DVDPlayer:
    def on(self):
        return "DVD Player ON"

    def off(self):
        return "DVD Player OFF"

    def play(self, movie):
        return f"Playing movie: {movie}"

# Facade
class HomeTheaterFacade:
    def __init__(self, projector: Projector, screen: Screen, amplifier: Amplifier, dvd_player: DVDPlayer):
        self.projector = projector
        self.screen = screen
        self.amplifier = amplifier
        self.dvd_player = dvd_player

    def watch_movie(self, movie: str):
        results = []
        # TODO: Implement the sequence of calls to subsystem components to watch a movie
        # Example sequence: screen down, projector on, projector widescreen, amplifier on, amplifier set DVD, amplifier set volume, DVD player on, DVD player play movie
        return "\n".join(results)

    def end_movie(self):
        results = []
        # TODO: Implement the sequence of calls to subsystem components to end a movie
        # Example sequence: DVD player off, amplifier off, projector off, screen up
        return "\n".join(results)


# --- Tests ---
def run_tests():
    print("Running Facade Pattern Home Theater Tests...")

    projector = Projector()
    screen = Screen()
    amplifier = Amplifier()
    dvd_player = DVDPlayer()

    home_theater = HomeTheaterFacade(projector, screen, amplifier, dvd_player)

    # Test watch_movie
    print("\nTesting watch_movie:")
    watch_output = home_theater.watch_movie("Inception")
    expected_watch_output = (
        "Screen DOWN\n" +
        "Projector ON\n" +
        "Projector in widescreen mode\n" +
        "Amplifier ON\n" +
        "Amplifier input set to DVD\n" +
        "Amplifier volume set to 10\n" +
        "DVD Player ON\n" +
        "Playing movie: Inception"
    )
    assert watch_output == expected_watch_output, f"watch_movie failed.\nExpected:\n{expected_watch_output}\nGot:\n{watch_output}"
    print("watch_movie test passed.")

    # Test end_movie
    print("\nTesting end_movie:")
    end_output = home_theater.end_movie()
    expected_end_output = (
        "DVD Player OFF\n" +
        "Amplifier OFF\n" +
        "Projector OFF\n" +
        "Screen UP"
    )
    assert end_output == expected_end_output, f"end_movie failed.\nExpected:\n{expected_end_output}\nGot:\n{end_output}"
    print("end_movie test passed.")

    print("All Facade Pattern Home Theater Tests Passed!")

if __name__ == "__main__":
    run_tests()

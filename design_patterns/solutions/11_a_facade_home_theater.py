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
        results.append(self.screen.down())
        results.append(self.projector.on())
        results.append(self.projector.wide_screen_mode())
        results.append(self.amplifier.on())
        results.append(self.amplifier.set_dvd())
        results.append(self.amplifier.set_volume(10))
        results.append(self.dvd_player.on())
        results.append(self.dvd_player.play(movie))
        return "\n".join(results)

    def end_movie(self):
        results = []
        results.append(self.dvd_player.off())
        results.append(self.amplifier.off())
        results.append(self.projector.off())
        results.append(self.screen.up())
        return "\n".join(results)

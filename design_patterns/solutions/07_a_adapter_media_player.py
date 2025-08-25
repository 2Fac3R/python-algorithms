
from abc import ABC, abstractmethod

"""
Solution for: Media Player Adapter
"""

# Target Interface
class MediaPlayer(ABC):
    @abstractmethod
    def play(self, filename: str):
        pass

# Adaptee 1: Incompatible WAV Player
class WAVPlayer:
    def play_wav(self, file_path: str):
        return f"Playing WAV file: {file_path}"

# Adaptee 2: Incompatible OGG Player
class OGGPlayer:
    def play_ogg_file(self, path: str):
        return f"Playing OGG file: {path}"

# Adapter for WAVPlayer
class WAVPlayerAdapter(MediaPlayer):
    def __init__(self, wav_player: WAVPlayer):
        self._wav_player = wav_player

    def play(self, filename: str):
        return self._wav_player.play_wav(filename)

# Adapter for OGGPlayer
class OGGPlayerAdapter(MediaPlayer):
    def __init__(self, ogg_player: OGGPlayer):
        self._ogg_player = ogg_player

    def play(self, filename: str):
        return self._ogg_player.play_ogg_file(filename)

# Client Code
def client_code(player: MediaPlayer, file: str):
    print(player.play(file))

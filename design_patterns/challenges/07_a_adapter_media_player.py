from abc import ABC, abstractmethod

"""
Challenge: Media Player Adapter

Design a media player system that can play different audio formats (MP3, WAV, OGG).
Initially, your `MediaPlayer` interface only supports a generic `play` method.

You need to integrate existing, incompatible audio players for WAV and OGG formats.

Your task is to:
1.  Define the `MediaPlayer` abstract class (Target interface) with an abstract `play(filename: str)` method.
2.  Define two incompatible audio players (Adaptees):
    -   `WAVPlayer`: Has a method `play_wav(file_path: str)`.
    -   `OGGPlayer`: Has a method `play_ogg_file(path: str)`.
3.  Create `WAVPlayerAdapter` and `OGGPlayerAdapter` classes that implement the `MediaPlayer` interface
    and adapt the respective incompatible players.
4.  Implement a `client_code` function that takes a `MediaPlayer` object and a filename, and calls its `play` method.

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
        # TODO: Implement the adaptation logic
        pass

# Adapter for OGGPlayer
class OGGPlayerAdapter(MediaPlayer):
    def __init__(self, ogg_player: OGGPlayer):
        self._ogg_player = ogg_player

    def play(self, filename: str):
        # TODO: Implement the adaptation logic
        pass

# Client Code
def client_code(player: MediaPlayer, file: str):
    # TODO: Call the play method of the MediaPlayer
    pass


# --- Tests ---
def run_tests():
    print("Running Adapter Pattern Media Player Tests...")

    # Test WAVPlayerAdapter
    wav_player = WAVPlayer()
    wav_adapter = WAVPlayerAdapter(wav_player)
    result_wav = wav_adapter.play("song.wav")
    expected_wav = "Playing WAV file: song.wav"
    assert result_wav == expected_wav, f"WAV Adapter Test Failed: Expected '{expected_wav}', Got '{result_wav}'"
    print("WAVPlayerAdapter test passed.")

    # Test OGGPlayerAdapter
    ogg_player = OGGPlayer()
    ogg_adapter = OGGPlayerAdapter(ogg_player)
    result_ogg = ogg_adapter.play("music.ogg")
    expected_ogg = "Playing OGG file: music.ogg"
    assert result_ogg == expected_ogg, f"OGG Adapter Test Failed: Expected '{expected_ogg}', Got '{result_ogg}'"
    print("OGGPlayerAdapter test passed.")

    # Test client_code with adapters
    print("\nTesting client_code with adapters:")
    try:
        client_code(wav_adapter, "another_song.wav")
        client_code(ogg_adapter, "another_music.ogg")
        print("client_code with adapters test passed.")
    except Exception as e:
        print(f"client_code with adapters test failed: {e}")

    print("All Adapter Pattern Media Player Tests Passed!")

if __name__ == "__main__":
    run_tests()

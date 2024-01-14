# Voice Recorder

It is an application that is used to record sound and save it in a specific file format, which can be listened to and transferred to another device.

-----

## Installation

```python
pip install sounddevice
```
Firstly import the `sounddevice` library through the terminal that will help to record a voice message.
```python
pip install SciPy
```
The sounddevice library will help you to record your voice, but to save your voice in a specific file format. We will use `SciPy` library for that.

-----

## Code Break:

```python
import sounddevice
```

This line imports the `sounddevice` module, which is used for audio input and output operations.

```python
from scipy.io.wavfile import write
```

This line imports the `write` function from the `wavfile` module of the `scipy.io` library. This function is used to write audio data to a WAV file.

```python
def voice_recorder(seconds, file):
```

Defines a function named `voice_recorder` that takes two parameters: `seconds` (the duration of the recording in seconds) and `file` (the name of the WAV file to be saved).

```python
    print("Recording Started…")
```

Prints a message indicating that the recording has started.

```python
    recording = sounddevice.rec((seconds * 44100), samplerate=44100, channels=2)
```

Uses the `sounddevice.rec` function to record audio. It specifies the number of samples to record based on the duration (`seconds * 44100`), sets the sampling rate to 44100 Hz, and uses 2 channels (stereo).

```python
    sounddevice.wait()
```

Waits for the recording to complete before proceeding to the next steps.

```python
    write(file, 44100, recording)
```

Uses the `write` function to save the recorded audio data (`recording`) to a WAV file named by the `file` parameter. The sampling rate is set to 44100 Hz.

```python
    print("Recording Finished")
```

Prints a message indicating that the recording has finished.

```python
voice_recorder(10, "recording.wav")
```

Calls the `voice_recorder` function with a recording duration of 10 seconds and specifies the output file name as "recording.wav". This line initiates the recording process.

-----
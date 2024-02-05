# Extract Text From Videos

Speech recognition is an interesting task that allows you to recognize the text behind the audio. With the use of voice recognition, we can also extract text from a video.

------

## Installation

```
pip install SpeechRecognition moviepy
```
Firstly import the `moviepy` library through the terminal that will help in the program.

-----

## Code Break:

```python
import speech_recognition as sr
```
This line imports the `speech_recognition` library and assigns it the alias `sr`.

```python
import moviepy.editor as mp
```
This line imports the `moviepy.editor` module from the `moviepy` library and assigns it the alias `mp`.

```python
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
```
This line imports the `ffmpeg_extract_subclip` function from the `moviepy.video.io.ffmpeg_tools` module. This function is used to extract a subclip from a video file.

```python
num_seconds_video = 52 * 60
print("The video is {} seconds".format(num_seconds_video))
```
These lines set the variable `num_seconds_video` to the total duration of the video in seconds (52 minutes * 60 seconds) and then print the duration.

```python
l = list(range(0, num_seconds_video + 1, 60))
```
This line generates a list `l` containing values in the range from 0 to `num_seconds_video` (inclusive), with a step of 60 seconds. It essentially creates a list of time points at every minute in the video.

```python
diz = {}
```
This line initializes an empty dictionary `diz` to store the recognized speech for each chunk of the video.

```python
for i in range(len(l) - 1):
```
This line initiates a loop to iterate over the range of indices in the list `l` (excluding the last element).

```python
    ffmpeg_extract_subclip(
        "videorl.mp4",
        l[i] - 2 * (l[i] != 0),
        l[i + 1],
        targetname="chunks/cut{}.mp4".format(i + 1),
    )
```
This line uses `ffmpeg_extract_subclip` to extract a subclip from the video file "videorl.mp4" starting from `l[i] - 2` seconds (if `l[i]` is not 0) to `l[i + 1]`. The extracted subclip is saved with the name "chunks/cut{i + 1}.mp4".

```python
    clip = mp.VideoFileClip(r"chunks/cut{}.mp4".format(i + 1))
    clip.audio.write_audiofile(r"converted/converted{}.wav".format(i + 1))
```
These lines load the extracted video subclip, convert it to audio, and save the audio as a WAV file. This is done using the `VideoFileClip` class from `moviepy`.

```python
    r = sr.Recognizer()
    audio = sr.AudioFile("converted/converted{}.wav".format(i + 1))
```
This code creates a `Recognizer` object from the `speech_recognition` library and an `AudioFile` object pointing to the converted WAV file.

```python
    with audio as source:
        r.adjust_for_ambient_noise(source)
        audio_file = r.record(source)
```
This block uses the `Recognizer` to adjust for ambient noise in the audio source and then records the audio from the source.

```python
    result = r.recognize_google(audio_file)
    diz["chunk{}".format(i + 1)] = result
```
This line recognizes the speech in the recorded audio using Google's Speech Recognition API and stores the result in the dictionary `diz` with the key "chunk{i + 1}".

Overall, this code extracts chunks of video, converts them to audio, performs speech recognition on each chunk, and stores the results in a dictionary.

-----
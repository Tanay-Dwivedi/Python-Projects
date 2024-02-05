# Video to Audio Converter

Converting Video to audio files is a smart tool to extract audio from video files.

-----

## Installation

```
pip install pytube
```
Firstly import the `pytube` library through the terminal that will help in the program.

-----

## Code Break:

This script uses the `pytube` library to download audio from a YouTube video and then converts it to an MP3 file. Let's break down the code:

```python
from pytube import YouTube
import os
```
These lines import the necessary modules, including `pytube` for working with YouTube videos and `os` for interacting with the operating system.

```python
video_url = input("Enter YouTube video URL: ")
```
This line prompts the user to enter a YouTube video URL, and the input is stored in the variable `video_url`.

```python
if os.name == "nt":
    path = os.getcwd() + "\\"
else:
    path = os.getcwd() + "/"
```
These lines check the operating system. If it's Windows (`nt`), the `path` variable is set to the current working directory with a backslash. Otherwise, on Unix-like systems, it uses a forward slash.

```python
yt = YouTube(video_url)
```
This line creates a `YouTube` object using the provided video URL.

```python
video_stream = yt.streams.filter(only_audio=True).first()
```
This line filters the available video streams to select only the audio stream (`only_audio=True`). Then, it selects the first stream.

```python
name = video_stream.title
```
This line retrieves the title of the video stream and stores it in the variable `name`.

```python
video_stream.download(output_path=path, filename=name)
```
This line downloads the audio stream, saving it with the original video title as the filename.

```python
location = os.path.join(path, name + ".mp4")
renametomp3 = os.path.join(path, name + ".mp3")
```
These lines create paths for the original video location (`location`) and the desired MP3 file location (`renametomp3`).

```python
if os.name == "nt":
    os.system('ren "{0}" "{1}"'.format(location, renametomp3))
else:
    os.system('mv "{0}" "{1}"'.format(location, renametomp3))
```
These lines use the `os.system` function to execute a system command. On Windows, it uses `ren` to rename the file, and on Unix-like systems, it uses `mv`. The command renames the downloaded audio file from `.mp4` to `.mp3`.

Note: The script assumes that the operating system is either Windows or a Unix-like system, and it might not work as expected on other operating systems. Also, keep in mind that downloading and distributing copyrighted content without permission may violate YouTube's terms of service and copyright laws.

-----
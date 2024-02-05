from pytube import YouTube
import os

video_url = input("Enter YouTube video URL: ")

if os.name == "nt":
    path = os.getcwd() + "\\"
else:
    path = os.getcwd() + "/"

yt = YouTube(video_url)
video_stream = yt.streams.filter(only_audio=True).first()
name = video_stream.title

video_stream.download(output_path=path, filename=name)
location = os.path.join(path, name + ".mp4")
renametomp3 = os.path.join(path, name + ".mp3")

if os.name == "nt":
    os.system('ren "{0}" "{1}"'.format(location, renametomp3))
else:
    os.system('mv "{0}" "{1}"'.format(location, renametomp3))

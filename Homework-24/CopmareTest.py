from threading import Thread
from time import time
from moviepy import editor

# My Test Results:
# Normal Converting: 95.62467241287231 secs
# Convert with thread: 48.74849724769592 secs


vids = [["vids\BERLIN-2023-Trailer.mp4", "audios\Berlin.mp3"],
        ["vids\Marvel-Studios-Ant-Man-and-The-Wasp-Quantumania-Trailer.mp4", "audios\Ant-man.mp3"],
        ["vids\PoosteShir-2-Trailer.mp4", "audios\Lion-Skin.mp3"],
        ["vids\PUSS-IN-BOOTS-THE-LAST-WISH-Trailer.mp4", "audios\Puss-in-Boots.mp3"],
        ["vids\The-Super-Mario-Bros-Movie-Trailer.mp4", "audios\Super-Mario-Bros.mp3"]]

def mp4TOmp3(vid, name):
    video = editor.VideoFileClip(vid)
    video.audio.write_audiofile(name)


def convert_normal():
    for vid, name in vids:
        mp4TOmp3(vid, name)


def threading_convert():
    threads = []

    for vid, name in vids:
        threads.append(Thread(target=mp4TOmp3, args=(vid, name)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

user = input("convert_normal OR threading_convert?? : ")

if user == "convert_normal":
    start_time = time()
    convert_normal()
    end_time = time()
    print("Time : ", end_time-start_time)

elif user == "threading_convert":
        start_time = time()
        threading_convert()
        end_time = time()
        print("Time : ", end_time-start_time)
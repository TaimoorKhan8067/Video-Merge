from random import randrange

from moviepy.editor import VideoFileClip, concatenate_videoclips, os
import pathlib
initial_count = 0
for path in pathlib.Path("./videos").iterdir():
    if path.is_file():
        initial_count += 1
count = 1
directory = os.path.dirname("./FinalVideos")
if not os.path.exists(directory):
    os.makedirs(directory)
finalCount = 1
rand = 0
while count <= initial_count:
    rand = randrange(0, initial_count)
    print(rand)
    filename1 = "videos/(%s).mp4" % rand
    count += 1
    rand = randrange(0, initial_count)
    print(rand)
    filename2 = "videos/(%s).mp4" % rand
    video_1 = VideoFileClip(filename1)
    video_2 = VideoFileClip(filename2)
    final_video = concatenate_videoclips([video_1, video_2])
    final_video.write_videofile(f"FinalVideos/final_video{finalCount}.mp4")
    finalCount += 1
    count += 1

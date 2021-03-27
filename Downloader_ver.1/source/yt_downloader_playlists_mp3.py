
#Import pytube und re
import pytube
import re
from pytube import YouTube
from pytube import Playlist

#Variabeln
YOUTUBE_STREAM_AUDIO = "140"


#Anfang
print("Give URL")
playlist = Playlist(input("here: "))
print("                         ")
print("Give full path of where you want your Download")
Path = input("here: ")
print("                         ")

# this fixes the empty playlist.videos list
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print(len(playlist.video_urls))


for url in playlist.video_urls:
    print(url)

#Download an sich
for video in playlist.videos:
    audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
    audioStream.download(output_path=Path)



#Ende
print("                         ")
input("Did everything worked correctly? ")
print("                         ")
print("Thank you for the feedback")
print("                         ")
print("thanks for using this Downloader :-)")

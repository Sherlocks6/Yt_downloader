import pytube
from pytube import YouTube
from pytube import Playlist

#Gib mir die Url und Den Video_Namen
print("Give URL")
youtube_video_url = input("here: ")
print("                         ")
print("Give full path of where you want your Download")
Path = input("here: ")
print("                         ")

#Download an sich
try:
    playlist = Playlist(youtube_video_url)
 
    playlist.download_all(download_path= Path)
 
except Exception as e:
    print(e)


#Ende
print("                         ")
input("Did everything worked correctly? ")
print("                         ")
print("Thank you for the feedback")
print("                         ")
print("thanks for using this Downloader :-)")

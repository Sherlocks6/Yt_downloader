import pytube
from pytube import YouTube

#Gib mir die Url und Den Video_Namen
print("Give URL")
youtube_video_url = input("here: ")
print("                         ")
print("Give Video_Name")
Name = input("here: ")
print("                         ")
print("Give full path of where you want your Download")
Full_name = input("here: ")
print("                         ")

#Download an sich
try:
    yt_obj = YouTube(youtube_video_url)
 
    yt_obj.streams.get_audio_only().download(output_path= Full_name, filename= Name)
    print('YouTube video audio downloaded successfully')
except Exception as e:
    print(e)



#Ende
print("                         ")
input("Did everything worked correctly? ")
print("                         ")
print("Thank you for the feedback")
print("                         ")
print("thanks for using this Downloader :-)")

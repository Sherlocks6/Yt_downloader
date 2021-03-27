#Converter
import  os
from  os import system
import time
from os import remove



#User Input
print("Please change the file name to 'Joa' before converting")
print("If you want to convert mp4 to mp3 write 'mp4_to_mp3': ")
print("If you want to convert mp3 to mp4 write 'mp3_to_mp4': ")
print("If you want to convert mp4 to wav write 'mp4_to_wav': ")
print("If you want to convert mp4 to mov write 'mp4_to_mov': ")
first = input(": ")


#IF statments

if first == "mp4_to_mp3":
    os.system('cmd /k "ffmpeg -i joa.mp4 joa.mp3"')
    os.remove("joa.mp4")
elif first == "mp3_to_mp4":
    os.system('cmd /k "ffmpeg -i joa.mp3 joa.mp4"')
    os.remove("joa.mp3")
elif first == 'mp4_to_wav':
    os.system('cmd /k "ffmpeg -i joa.mp4 joa.wav"')
    os.remove("joa.mp4")
else:
    os.system('cmd /k "ffmpeg -i joa.mp4 -f joa.mov')
    os.remove("joa.mp4")








color 9
cls
echo off
cls

echo Write "mp3" to download audio
echo Write "playlist_mp3" to download a playlist as audio
echo Write "playlist_mp4" to download a playlist as video

SET /P _inputname= "otherwise write "mp4" to download video: "
IF "%_inputname%"== "mp3" ( 
   GOTO :MP3
) 
IF "%_inputname%"== "mp4" (
   GOTO :MP4)


IF "%_inputname%"== "playlist_mp3" (
   GOTO :MP4)


else (
   GOTO :playlist_mp4
)   

:MP4
title yt_mp4
cls
cd source
cls
start example_mp4.txt
cls
python yt_downloader_mp4.py
cls
GOTO :finish






:MP3
title yt_mp3
cls
cd source
cls
start example_mp3.txt
cls
python yt_downloader_mp3.py
cls
Goto :finish



:playlist_mp3
title yt_downloader_playlists_mp3
cls
cd source
cls
start example_playlists_mp3.txt
cls
python yt_downloader_playlists_mp3.py
cls
Goto :finish



:playlist_mp4
title yt_downloader_playlists_mp4
cls
cd source
cls
start example_playlists_mp4.txt
cls
python yt_downloader_playlists_mp4.py
cls
Goto :finish




:finish

taskkill /IM notepad.exe /f

timeout 2
cls

echo Thank you for using this Downloader :-)

timeout 5
cls



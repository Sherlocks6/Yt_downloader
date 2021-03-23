color 9
cls
echo off
cls
title yt_mp3
cls


cd source
start example_mp3
cls



python yt_downloader_mp3.py
cls

taskkill /IM notepad.exe /f

timeout 2
cls

echo Thank you for using this Downloader :-)

timeout 5
cls



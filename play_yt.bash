#!/bin/bash

argumentos=$*
echo $argumentos
url=`python3.9 url_youtube.py $argumentos`
echo $url
echo "`date`,$argumentos,$url" >> history_play_yt.txt 
# mpv $url --no-video
# mpv $url

if [ $1 = --video ]; then
	mpv $url
else
	mpv $url --no-video
fi

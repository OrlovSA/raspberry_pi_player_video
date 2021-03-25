#!/usr/bin/env python3

from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep
import os
from moviepy.editor import VideoFileClip
import logging

logging.basicConfig(level=logging.INFO)
player_log = logging.getLogger("Player 1")

usb = "../snt/usb/"
valid_format = ['avi', 'mov', 'mkv', 'mp4']
files_valid = []
viewed = 0

# Проверяем есть ли каталог(флешка)
if os.path.exists(usb):
    # Проверяем есть ли файлы
    files_usb = os.listdir(usb)
    # Проверяем формат и опредиляем продолжительность
    for i in files_usb:
        x = []
        if i.split('.')[-1] in valid_format:
            x.append(usb + i)
            clip = VideoFileClip(x[0])
            x.append(clip.duration)
            clip.close()
            files_valid.append(x)
else:
    print ('Объект не найден')

while True:
    if files_valid[viewed][0]:
        player = OMXPlayer(files_valid, args=['--no-osd', '--no-keys'])
        # dbus_name='org.mpris.MediaPlayer2.omxplayer1'
        # player.playEvent += lambda _: player_log.info("Play")
        # player.pauseEvent += lambda _: player_log.info("Pause")
        # player.stopEvent += lambda _: player_log.info("Stop")
        # VIDEO_PATH = Path(files, )
        # player = OMXPlayer(VIDEO_PATH)
        # sleep(10)
        # player.quit()

        # Ждем пока закончится вмдео
        sleep(files_valid[viewed][1])
        viewed +=1
    else:
        print("Видеофайлов нет")
        break
        
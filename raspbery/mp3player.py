#!/usr/bin/env python
#-*- cording: utf-8 -*-
import sys
import pygame.mixer
import time
import glob
args = sys.argv
# mixerモジュールの初期化
pygame.mixer.init()

if len(args) > 1:
    argument = args[1] + ".mp3"
    print(argument)
    # 音楽ファイルの読み込み
    pygame.mixer.music.load(argument)
else:
    musics = glob.glob("*.mp3")
    for music in musics:
        print(music)
        pygame.mixer.music.load(music)
        # 音楽再生、および再生回数の設定(-1はループ再生)
        pygame.mixer.music.play(1)
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        # 再生の終了
        pygame.mixer.music.stop()

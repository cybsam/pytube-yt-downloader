#########################################################
#! /usr/bin/python3                                     #
# -=- coding: utf-8 -=-                                 #
#                                                       #
# python 3.3.2+ Python Youtube Downloader Script v.1    #
# by cybsam                                             #
# only for legal purpose                                #
# https://github.com/cybsam/pytube-yt-downloader.git    #
#########################################################
from pytube import YouTube
import os
import time
import subprocess

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        print("[ Downloading...              ] ")
        print("[                             ] 0% ")
        time.sleep(1)
        print("[ =======                     ] 25% ")
        time.sleep(2)
        print("[ =============               ] 50% ")
        time.sleep(2)
        print("[ ====================        ] 70% ")
        youtubeObject.download()
        time.sleep(3)
        print("[ =========================== ] 100% ")
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)
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

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)
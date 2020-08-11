import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from tkinter import *

#creates window and sets size
root = Tk()
root.minsize(300,300)

listOfSongs = []
songNames= []

#
v= StringVar()
songLabel = Label(root, textvariable = v, width=35)
def chooseDirectory():
    directory = askdirectory()
    os.chdir(directory)

    for file in os.listdir(directory):
        if file.endswith(".mp3", ".flac", ".mp4"):
            readir = os.path.realpath(file)

            audio = ID3(readir)

            songNames.append(audio['TUT2'].text[0]
            listOfSongs.append(file)

            pygame.mixer.init()

            pygame.mixer.music.load(listOfSongs[0])


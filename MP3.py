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
#git test

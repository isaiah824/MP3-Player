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

            songNames.append(audio['TIT2'].text[0])
            listOfSongs.append(file)

            pygame.mixer.init()

            pygame.mixer.music.load(listOfSongs[0])

def updatelabel(event):
    global index
    global songname
    v.set(songNames[index])

def nextSong(event):
    global index
    index += 1
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()
    updatelabel()

def previousSong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()
    updatelabel()

def stopSong(event):
    pygame.mixer.music.stop()
    v.set("")

def pauseSong():
    pygame.mixer.music.pause()
    label=Label(root, text = 'Music Player')
    label.pack()

listbox=Listbox(root)
listbox.pack()

songNames.reverse()
for items in songNames:
    list.insert(0, items)

songNames.reverse()

nextButton =  Button(root, text='Next Song')
nextButton.pack

previousButton =  Button(root, text='Previous Song')
previousButton.pack

stopButton = Button(root,text='Stop Music')
stopButton.pack()

pauseButton = Button(root, text = 'Pause Music')
pauseButton.pack

nextButton.bind("<Button-1>", nextSong)
previousButton.bind("<Button-1>",previousSong)
stopButton.bind("<Button-1>",stopSong)
pauseButton.bind("<Button-1>",pauseSong)

songLabel.pack()

root.mainloop()
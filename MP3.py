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
def choosedirectory():
    directory = askdirectory()
    os.chdir(directory)
    for file in os.listdir(directory):
        if file.endswith(".mp3"):
            realdir = os.path.realpath(file)

            audio = ID3(realdir)

            songNames.append(audio['TIT2'].text[0])
            listOfSongs.append(file)

            pygame.mixer.init()

            pygame.mixer.music.load(listOfSongs[0])
choosedirectory()
def updatelabel(event):
    global index
    global songname
    v.set(songNames[index])

def playsong(event):
    global index
    index=0
    pygame.mixer.music.play()
    updatelabel(event)

def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()
    updatelabel(event)

def previoussong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()
    updatelabel(event)

def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")

def pausesong(event):
    pygame.mixer.music.pause()



listbox=Listbox(root)
listbox.pack()

songNames.reverse()
for items in songNames:
    listbox.insert(0, items)

songNames.reverse()

nextButton =  Button(root, text='Next Song')
nextButton.pack()

playButton =  Button(root, text='Play Song')
playButton.pack()

previousButton =  Button(root, text='Previous Song')
previousButton.pack()

stopButton = Button(root,text='Stop Music')
stopButton.pack()

pauseButton = Button(root, text = 'Pause Music')
pauseButton.pack()

nextButton.bind("<Button-1>", nextsong)
playButton.bind("<Button-1>", playsong)
previousButton.bind("<Button-1>",previoussong)
stopButton.bind("<Button-1>",stopsong)
pauseButton.bind("<Button-1>",pausesong)

songLabel.pack()

root.mainloop()
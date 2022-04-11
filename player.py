#!/usr/bin/python
import os
import glob
import mpv
from time import sleep
from gpiozero import Button

# button is attached to GPIO18
button = Button(18)

# get tracks
filelist = glob.glob("/media/sleep_media/*.*")
print(filelist)
playlist_length = len(filelist)
position = 0
button.hold_time = 1
# Main
starting = True
timer = 0


while True:
    button.wait_for_press(300)
    if button.is_pressed and starting:
        button.wait_for_release()
        print(f"starting playing {filelist[position]}")
        player = mpv.MPV()
        player.play(filelist[position])
        player.wait_until_playing()
        starting = False
    elif button.is_pressed and not starting:
        button.wait_for_release()
        print("pausing")
        player.pause = not player.pause
    else:
        print("paused for 5 min, quitting")
        player.quit
        if position >= playlist_length:
            positon = 1
        else:
            position += 1
        starting = True
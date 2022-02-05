from tkinter import *
from styles import *
import os
import random
import sys
# import time

shuffled_music_fullpath =""
def get_music_files():
    files = os.listdir('files')
    return files


def destroyer():
    root.quit()
    root.destroy()
    sys.exit()


def run_music():
    music_files = get_music_files()
    shuffled_music = random.choice(music_files)
    # shuffled_music_fullpath=os.getcwd()+shuffled_music
    shuffled_music_fullpath = os.path.join(os.curdir, 'files', shuffled_music)
    os.startfile(shuffled_music_fullpath)


root = Tk()
root.state("zoomed")
root.configure(bg=blue)
# root.geometry("480x320")
title = Label(root, text="Music Program",
              fg=yellow, bg=blue,
              font=(font_type, 20)
              )
title.pack()
title2 = Label(root, text="Click the button to start playing music",
               fg=yellow, bg=blue,
               font=(font_type, 10)
               )
title2.pack()

exit_button = Button(root, text="Exit",
                     fg=yellow, bg=blue,
                     font=(font_type,15),
                     command=destroyer)
exit_button.place(x=550, y=200)

btn = Button(root, text="Play Music",
             fg=yellow, bg=blue,
             font=(font_type, 15),
             command=run_music
             )
btn.place(x=430, y=200)
root.protocol("WM_DELETE_WINDOW", destroyer)
root.mainloop()
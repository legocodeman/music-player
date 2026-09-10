from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os
from PIL import Image


try:
    from ctypes import windll  # Only exists on Windows.

    myappid = "mar.desktopapp.musicplayer.1"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass



root=Tk()
root.title("Music Player")
root.geometry("340x500+620+190")
#root.configure(bg="#0f1a2b")
root.resizable(False, False)


mixer.init()


def open_folder():
    path= filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
##        print(songs)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)


def play_song():
    music_name=playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4],font=("arial,15"))

frame = Frame(root)
frame.pack()


canvas = Canvas(frame, bg="black", width=900, height=700)
canvas.pack()

#icon
image_icon=PhotoImage(file="assets/musicplayer.png")
root.iconphoto(False,image_icon)

Top=PhotoImage(file="assets/top.png")
#Label(root,image=Top,bg="#0f1a2b").pack()
canvas.create_image(460,80,image=Top)

#logo


#button
play_button=PhotoImage(file="assets/play.png")
Button(root,image=play_button,bg="#0f1a2b",bd=0,command=play_song).place(x=100,y=400)

stop_button=PhotoImage(file="assets/stop.png")
Button(root,image=stop_button,bg="#0f1a2b",bd=0,command=mixer.music.stop).place(x=30,y=500)

resume_button=PhotoImage(file="assets/resume.png")
Button(root,image=resume_button,bg="#0f1a2b",bd=0,command=mixer.music.unpause).place(x=115,y=500)


pause_button=PhotoImage(file="assets/pause.png")
Button(root,image=pause_button,bg="#0f1a2b",bd=0,command=mixer.music.pause).place(x=200,y=500)


#label
music=Label(root,text="",font=("arial",15),fg="white",bg="#000000")
music.place(x=166,y=300,anchor="center")



#music
Menu=PhotoImage(file="assets/menu.png")
#Label(root,image=Menu,bg="#0f1a2b").pack(padx=10,pady=50,side=RIGHT)
canvas.create_image(600, 450,image=Menu)

music_frame= Frame(root,bd=2, relief=RIDGE)
music_frame.place(x=130,y=350,width=560,height=250)


Button(root,text="open folder",width=15,height=2,font=("arial",10,"bold"),fg="white",bg="#21b3de",
       command=open_folder).place(x=112,y=300)

scroll = Scrollbar(music_frame)
playlist=Listbox(music_frame,width=100,font=("arial",10),bg="#333333",fg="grey",selectbackground="lightblue",
                 cursor="hand2",bd=0,yscrollcommand=scroll.set)

scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT,fill=BOTH)





root.mainloop()

'''
window = tk.Tk()
window.title("Hello World")


def handle_button_press(event):
    window.destroy()


button = tk.Button(text="My simple app.")
button.bind("<Button-1>", handle_button_press)
button.pack()

# Start the event loop.
window.mainloop()
'''
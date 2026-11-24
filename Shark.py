import tkinter as tk
from ttkthemes import themed_tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
import os
from mutagen.mp3 import MP3
import time
import pygame
from pygame import mixer  # Import mixer module from pygame for audio playback
import sys


if getattr(sys, 'frozen', False):
    basedir = getattr(sys, '_MEIPASS')
else:
    basedir = os.path.dirname(os.path.abspath(__file__))

os.chdir(basedir)
print("Basedir:", basedir)
print("Image exists:", os.path.exists(os.path.join(basedir, "assets", "shark_record.png")))




try:
    from ctypes import windll  # Only exists on Windows.

    myappid = "mar.musicplayer.shark.1"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

class MediaPlayer:
    def __init__(self, window):

        style = ttk.Style()
        style.theme_use("equilux")

        background = "#313799"
        main_background = "#313799"

        style.configure("TScale", background = background)

        self.root = window

        self.root.configure(bg="#5981D7")

        mixer.init()

        print("Current directory:", os.getcwd())
        print("Image exists here:", os.path.exists('assets/shark_record.png'))  

        self.music_image = Image.open('assets/shark_record.png')
        self.music_image = self.music_image.resize((140,140), Image.LANCZOS)
        self.music_image = ImageTk.PhotoImage(self.music_image)

####################################################################################################################################################################
        self.purple_image = Image.open('assets/purple.png')
        self.purple_image = self.purple_image.resize((250,410), Image.LANCZOS)
        self.purple_image = ImageTk.PhotoImage(self.purple_image)

        self.purple_image1 = Image.open('assets/purple.png')
        self.purple_image1 = self.purple_image1.resize((250,350), Image.LANCZOS)
        self.purple_image1 = ImageTk.PhotoImage(self.purple_image1)

        self.purple_image2 = Image.open('assets/purple.png')
        self.purple_image2 = self.purple_image2.resize((250,50), Image.LANCZOS)
        self.purple_image2 = ImageTk.PhotoImage(self.purple_image2)
####################################################################################################################################################################

        self.repeat_icon = Image.open('assets/repeat.png')
        self.repeat_icon = self.repeat_icon.resize((24,24), Image.LANCZOS)
        self.repeat_icon = ImageTk.PhotoImage(self.repeat_icon)

        self.repeat1_icon = Image.open('assets/repeat1.png')
        self.repeat1_icon = self.repeat1_icon.resize((24,24), Image.LANCZOS)
        self.repeat1_icon = ImageTk.PhotoImage(self.repeat1_icon)

        self.play_icon = Image.open('assets/play.png')
        self.play_icon = self.play_icon.resize((28,32), Image.LANCZOS)
        self.play_icon = ImageTk.PhotoImage(self.play_icon)

        self.pause_icon = Image.open('assets/pause.png')
        self.pause_icon = self.pause_icon.resize((26,26), Image.LANCZOS)
        self.pause_icon = ImageTk.PhotoImage(self.pause_icon)

        self.next_icon = Image.open('assets/fishboneright.png')
        self.next_icon = self.next_icon.resize((33,20), Image.LANCZOS)
        self.next_icon = ImageTk.PhotoImage(self.next_icon)

        self.previous_icon = Image.open('assets/fishboneleft.png')
        self.previous_icon = self.previous_icon.resize((33,20), Image.LANCZOS)
        self.previous_icon = ImageTk.PhotoImage(self.previous_icon)

        self.stop_icon = Image.open('assets/stop.png')
        self.stop_icon = self.stop_icon.resize((20,20), Image.LANCZOS)
        self.stop_icon = ImageTk.PhotoImage(self.stop_icon)

        self.speaker_icon = Image.open('assets/speaker.png')
        self.speaker_icon = self.speaker_icon.resize((30,30), Image.LANCZOS)
        self.speaker_icon = ImageTk.PhotoImage(self.speaker_icon)

        self.mute_icon = Image.open('assets/mute.png')
        self.mute_icon = self.mute_icon.resize((30,30), Image.LANCZOS)
        self.mute_icon = ImageTk.PhotoImage(self.mute_icon)

        self.delete_icon = Image.open('assets/delete.png')
        self.delete_icon = self.delete_icon.resize((30,30), Image.LANCZOS)
        self.delete_icon = ImageTk.PhotoImage(self.delete_icon)

        self.delete_all_icon = Image.open('assets/delete2.png')
        self.delete_all_icon = self.delete_all_icon.resize((30,30), Image.LANCZOS)
        self.delete_all_icon = ImageTk.PhotoImage(self.delete_all_icon)

        self.add_song_icon = Image.open('assets/addsongs.png')
        self.add_song_icon = self.add_song_icon.resize((25,30), Image.LANCZOS)
        self.add_song_icon = ImageTk.PhotoImage(self.add_song_icon)

        self.multiple_song_icon = Image.open('assets/song2.png')
        self.multiple_song_icon = self.multiple_song_icon.resize((30,30), Image.LANCZOS)
        self.multiple_song_icon = ImageTk.PhotoImage(self.multiple_song_icon)

        self.shuffle_icon = Image.open('assets/shuffle.png')
        self.shuffle_icon = self.shuffle_icon.resize((30,45), Image.LANCZOS)
        self.shuffle_icon = ImageTk.PhotoImage(self.shuffle_icon)

        self.auto_play_icon = Image.open('assets/auto_play.png')
        self.auto_play_icon = self.auto_play_icon.resize((30,40), Image.LANCZOS)
        self.auto_play_icon = ImageTk.PhotoImage(self.auto_play_icon)

        self.auto_play_not_icon = Image.open('assets/auto_play_not.png')
        self.auto_play_not_icon = self.auto_play_not_icon.resize((40,40), Image.LANCZOS)
        self.auto_play_not_icon = ImageTk.PhotoImage(self.auto_play_not_icon)

        self.purple_photo = tk.Label(self.root,text="",image=self.purple_image,bd=0, background="#5981D7")
        self.purple_photo.place(x=1,y=1)

        self.purple_photo1 = tk.Label(self.root,text="",image=self.purple_image1,bd=0, background="#5981D7")
        self.purple_photo1.place(x=265,y=2)

        self.purple_photo2 = tk.Label(self.root,text="",image=self.purple_image2,bd=0, background="#5981D7")
        self.purple_photo2.place(x=265,y=350)

        self.song_photo = tk.Label(self.root,text="",image=self.music_image,bd=0, background=main_background)
        self.song_photo.place(x=55,y=45)

        #self.heading = tk.Label(self.root, bg="black",text="Music Player", font="helvetica 40 bold italic", fg="#003F05")
        #self.heading.place(x=0,y=2,relwidth=1)

       # tk.Label(self.root, text="",background=background,height=7,width=120).place(x=5,y=400)

        self.songs_list = tk.Listbox(self.root, width=35, height=18, bg="#99A3A4", fg="blue", relief="groove",
                                     selectbackground="#877BF6")
        self.songs_list.place(x=284, y=28)

        self.time_elapsed_label = tk.Label(self.root,text="00:00", fg="white",background=main_background,
                                           activebackground=main_background,padx=5)
        self.time_elapsed_label.place(x=10,y=290)

        self.music_duration_label = tk.Label(self.root,text="00:00",fg="white",background=main_background,
                                             activebackground=main_background,padx=15)
        self.music_duration_label.place(x=185,y=290)

        self.progress_scale = ttk.Scale(self.root,orient="horizontal",style='TScale',from_=0, length=150, 
                                        command=self.progress_scale_moved,cursor='hand2')
        self.progress_scale.place(x=50,y=287)

####################################################################################################################################################################
        #BUTTONS
        self.add_song_button = tk.Button(self.root,image=self.add_song_icon,command=self.add_songs,cursor='hand2',bd=0,
                                     background=main_background, activebackground=main_background)
        self.add_song_button.place(x=11,y=20)

        self.delete_button = tk.Button(self.root,image=self.delete_icon,command=lambda: self.delete_song('selected'),cursor='hand2',bd=0,
                                     background=main_background, activebackground=main_background)
        self.delete_button.place(x=460,y=360)

        self.play_button = tk.Button(self.root,image=self.play_icon,command=self.check_play_pause,cursor='hand2',bd=0,
                                     background=main_background, activebackground=main_background)
        self.play_button.place(x=113,y=331)

        self.next_button = tk.Button(self.root,image=self.next_icon,command=self.next_song,cursor='hand2',bd=0,
                                     background=main_background, activebackground=main_background)
        self.next_button.place(x=162,y=337)

        self.previous_button = tk.Button(self.root,image=self.previous_icon,command=self.previous_song,cursor='hand2',bd=0,
                                     background=main_background, activebackground=main_background)
        self.previous_button.place(x=57,y=337)

        #self.stop_button = tk.Button(self.root,image=self.stop_icon,command=self.stop_song,cursor='hand2',bd=0,
                                     #background=background, activebackground=background)
        #self.stop_button.place(x=236,y=400)

        self.shuffle_button = tk.Button(self.root,image=self.shuffle_icon,command=self.shuffle_songs,cursor='hand2',bd=0,
                                     background=main_background, activebackground=main_background)
        self.shuffle_button.place(x=10,y=327)

        self.speaker_button = tk.Button(self.root,image=self.speaker_icon,command=self.speaker_song,cursor='hand2',bd=0,
                                     background=background, activebackground=background)
        self.speaker_button.place(x=290,y=360)

        self.repeat_button = tk.Button(self.root,image=self.repeat_icon,command=self.repeat_song,cursor='hand2',bd=0,
                                     background=main_background, activebackground=main_background)
        self.repeat_button.place(x=210,y=334)

        #self.auto_play_button = tk.Button(self.root,image=self.auto_play_icon,command=self.auto_play_song,cursor='hand2',bd=0,
                                     #background="#313799", activebackground="#313799")
        #self.auto_play_button.place(x=450,y=350)

        #self.mute_button= tk.Button(self.root,image=self.auto_play_icon,command=self.auto_play_song,cursor='hand2',bd=0,
                                     #background="#313799", activebackground="#313799")
        #self.mute_button.place(x=450,y=350)

        self.vol_scale = ttk.Scale(self.root, from_=0, to=100, orient="horizontal",command=self.set_volume,cursor="hand2")
        self.vol_scale.set(50)  # Set initial volume to 50%
        self.vol_scale.pack(pady=5)
        self.vol_scale.place(x=330,y=365)

       # self.status = tk.Label(self.root, text="Playing : ---------- Song 0 of 0",fg="white",anchor="w",background= "grey",
                              # font="lucida 9 bold",bd=5,relief="ridge")
        self.status = tk.Label(self.root, text="-----------------",fg="white",background=main_background, anchor='center',
                               font="lucida 13 bold",bd=5)      
        #wraplength=190, anchor='center', 

        self.status.place(x=40,y=220)
################################################################################################################################################
        self.menu = tk.Menu(self.root)
        self.root.configure(menu=self.menu)

        #m1 = tk.Menu(self.menu,background="grey",tearoff=False,bd=0,activebackground="black")
        #self.menu.add_cascade(label="Actions",menu=m1)

        #m1.add_command(label="Add Song", command=self.add_songs,image=self.add_song_icon,compound="left")

        #m2 = tk.Menu(self.menu,background="grey",tearoff=False,bd=0,activebackground="black")
        #self.menu.add_cascade(label="Delete",menu=m2)

        #m2.add_command(label="Delete Selected", command=lambda: self.delete_song('selected'),image=self.delete_icon,compound="left")
        #m2.add_command(label="Delete All", command=lambda: self.delete_song('all'), image=self.delete_all_icon, compound="left")
##################################################################################################################################################
        self.directory_list = []
        self.pause=False
        self.repeat_condition=False

        self.autoplay = True
        self.speaker = True

        self.songs_to_play=[]

###############################################################################################################################################################
   
    def add_songs(self):
        songs = filedialog.askopenfilenames(title="Select Music Folder", filetypes=(('mp3 files', '*.mp3'),))
        for song in songs:
            song_name = os.path.basename(song)
            directory_path = song.replace(song_name,"")
            self.directory_list.append({'path':directory_path,'song':song_name})
            self.songs_list.insert('end',song_name)
            #c:/new_folder/song.mp3

        self.songs_list.select_set('0')

    def check_play_pause(self):
        if self.songs_list.size() >= 1:
            self.songs_to_play.append(self.songs_list.get('active'))

            length=len(self.songs_to_play)

            if len(self.songs_to_play)==1:
                self.play_song()


            elif self.songs_to_play[length-1]!=self.songs_to_play[length-2]:
                self.root.after_cancel(self.updater)
                self.play_song()

            else:
                self.pause_unpause()

    def pause_unpause(self):
        if not self.pause:
            self.root.after_cancel(self.updater)
            self.play_button.config(image=self.play_icon)
            self.pause=True

            #self.status.config(text=f"Paused : {self.songs_list.get('active')} {self.songs_list.index('active')+1} of {self.songs_list.size()}")
            self.status.config(text=f"{self.songs_list.get('active')}")            
            pygame.mixer.music.pause()
        else:
            self.pause=False
            self.play_button.config(image=self.pause_icon)
            #self.status.config(text=f"Playing : {self.songs_list.get('active')} {self.songs_list.index('active')+1} of {self.songs_list.size()}")
            self.status.config(text=f"{self.songs_list.get('active')}")
            pygame.mixer.music.unpause()
            self.scale_update()


    def play_song(self):
        self.progress_scale['value'] = 0
        self.time_elapsed_label['text'] = "00:00"

        song_name = self.songs_list.get('active')
        #self.status.config(text=f"Playing: {song_name} Song : {self.songs_list.index('active')} of "
                              #f"{self.songs_list.size()}")
        self.status.config(text=f"{song_name}")
        directory_path=None
        for dictio in self.directory_list:
            if dictio['song'] == song_name:
                directory_path = dictio['path']

        song_with_path = f'{directory_path}/{song_name}'
        music_data = MP3(song_with_path)
        self.music_length = int(music_data.info.length)
        self.music_duration_label['text'] = time.strftime('%M:%S', time.gmtime(self.music_length))

        self.progress_scale['to'] = self.music_length
        self.play_button.config(image=self.pause_icon)
        pygame.mixer.music.load(song_with_path)
        pygame.mixer.music.play()
        self.scale_update()

    def stop_song(self):
        if self.songs_list.size() >= 1:
            self.root.after_cancel(self.updater)
            pygame.mixer.music.stop()

            self.progress_scale['value']=0
            self.time_elapsed_label['text']="00:00"
            self.music_duration_label['text']="00:00"
            self.play_button['image']=self.play_icon  



    def progress_scale_moved(self,x):
        self.root.after_cancel(self.updater)

        scale_at = self.progress_scale.get()

        song_name=self.songs_list.get('active')

        directory_path=None

        for dictio in self.directory_list:
            if dictio['song']==song_name:
                directory_path=dictio['path']

        pygame.mixer.music.load(f"{directory_path}/{song_name}")


        pygame.mixer.music.play(0,scale_at)
        self.scale_update()
        

    def scale_update(self):
        if self.progress_scale['value'] < self.music_length:
            self.progress_scale['value'] += 1

            self.time_elapsed_label['text'] = time.strftime('%M:%S', time.gmtime(self.progress_scale.get()))

            self.updater = self.root.after(1000, self.scale_update)

        elif self.repeat_condition:
            self.play_song()

        elif self.autoplay:
            self.next_song()

        else:
            self.progress_scale['value'] = 0
            self.time_elapsed_label['text'] = "00:00"
            self.play_button.config(image=self.play_icon)
            self.songs_to_play=[]

    def repeat_song(self):
        if self.songs_list.size() >= 1:
            if not self.repeat_condition:
                self.repeat_condition=True
                self.repeat_button.config(image=self.repeat1_icon)
            else:
                self.repeat_condition=False
                self.repeat_button.config(image=self.repeat_icon)

    def auto_play_song(self):
        if self.songs_list.size() >= 1:
            if not self.autoplay:
                self.autoplay=True
                self.auto_play_button.config(image=self.auto_play_icon)
            else:
                self.autoplay=False
                self.auto_play_button.config(image=self.auto_play_not_icon)

    def speaker_song(self):
        if self.songs_list.size() >= 1:
            if not self.speaker:
                self.speaker=True
                self.speaker_button.config(image=self.speaker_icon)
            else:
                self.speaker=False
                self.speaker_button.config(image=self.mute_icon)
                self.vol_scale.set(0)

    def shuffle_songs(self):
        if self.songs_list.size() >= 1:
            song_name=self.songs_list.get('active')

            songs_list=list(self.songs_list.get(0,'end'))
            self.songs_list.delete("0","end")

            import random
            random.shuffle(songs_list)

            for i,song in enumerate(songs_list):
                self.songs_list.insert(i,song)

                if song==song_name:
                    self.songs_list.selection_set(i)
                    self.songs_list.activate(i)

            self.songs_list.update()


    def next_song(self):
        if self.pause ==True:
            self.play_button.config(image=self.pause_icon)
            self.pause=False
        if self.songs_list.size() >= 1:
            self.root.after_cancel(self.updater)
            song_index=self.songs_list.index('active')
            self.songs_list.selection_clear('active')

            list_length=self.songs_list.size()

            if list_length-1 == song_index:
                self.songs_list.selection_set(0)
                self.songs_list.activate(0)   
                self.check_play_pause()
            else:
                self.songs_list.selection_set(song_index+1)
                self.songs_list.activate(song_index+1)
                self.check_play_pause()

    def previous_song(self):
        if self.pause ==True:
            self.play_button.config(image=self.pause_icon)
            self.pause=False
        if self.songs_list.size() >= 1:
            self.root.after_cancel(self.updater)
            song_index=self.songs_list.index('active')
            self.songs_list.selection_clear('active')

            list_length=self.songs_list.size()

            if song_index == 0:
                self.songs_list.selection_set(list_length-1)
                self.songs_list.activate(list_length-1)
                self.check_play_pause()
            else:
                self.songs_list.selection_set(song_index-1)
                self.songs_list.activate(song_index-1)
                self.check_play_pause()

    def delete_song(self, command):
        if self.songs_list.size() >= 1:
            current_song = self.songs_list.index('active')

            if command == 'selected':
                if self.songs_list.size()>1:
                    if current_song == self.songs_list.size()-1:
                        self.songs_list.selection_set(self.songs_list.size()-2)
                        self.songs_list.activate(self.songs_list.size()-2)
                    else:
                        self.songs_list.selection_set(current_song+1)
                        self.songs_list.activate(current_song+1)

                self.songs_list.delete(current_song)
            else:
                self.songs_list.delete(0, self.songs_list.size()-1)


            self.root.after_cancel(self.updater)
            pygame.mixer.music.stop()

            self.progress_scale['value']=0
            self.time_elapsed_label['text']="00:00"
            self.music_duration_label['text']="00:00"
            self.play_button['image']=self.play_icon        

    def set_volume(self, value):
        """Set the volume of the audio playback."""
        volume = float(value) / 100  # Convert slider value to a float between 0 and 1
        mixer.music.set_volume(volume)

        
##########################################################################################################################################

if __name__ == '__main__':

    window = themed_tk.ThemedTk()
    pygame.init()

    window.title("[Shark]")
    window.iconbitmap(os.path.join(basedir, "icon.ico"))
    window.maxsize(width=515,height=410)
    #window.minsize(width=250,height=400)
    window.geometry("250x410+650+220")
    

    x = MediaPlayer(window)
    window.mainloop()

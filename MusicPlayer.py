import tkinter as tk
from ttkthemes import themed_tk
from tkinter import ttk

class MediaPlayer:
    def __init__(self, window):

        style = ttk.Style()
        style.theme_use("breeze")





if __name__ == '__main__':

    window = themed_tk.ThemedTk()


    window.title("Music Player")
    window.maxsize(width=750,height=550)
    window.minsize(width=750,height=550)

    x = MediaPlayer(window)
    window.mainloop()

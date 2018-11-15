from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("Song Maker")
        
        self.add_title()
        self.add_lyric()
        self.add_lyric_entry()
        self.add_lyric_button()
        self.add_lyric_heading()
        self.add_listbox()
        
    def add_title(self):
        self.title = Label()
        self.title.grid(row=0, column=0, columnspan=2)
        self.title.configure(font=("Courier", 18),text="Song Maker")

    def add_lyric(self):
        self.lyric = Label(text="Lyric to add:")
        self.lyric.grid(row=1, column=0, columnspan=2, sticky=W)

    def add_lyric_entry(self):
        self.lyric_entry = Entry()
        self.lyric_entry.grid(row=3, column=0, pady=10, padx=(50,0))

    def add_lyric_button(self):
        self.add_button = Button()
        self.add_button.grid(row=3, column=1, padx=(20,0))
        self.add_button.configure(text="Add")

        self.add_button.bind("<ButtonRelease-1>", self.listbox_add_value)

    def add_lyric_heading(self):
        self.lyrics = Label()
        self.lyrics.grid(row=4, column=0, sticky=W)
        self.lyrics.configure(text="Lyrics:")

    def add_listbox(self):
        self.listbox = Listbox()
        self.listbox.grid(row=5, column=0, columnspan=2)
        self.listbox.configure(height=0, width=0)

    def listbox_add_value(self, event):
        lyric_value = self.lyric_entry.get()
        self.listbox.insert(END, lyric_value) 

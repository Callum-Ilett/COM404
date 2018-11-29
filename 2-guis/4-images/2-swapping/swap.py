from tkinter import *


class Gui(Tk):

    def __init__(self):
        super().__init__()

        self.black_image = PhotoImage(file="black.gif")
        self.stars_image = PhotoImage(file="stars.gif")

        self.image = Label()
        self.image.pack()
        self.image.configure(image=self.black_image)

        self.flip = Button()
        self.flip.pack()
        self.flip.configure(text="Flip", command=self.flip_image)

    def flip_image(self):
        src = self.image.cget('image')

        if src == "pyimage1":
            self.image.configure(image=self.stars_image)

        else:
            self.image.configure(image=self.black_image)

root = Gui()
root.mainloop()
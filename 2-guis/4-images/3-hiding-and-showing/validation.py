from tkinter import *


class Gui(Tk):

    def __init__(self):
        super(Gui, self).__init__()

        self.correct = PhotoImage(file="check.gif")

        self.fields = ['Name:', 'Passport Number:', 'Nights:']
        label = {}
        self.images = {}
        self.entry = {}

        i = 0

        for name in self.fields:
            lb = Label(text=name)
            lb.grid(row=i, column=0)
            label[name] = lb

            e = Entry()
            e.grid(row=i, column=1)
            e.bind("<FocusOut>", self.callback)
            self.entry[name] = e

            valid = Label()
            valid.grid(row=i, column=2)
            self.images[name] = valid

            i += 1

        print(label)

    def callback(self, event):
        for name in self.fields:
            if self.entry[name].get() != "":
                self.images[name].configure(image=self.correct)
            else:
                self.images[name].configure(text="Required")

root = Gui()
root.mainloop()
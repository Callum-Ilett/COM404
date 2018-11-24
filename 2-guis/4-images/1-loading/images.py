from tkinter import *


class Gui(Tk):

    def __init__(self):
        super().__init__()

        self.title_label = Label()
        self.title_label.grid(row=0, columnspan=2, sticky=N+E+S+W)
        self.title_label.configure(text="TRANSPORT")

        self.ambulance_image = PhotoImage(file="ambulance.gif")
        self.bike_image = PhotoImage(file="bike.gif")
        self.plane_image = PhotoImage(fil="plane.gif")

        self.ambulance_label = Label()
        self.ambulance_label.grid(row=1, column=0)

        self.ambulance_label.configure(image=self.ambulance_image)

        self.bike_label = Label()
        self.bike_label.grid(row=1, column=1)

        self.bike_label.configure(image=self.bike_image)

        self.plane_label = Label()
        self.plane_label.grid(row=1, column=2)
        self.plane_label.configure(image=self.plane_image)


root = Gui()
root.mainloop()

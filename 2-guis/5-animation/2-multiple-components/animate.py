from tkinter import *
import time

class AnimatedGui(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("500x500")

        self.red_circle = PhotoImage(file="red.gif")
        self.blue_circle = PhotoImage(file="blue.gif")

        self.add_red()
        self.add_blue()
        
    def add_red(self):
        self.red_label = Label()
        self.red_label.place(x=150, y=0)
        self.red_label.configure(image=self.red_circle)

    def add_blue(self):
        self.blue_label = Label()
        self.blue_label.place(x=250, y=0)
        self.blue_label.configure(image=self.blue_circle)

    def tick(self):

                    
        self.umbrella_x_pos += self.umbrella_x_pos_change
        self.umbrella_y_pos += self.umbrella_y_pos_change
                        
        
        self.umbrella_label.place(x=self.umbrella_x_pos, y=self.umbrella_y_pos)
        
        if(self.umbrella_x_pos >= 440):
            
            self.umbrella_x_pos_change *= -1

        if(self.umbrella_y_pos >= 440):
            self.umbrella_y_pos_change *= -1

        if(self.umbrella_x_pos <= 0):
             self.umbrella_x_pos_change *= -1

        if(self.umbrella_y_pos <= 0):
            self.umbrella_y_pos_change *= -1
            
        self.after(10, self.tick)
        
root = AnimatedGui()
root.mainloop()
        

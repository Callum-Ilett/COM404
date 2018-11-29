from tkinter import *
import time

class AnimatedGui(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("500x500")

        self.umbrella_img = PhotoImage(file="umbrella.gif")

        
        self.umbrella_x_pos = 250
        self.umbrella_y_pos = 0

        self.umbrella_x_pos_change = 1
        self.umbrella_y_pos_change = 1
        
        self.add_image()
        self.tick()

    def add_image(self):

        self.umbrella_label = Label()
        self.umbrella_label.place(x=250, y=0)

        self.umbrella_label.configure(image=self.umbrella_img)

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
        

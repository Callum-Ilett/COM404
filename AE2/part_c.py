from tkinter import *
import time

class Greetings(Tk):
    def __init__(self):
        super().__init__()

        #Load images
        self.helper_image = PhotoImage(file="helpers.gif")
        self.santa = PhotoImage(file="santa.gif")
        self.snowman = PhotoImage(file="snowy.gif")
        self.elf = PhotoImage(file="elf.gif")
        self.reindeer = PhotoImage(file="reindeer.gif")
        self.unknown = PhotoImage(file="unknown.gif")
        
        #Change Window Settings
        self.title("Greetings")
        self.config(bg="#6666fd", padx=15, pady=15)

        #Animation Co-ordinates
        self.helper_x_pos = 250
        self.helper_y_pos = 0

        self.helper_x_pos_change = 1
        self.helper_y_pos_change = 1

        #Add Widgets
        self.add_heading_label()
        
        self.add_helper_image()
        self.add_helper_label()
        self.add_helper_entry()

        self.add_instruction_label()
        
        self.add_message_label()
        self.add_message_entry()

        self.add_changing_image()
        
        self.add_send_button()
        self.add_animate_button()
        self.add_animation_frame()

    def add_heading_label(self):
        self.heading = Label()
        self.heading.grid(row=0, sticky="nesw")

        self.heading.config(bg="#4141ff", text="SEND HELPER" , font="Arial 16", padx=11, pady=11, fg="#fff")

    def add_helper_image(self):
        self.helper = Label()
        self.helper.grid(row=1)

        self.helper.config(image=self.helper_image)

    def add_instruction_label(self):
        self.instruction = Label()
        self.instruction.grid(row=2)
        self.instruction.config(text="Please complete all fields and then click send.", bg="#4141ff", fg="#fff", padx=10, pady=10)

    def add_message_label(self):
        self.message = Label()
        self.message.grid(row=3, sticky="w")

        self.message.config(text="Message:", bg="#4141ff", fg="#fff", padx=10, pady=10)

    def add_message_entry(self):
        self.message_e = Entry()
        self.message_e.grid(row=4, sticky="nesw", padx=10)        

    def add_helper_label(self):
        self.helper = Label()
        self.helper.grid(row=5, column=0, sticky="w")

        self.helper.config(text="Helper:", bg="#4141ff", fg="#fff", padx=10, pady=10)

    def add_helper_entry(self):
        self.helper_e = Entry()
        self.helper_e.grid(row=5, column=1, sticky="w")

        self.helper_e.bind("<KeyRelease>", self.help)

    def add_changing_image(self):
        self.image = Label()
        self.image.grid(row=6, pady=10)
        self.image.config(image=self.unknown)

    def add_send_button(self):
        self.send = Button(command=self.send)
        self.send.grid(row=7, sticky="nesw", pady=2)

        self.send.config(text="Send", padx=12, bg="#ff0")

    def add_animate_button(self):
        self.animate = Button(command=self.animate)
        self.animate.grid(row=8, sticky="nesw")

        self.animate.config(text="Start Animation", bg="#0ff")

    def add_animation_frame(self):
        animation_frame = Frame(self)
        animation_frame.grid(row=9, sticky="ew")

        animation_frame.config(height=200)

    #Button Bind functions

    def send(self):
        message_value = self.message_e.get()
        helper_value = self.helper_e.get()
        message = "Error"
        state = "Error!!"

        helper_array_characters = ["Santa", "Snowman", "Elf", "Reindeer"]
        helper_array_message = ["Santa is on his sleigh", "The Snowman is falling", "The Elf is making its way", "The Reindeer is shining it's nose"]

        if(message_value == ""):
            message = "Please enter a message."

        elif(helper_value == ""):
            message = "Please enter a valid helper."

        else:
            state = "Success!!"

            for i in range(0, len(helper_array_characters)):
                if(helper_value == helper_array_characters[i]):
                    message = helper_array_message[i]
              
        messagebox.showinfo(state, message)

    def help(self, event):
        value = self.helper_e.get()

        if(value=="Santa"):
            self.image.config(image=self.santa)
            
        elif(value=="Snowman"):
            self.image.config(image=self.snowman)

        elif(value=="Elf"):
            self.image.config(image=self.elf)

        elif(value=="Reindeer"):
            self.image.config(image=self.reindeer)

        else:
            self.image.config(image=self.unknown)

    def animate(self):
        animation_frame = Frame(self)
        animation_frame.grid(row=9)

        self.image_helper_animate = Label(animation_frame)
        self.image_helper_animate.config(image=self.unknown)
        
        self.tick()

    #Animation timer

    def tick(self):

        self.helper_x_pos += self.helper_x_pos_change
        self.helper_y_pos += self.helper_y_pos_change
                        
        
        self.image_helper_animate.place(x=self.helper_x_pos, y=self.helper_y_pos)
        
        if(self.helper_x_pos >= 440):
            
            self.helper_x_pos_change *= -1

        if(self.helper_y_pos >= 440):
            self.helper_y_pos_change *= -1

        if(self.helper_x_pos <= 0):
             self.helper_x_pos_change *= -1

        if(self.helper_y_pos <= 0):
            self.helper_y_pos_change *= -1
            
        self.after(10, self.tick)
            
root = Greetings()
root.mainloop()
  

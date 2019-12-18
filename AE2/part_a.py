from tkinter import *

class Greetings(Tk):
    def __init__(self):
        super().__init__()
        self.helper_image = PhotoImage(file="helpers.gif")

        self.title("Greetings")
        self.config(bg="#6666fd", padx=15, pady=15)

        self.add_heading_label()
        self.add_helper_image()
        self.add_helper_label()
        self.add_helper_entry()
        
        self.add_message_label()
        self.add_message_entry()
        
        self.add_instruction_label()
        self.add_send_button()

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

    def add_send_button(self):
        self.send = Button(command=self.send)
        self.send.grid(row=7, sticky="nesw")

        self.send.config(text="Send", padx=12, bg="#ff0")

    def send(self):
        messagebox.showinfo("Sent!!", "Your helper has been sent!")
    
root = Greetings()
root.mainloop()
  

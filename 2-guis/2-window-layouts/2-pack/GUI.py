from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("Newsletter")
        self.configure(height=200, width=400, padx=20, pady=20, bg="blue")
        
        self.add_main_frame()
        self.add_heading_label()
        self.add_instruction_label()    
        self.add_email_frame()
        self.add_email_label()
        self.add_email_entry()
        self.add_subscribe_button()
        

    def add_heading_label(self):
        self.add_heading_label = Label(self.main_frame)
        self.add_heading_label.pack(pady=(0, 25))
        self.add_heading_label.configure(font=("Helvetica", 18),text="RECEIVE OUR NEWSLETTER")

    def add_instruction_label(self):
        self.add_instruction_label = Label(self.main_frame)
        self.add_instruction_label.pack(pady=(0, 25))
        self.add_instruction_label.configure(text="Please enter your email below to receive our newsletter.")

    def add_email_label(self):
        self.add_email_label = Label(self.email_frame)
        self.add_email_label.pack(side=LEFT)
        self.add_email_label.config(text="Email:")

    def add_email_entry(self):
        self.add_email_entry = Entry(self.email_frame)
        self.add_email_entry.pack(side=LEFT,pady=(0,15))

    def add_subscribe_button(self):
        self.add_subscribe_button = Button(self.main_frame)
        self.add_subscribe_button.pack(fill=X)
        self.add_subscribe_button.config(text="Subscribe")
        
    def add_email_frame(self):
        self.email_frame = Frame(self.main_frame)
        self.email_frame.pack()

    def add_main_frame(self):
        self.main_frame = Frame()
        self.main_frame.pack()

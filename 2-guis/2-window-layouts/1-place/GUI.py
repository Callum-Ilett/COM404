from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("Newsletter")
        self.configure(height=200, width=400)

        self.add_heading_label()
        self.add_instruction_label()
        self.add_email_label()
        self.add_email_entry()
        self.add_subscribe_button()

    def add_heading_label(self):
        self.add_heading_label = Label(self)
        self.add_heading_label.place(x=50, y=0)
        self.add_heading_label.configure(font=("Helvetica", 18),text="RECEIVE OUR NEWSLETTER")

    def add_instruction_label(self):
        self.add_instruction_label = Label(self, text="Please enter your email below to receive our newsletter.")
        self.add_instruction_label.place(x=50, y=50)

    def add_email_label(self):
        self.add_email_label = Label(self, text="Email:")
        self.add_email_label.place(x=100, y=100)

    def add_email_entry(self):
        self.add_email_entry = Entry(self)
        self.add_email_entry.place(x=150, y=100)

    def add_subscribe_button(self):
        self.add_subscribe_button = Button(self, text="Subscribe", width=50)
        self.add_subscribe_button.place(x=25,y=150)

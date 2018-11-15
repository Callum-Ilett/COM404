from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("Newsletter")
        self.configure(height=200, width=400, padx=20, pady=20, bg="blue")
        
        self.add_main_frame()
        self.add_heading_label()
        self.add_instruction_label()    
        self.add_email_label()
        self.add_email_entry()
        self.add_subscribe_button()
        

    def add_heading_label(self):
        self.add_heading_label = Label(self.main_frame)
        self.add_heading_label.grid(row=0, column=0, columnspan=2)
        self.add_heading_label.configure(font=("Helvetica", 18),text="RECEIVE OUR NEWSLETTER")

    def add_instruction_label(self):
        self.add_instruction_label = Label(self.main_frame)
        self.add_instruction_label.grid(row=1, column=0, columnspan=2)
        self.add_instruction_label.configure(text="Please enter your email below to receive our newsletter.")

    def add_email_label(self):
        self.add_email_label = Label(self.main_frame)
        self.add_email_label.grid(row=2,column=0, sticky=W)
        self.add_email_label.config(text="Email:")

    def add_email_entry(self):
        self.add_email_entry = Entry(self.main_frame)
        self.add_email_entry.grid(row=2, column=1, sticky=W)

    def add_subscribe_button(self):
        self.add_subscribe_button = Button(self.main_frame, command=self.submit_callback)
        self.add_subscribe_button.grid(row=3, column=0, columnspan=2)
        self.add_subscribe_button.config(text="Subscribe")

    def submit_callback(self):
        email = self.add_email_entry.get()
        
        messagebox.showinfo("Subscribed!", "Your email {} has been added".format(email))
        
    def add_main_frame(self):
        self.main_frame = Frame()
        self.main_frame.grid()


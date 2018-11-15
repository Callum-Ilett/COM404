from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("Passport Checker")

        self.add_title()
        
        #Add components for the face
        self.add_face_label()
        self.add_face_checkbox_yes()
        self.add_face_checkbox_no()

        #Add components for the moths
        self.add_months_label()
        self.add_months_checkbox_yes()
        self.add_months_checkbox_no()

        #Add components for the visa
        self.add_visa_label()
        self.add_visa_checkbox_yes()
        self.add_visa_checkbox_no()

        self.add_check_button()

    def add_title(self):
        self.title = Label()
        self.title.grid(row=0, column=0, sticky=W, pady=(0, 20))
        self.title.configure(font=("Helvetica", 18),text="Passport Checker")

    def add_face_label(self):
        self.face_label = Label()
        self.face_label.grid(row=1, column=0, sticky=W)
        self.face_label.configure(text="1.Photo matches face?")
        
    def add_face_checkbox_yes(self):
        self.face_checkbox_value = IntVar()
        self.face_checkbox = Checkbutton(variable=self.face_checkbox_value)
        self.face_checkbox.grid(row=2, column=0)
        self.face_checkbox.configure(text="Yes")

    def add_face_checkbox_no(self):
        self.face_checkbox = Checkbutton()
        self.face_checkbox.grid(row=2, column=1)
        self.face_checkbox.configure(text="No")

#--------------------------------------------------------------------
    
    def add_months_label(self):
        self.months_label = Label()
        self.months_label.grid(row=3, column=0, pady=10)
        self.months_label.configure(text="2.Passport has at least 6 months validity?")
        
    def add_months_checkbox_yes(self):
        self.months_checkbox_value = IntVar()
        self.months_checkbox = Checkbutton(variable=self.months_checkbox_value)
        self.months_checkbox.grid(row=4, column=0)
        self.months_checkbox.configure(text="Yes")

    def add_months_checkbox_no(self):
        self.months_checkbox = Checkbutton()
        self.months_checkbox.grid(row=4, column=1)
        self.months_checkbox.configure(text="No")
        
#--------------------------------------------------------------------
        
    def add_visa_label(self):
        self.visa_label = Label()
        self.visa_label.grid(row=5, column=0, pady=10)
        self.visa_label.configure(text="2.Passport has at least 6 months validity?")
        
    def add_visa_checkbox_yes(self):
        self.months_checkbox_value = IntVar()
        self.visa_checkbox = Checkbutton(variable=self.months_checkbox_value)
        self.visa_checkbox.grid(row=6, column=0)
        self.visa_checkbox.configure(text="Yes")

    def add_visa_checkbox_no(self):
        self.visa_checkbox = Checkbutton()
        self.visa_checkbox.grid(row=6, column=1)
        self.visa_checkbox.configure(text="No")

#--------------------------------------------------------------------

    def add_check_button(self):
        self.check = Button(command=self.check_clicked)
        self.check.grid(row=7, column=0)

        self.check.configure(text="Check")

    def check_clicked(self):
        self.box1 = self.face_checkbox_value.get()
        self.box2 = self.months_checkbox_value.get()
        self.box3 = self.months_checkbox_value.get()

        if(self.box1 == 1 & self.box2 == 1 & self.box3 == 1):
            messagebox.showinfo("Check Success", "You are eligible for a new passport")
        else:
            messagebox.showinfo("Check Failed", "You are NOT eligible for a new passport")


root = Gui()
root.mainloop()

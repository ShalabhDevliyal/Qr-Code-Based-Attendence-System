from tkinter import *
import os


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        # self.configure(bg='#1E90FF')
        self.bg_image = PhotoImage(file='background.png')
        bg_label = Label(self, image=self.bg_image)
        bg_label.pack(fill=BOTH, expand=1)

        self.pack(fill=BOTH, expand=1)

        exitButton = Button(self, text="Exit", height=2,
                            width=8, command=self.clickExitButton, bg='Red', fg='White', font='Helvetica 12 bold')
        exitButton.place(x=170, y=250)

        generateButton = Button(self, text="Generate QR", height=2,
                                width=10, command=self.generate, font='Helvetica 12 bold')
        generateButton.place(x=20, y=100)

        takeattendanceButton = Button(self, text="Scanner", height=2,
                                      width=10, command=self.attendance, font='Helvetica 12 bold')
        takeattendanceButton.place(x=300, y=100)

    def clickExitButton(self):
        exit()

    def generate(self):
        os.system('generate.py')

    def attendance(self):
        os.system('attendance.py')


root = Tk()
app = Window(root)
root.wm_title("Qr Attendance Interface")
root.geometry("430x350")
root.configure(bg='light blue')
root.mainloop()

from tkinter import *
import winsound, os, sys
class quiz:
    def destiny2(self):
        winsound.PlaySound('REEE.wav', winsound.SND_FILENAME)
    def darksouls(self):
        winsound.PlaySound('PraiseTheSun.wav', winsound.SND_FILENAME)
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        label1 = self.label1 = Label(frame, text='Which of these two games do you prefer?', fg="red")
        self.label1.grid(row=1, column=2)
        self.button1 = Button(frame, text='Destiny 2', fg="blue", command=self.destiny2)
        self.button1.grid(row=2, column=1)
        self.button2 = Button(frame, text='Dark Souls III', fg="red", command=self.darksouls)
        self.button2.grid(row=2, column=3)








root = Tk()
app = quiz(root)
root.mainloop()
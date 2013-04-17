# File: hello2.py

from Tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.grid()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit,height=1,width=1)
        self.button.grid(row=0, column=1)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.grid(row=1, column=1)

    def say_hi(self):
        print "hi there, everyone!"

root = Tk()

app = App(root)

root.mainloop()
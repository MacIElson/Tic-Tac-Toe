# File: hello2.py

from Tkinter import *

class App:

    def __init__(self, master):
		photo = PhotoImage(file="X_mark.gif", height=20, width=20)

		b1 = Button(master, image=photo)
		b1.image = photo
		b2 = Button(master, text="O", height=8, width=10)
		
		b1.grid(row=1, column=1)
		b2.grid(row=1, column=2)
		
		#	imgX= Image.open("x.jpeg")
    #    imgXjov = ImageTk.PhotoImage(bard)
    #    label1 = Label(self, image=imgXjov)
    #    label1.image = imgXjov
    #    label1.grid(column=1, row=0)

    def say_hi(self):
        print "hi there, everyone!"

root = Tk()

app = App(root)

root.mainloop()

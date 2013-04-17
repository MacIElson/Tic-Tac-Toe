from Tkinter import *

class App:

    def __init__(self, master):

        frame=Frame(master)
        Grid.rowconfigure(root,0,weight=1)
        Grid.columnconfigure(root,0,weight=1)
        frame.grid(row=0,column=0,sticky=N+S+E+W)
        grid=Frame(frame)
        grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
        Grid.rowconfigure(frame,7,weight=1)
        Grid.columnconfigure(frame,0,weight=1)

        #example values
        for x in range(10):
            for y in range(5):
                btn = Button(frame)
                btn.grid(column=x, row=y)
        for x in range(10):
          Grid.columnconfigure(frame,x,weight=1)
        for y in range(5):
          Grid.rowconfigure(frame,y,weight=1)

        def say_hi(self):
            print "hi there, everyone!"

root = Tk()

app = App(root)

root.mainloop()
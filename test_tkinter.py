from tkinter import *
#length of the input pane
ilength = 3
iheight = 3
mlength = 9
mheight = 9

class GameUI:

    def __init__(self, master):

        frame = Frame(master)
        inputframe = Frame(frame, bg="white")
        metaframe = Frame(frame, bg="white")
        frame.pack()
        inputframe.pack(side=LEFT)
        metaframe.pack(side=LEFT)

        Grid.rowconfigure(root,0,weight=1)
        Grid.columnconfigure(root,0,weight=1)

        #Generate buttons for the inputframe:
        for x in range(ilength):
        	for y in range(iheight):
        		button = Button(inputframe, bg="white")
        		button.grid(column=x, row=y)

        for x in range(ilength):
        	Grid.columnconfigure(frame,x,weight=1)
        for y in range(iheight):
        	Grid.rowconfigure(frame,y,weight=1)

        #Generate labels for the metaframe:
        n=1
        for i in range(mlength):
        	for j in range(mheight):
        		label = Label(metaframe, bg="white",text=str(n))
        		label.grid(column=j, row=i)
        		n += 1
        for i in range(mlength):
        	Grid.columnconfigure(frame,x,weight=1)
        for j in range(mheight):
        	Grid.rowconfigure(frame,y,weight=1)

    def say_hi(self):
        print("X")

root = Tk()

ui = GameUI(root)

root.mainloop()
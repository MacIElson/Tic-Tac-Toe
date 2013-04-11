#Software Design 2013
#Tic-Tac-Toe group project
#Antonia Elsen, Mac-I, Thomas Nattestad

try:
    from tkinter import *
except ImportError:
    from Tkinter import *

#length of the input pane (3x3 default)
ILENGTH = 3
IHEIGHT = 3
#length of the meta pane (9x9 default)
MLENGTH = 9
MHEIGHT = 9

class GameUI:

    def __init__(self, master):
        frame = Frame(master)                        #Create master frame
        inputframe = Frame(frame, bg="white")        #Frame for the input board (buttons)
        metaframe = Frame(frame, bg="white")         #Frame for the meta board (labels only)
        frame.pack()
        inputframe.pack(side=LEFT)
        metaframe.pack(side=LEFT)
        inputbuttons = []
        metalabels = []

        Grid.rowconfigure(root,0,weight=1)           #I still don't know exactly what this does, but it establishes a grid
        Grid.columnconfigure(root,0,weight=1)

        #Generate buttons for the inputframe:
        b = 1 #buttoncounter
        for x in range(ILENGTH):
        	for y in range(IHEIGHT):
        		button = Button(inputframe, bg="white",command=self.assign_token(b))
        		button.grid(column=x, row=y)
        		inputbuttons.append(button)
        		b+=1

        for x in range(ILENGTH):
        	Grid.columnconfigure(frame,x,weight=1)
        for y in range(IHEIGHT):
        	Grid.rowconfigure(frame,y,weight=1)

        #Generate labels for the metaframe:
        
        n=1 #Counter for frame numbers

        for i in range(MLENGTH):
        	for j in range(MHEIGHT):
        		label = Label(metaframe, bg="white",text=str(n))
        		label.grid(column=j, row=i) #Row and columns are flipped
        		metalabels.append(label)
        		n += 1
        for i in range(MLENGTH):
        	Grid.columnconfigure(frame,x,weight=1)
        for j in range(MHEIGHT):
        	Grid.rowconfigure(frame,y,weight=1)

    def assign_token(self, frame):
    	"""Changes the token of the corresponding metaboard label"""
    	print(str(frame))


root = Tk()

ui = GameUI(root)

root.mainloop()
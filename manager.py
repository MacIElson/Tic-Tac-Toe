#Software Design 2013
#Tic-Tac-Toe group project
#Antonia Elsen, Mac-I, Thomas Nattestad

from tkinter import *
import time, sys

#INITIALIZE CONSTANTS
SLENGTH = 3		#length of a small pane (3x3 default)
SHEIGHT = 3
MLENGTH = 9     #length of the meta pane (9x9 default)
MHEIGHT = 9
PLAYERTOKEN = "X"

mbnum = 0

class GameManager():
	def __init__(self, master):
		frame = Frame(master, width=800, height=600, bg="white")   #Create master frame
		inputframe = Frame(master=frame, bg="white")        #Frame for the input board (buttons)
		metaframe = Frame(master=frame, bg="black")         #Frame for the meta board (labels only)
		frame.pack()
		frame.grid_propagate(False)
		inputframe.grid(row=1,column=1)
		metaframe.grid(row=1,column=2)
		#List of gpanels and buttons for the inputboard and metaboard
		self.inputbuttons = []
		self.miniboards = []                             #The metaboard will contain 9 panels: one for each miniboard
		self.lvars = []
		Grid.rowconfigure(root,0,weight=1)           #I still don't know exactly what this does, but it establishes a grid
		Grid.columnconfigure(root,0,weight=1)

		#Generate buttons for the inputframe:
		b = 0 #buttoncounter
		for x in range(SLENGTH):
			for y in range(SHEIGHT):
				button = gButton(squarenum=b, master=inputframe, bg="white", width=6, height=3)
				button.grid(column=y, row=x, padx=2, pady=2)
				self.inputbuttons.append(button)
				b+=1

		for x in range(SLENGTH):
			Grid.columnconfigure(frame,x,weight=1)
		for y in range(SHEIGHT):
			Grid.rowconfigure(frame,y,weight=1)

		# Generate Boards for the metaframe:
		b = 0 #Counter for board numbers
		
		for i in range(SLENGTH):
			for j in range(SHEIGHT):
				miniboard = BoardFrame(squarenum=b,master=metaframe,bg="DarkGrey",width=3,height=3,padx=2,pady=2)
				#Generate labels for each board
				l = 0
				for il in range(SLENGTH):
					for jl in range(SHEIGHT):
						lvar = StringVar()					#The text of the label is variable and will be updated, hence the StringVar
						lvar.set("b"+str(b)+"s"+str(l))
						label = gLabel(squarenum=l,master=miniboard, bg="white",textvariable=lvar, fg = "LightGrey",width=6, height=3)
						label.grid(column=jl, row=il, padx=1, pady=1) #Row and columns are flipped
						miniboard.addLabel(label)
						miniboard.lvars.append(lvar)
						l += 1
				#Format Miniboard
				miniboard.pack()
				miniboard.grid(column=j, row=i) #Row and columns are flipped
				self.miniboards.append(miniboard)
				b += 1
			
	def playLabel(self,snum):
		"""Changes the token of the corresponding metaboard label"""
		self.miniboards[mbnum].setLabel(snum, PLAYERTOKEN)
		print("DEBUG: changeLabel: mn:"+str(mbnum)+" sn:"+str(snum))
		
class BoardFrame(Frame):
	def __init__(self, squarenum=0, *args, **kwargs):
		Frame.__init__(self, *args, **kwargs)
		#self.num = squarenum
		self.labellist = []                             #List of all of the labels
		self.lvars = []
		
	def addLabel(self, label):
		self.labellist.append(label)
		
	def setLabel(self, labelnum, token):
		"""Changes the token of the space in the board (plays either X or O)."""
		self.lvars[labelnum].set(token)
		print("Label "+str(labelnum)+" changed to "+PLAYERTOKEN)
	
	def checkState(self):
		"""Checks to see if the board is full. Returns true if board is filled, false if there is a spot open."""
		isFull = True
		for label in labellist:
			if label.text == "":                 #If any token in the board is blank, board is not full
				isFull = False
		return isFull

class gButton(Button):
	def __init__(self, squarenum=0, *args, **kwargs):
		"""Extends the tkinter.button class: the gButton takes an int 'squarenum' that determines what square
		the button represents, from 0-8"""
		self.num = squarenum
		Button.__init__(self, command=self.playLabel,*args, **kwargs)
	
	def playLabel(self):
		ui.playLabel(self.num)
		
		
class gLabel(Label):
	def __init__(self, squarenum=0, *args, **kwargs):
		Label.__init__(self, *args, **kwargs)
		self.num = squarenum
		

root = Tk()
ui = GameManager(root)
root.mainloop()
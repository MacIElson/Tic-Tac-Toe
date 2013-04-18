#Software Design 2013
#Tic-Tac-Toe group project
#Antonia Elsen, Mac-I, Thomas Nattestad

###CURRENT STATUS: 
#When the program tries to create "miniboards", the GUI does not show up
#If the miniboard code is commented out, the GUI will show up.

###Comments for Thomas and MacI:--------------------------------------------------------
#I use "###" to denote code I use to debug/test, that will be deleted later
#I created a couple of new classes: gButtons and gLabels that inherit the Buttons and Labels of tkinter
# 	 These new classes can keep track of what miniboard (one of the 9 boards of the metaboard) they are part of
#  	 Because Buttons, Lables, etc. can take a lot of parameters (like bg color, text, master, etc)
#	 I initialized them using *args (arguments) and **kwargs (keyword arguments)
#	 This basically lets us use as many parameters as we want (they are like variables for parameters)
#	 If that didn't make any sense...just look at the gButton and gLabel classes.
#I wrote this code in such a way that the boards can be any size, using the global variables
#	 SLENGTH and SHEIGHT
###-------------------------------------------------------------------------------------
from tkinter import *
import time, sys

#INITIALIZE CONSTANTS
SLENGTH = 3		#length of a small pane (3x3 default)
SHEIGHT = 3
MLENGTH = 9     #length of the meta pane (9x9 default)
MHEIGHT = 9

class GameManager():
	def __init__(self, master):
		frame = Frame(master)                        #Create master frame
		inputframe = Frame(frame, bg="white")        #Frame for the input board (buttons)
		metaframe = Frame(frame, bg="white")         #Frame for the meta board (labels only)
		frame.pack()
		inputframe.pack(side=LEFT)
		metaframe.pack(side=LEFT)
		#List of gpanels and buttons for the inputboard and metaboard
		inputbuttons = []
		metagpanels = []                             #The metaboard will contain 9 panels: one for each miniboard

		Grid.rowconfigure(root,0,weight=1)           #I still don't know exactly what this does, but it establishes a grid
		Grid.columnconfigure(root,0,weight=1)

		#Generate buttons for the inputframe:
		b = 0 #buttoncounter
		for x in range(SLENGTH):
			for y in range(SHEIGHT):
				button = gButton(b,inputframe, bg="white", width=3)
				button.grid(column=x, row=y)
				inputbuttons.append(button)
				b+=1

		for x in range(SLENGTH):
			Grid.columnconfigure(frame,x,weight=1)
		for y in range(SHEIGHT):
			Grid.rowconfigure(frame,y,weight=1)

		# Generate Boards for the metaframe:
		# b=0 #Counter for board numbers
		# for i in range(SLENGTH):
			# for j in range(SHEIGHT):
				# miniboard = BoardFrame(metaframe)
				# miniboard.grid(column=j, row=i) #Row and columns are flipped
				# miniboard.pack(side=LEFT)
				# metagpanels.append(miniboard)
				# b += 1
		# for i in range(SLENGTH):
			# Grid.columnconfigure(frame,x,weight=1)
		# for j in range(MHEIGHT):
			# Grid.rowconfigure(frame,y,weight=1)
		# frame.pack()
		
		###Failsafe to exit program after 5 secs
		# time.sleep(5)###
		# print("Exiting.")###
		# sys.exit(0)###
			

	def assign_token(self, frame):
		"""Changes the token of the corresponding metaboard label"""
		print("assign_token###: "+ str(frame))
		
class BoardFrame(Frame):
	def __init__(self, *args, **kwargs):
		Frame.__init__(self, *args, **kwargs)
		#self.num = squarenum
		self.labellist = []                                              #List of all of the labels
		l = 0                                                            #Label counter
		for i in range(SLENGTH):
			for j in range(SHEIGHT):
				label = gLabel(self, bg="white",text=str(l))
				label.grid(column=j, row=i) #Row and columns are flipped
				self.labellist.append(label)
				l += 1
		
	def setLabel(self, labelnum, token):
		"""Changes the token of the space in the board (plays either X or O)."""
		self.labellist[labelnum].text = token
	
	def checkState(self):
		"""Checks to see if the board is full. Returns true if board is filled, false if there is a spot open."""
		isFull = True
		for label in labellist:
			if label.text == "":                 #If any token in the board is blank, board is not full
				isFull = False
		return isFull

class gButton(Button):
	def __init__(self, squarenum=0, *args, **kwargs):
		Button.__init__(self, *args, **kwargs)
		"""Extends the tkinter.button class: the gButton takes an int 'squarenum' that determines what square
		the button represents, from 0-8"""
		self.num = squarenum
		self.text= str(self.num)
		self.activebackground = "LightBlue"
		
	def getNum(self):
		return self.num
		
class gLabel(Label):
	def __init__(self, squarenum=0, *args, **kwargs):
		Label.__init__(self, *args, **kwargs)
		self.num = squarenum
		

root = Tk()
ui = GameManager(root)
root.mainloop()
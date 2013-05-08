#Software Design 2013
#Tic-Tac-Toe group project
#Antonia Elsen, Mac-I, Thomas Nattestad

from tkinter import *

#INITIALIZE CONSTANTS
SLENGTH = 3		#length of a small pane (3x3 default)
SHEIGHT = 3
MLENGTH = 9     #length of the meta pane (9x9 default)
MHEIGHT = 9
EMPTY = " "
USERTOKEN = "X" #token for the main player (user)
PLAYER1TOKEN = "O"
PLAYER2TOKEN = "[ ]"
tokens = [USERTOKEN, PLAYER1TOKEN]

nextmini = 4		#global variable for the current metaboard (sketch, we know.)
currentmini = 4
prevmini = 4

win_combos =([0, 1, 2],
			 [3, 4, 5], 
			 [6, 7, 8],
			 [0, 3, 6], 
			 [1, 4, 7], 
			 [2, 5, 8],
			 [0, 4, 8],
			 [2, 4, 6]) 

class GameManager():
	def __init__(self, master):
		self.turn = 0
		self.firstplay = True
		self.switchboards = False
		self.win_list = [" " for i in range(9)]									#Create a list of the winners of each board
		self.setupGUI()
	
	def setupGUI(self):
		#Frame Setup
		frame = Frame( width=800, height=600, bg="white")    					#Master Frame
		inputframe = Frame(master=frame, bg="white")        					#Frame for the input board (SLENGTH x SHEIGHT buttons)
		metaframe = Frame(master=frame, bg="black")         					#Frame for the meta board (MLENGTH x MHEIGHT labels)
		
		#Frame formatting voodoo:
		frame.pack()
		frame.grid_propagate(False)												#Constrains the master frame grid
		inputframe.grid(row=1,column=1)											#Formatting the input frame
		metaframe.grid(row=1,column=2)											#Formatting the meta board frame
		#List of gpanels and buttons for the inputboard and metaboard
		self.inputbuttons = []
		self.miniboards = []                         	    					#The metaboard will contain 9 panels: one for each miniboard
		self.lvars = []															#List of the label's string variables (updated when game is played)
		Grid.rowconfigure(root,0,weight=1)           							#I still don't know exactly what this does, but it establishes a grid
		Grid.columnconfigure(root,0,weight=1)									#Some more grid-establishing going on here
		
		#Buttons: ===========================================================
		#Generate buttons for the inputframe:
		b = 0 #button counter
		for x in range(SLENGTH):
			for y in range(SHEIGHT):
				button = gButton(squarenum=b, master=inputframe, bg="white",
								 width=6, height=3)
				button.grid(column=y, row=x, padx=2, pady=2)
				self.inputbuttons.append(button)
				b+=1
		#Format buttons
		for x in range(SLENGTH):
			Grid.columnconfigure(frame,x,weight=1)
		for y in range(SHEIGHT):
			Grid.rowconfigure(frame,y,weight=1)

		#Boards: ============================================================
		# Generate Boards for the metaframe:
		b = 0 #board counter
		for i in range(SLENGTH):												#Creates / places miniboards by column and by row
			for j in range(SHEIGHT):
				miniboard = Board(squarenum=b,master=metaframe,
									   bg="darkgrey",width=3,height=3,padx=2,
									   pady=2)
				#Generate labels for each board
				l = 0
				for il in range(SLENGTH):										#Creates / places labels by column and by row
					for jl in range(SHEIGHT):
						lvar = StringVar()										#The text of the label is variable and will be updated, hence the StringVar
						lvar.set(" ")
						label = gLabel(squarenum=l,master=miniboard, bg=
									   "white",textvariable=lvar,
									   fg = "black",width=6, height=3)
						label.grid(column=jl, row=il, padx=1, pady=1) 			#Row and columns are flipped
						miniboard.addLabel(label)
						miniboard.lvars.append(lvar)
						l += 1
						
				#Format Miniboard
				miniboard.pack()
				miniboard.grid(column=j, row=i) 								#Row and columns are flipped
				self.miniboards.append(miniboard)
				b += 1
	
	def runButtonStates(self):
		"""Checks the content of each label in the current miniboard. 
		   If a label is occupied, disable its corresponding button."""
		
		currentlabellist = self.miniboards[nextmini].labellist
		for l in range(0,len(currentlabellist)): 								#For each label in the current miniboard, from 0 to length
			if(currentlabellist[l].cget("text") != EMPTY): 						
				self.inputbuttons[l].changeState(False)      					#If occupied, disable the input button
			else:
				self.inputbuttons[l].changeState(True)				#If blank, enable the input button

		for i in range(0, 9):
			buttonIsClean = False
			currentlabellist = self.miniboards[i].labellist
			for x in currentlabellist:
				if(x.cget("text") == EMPTY):
					buttonIsClean = True				#If blank, enable the input button
			if(not buttonIsClean):
				self.inputbuttons[i].changeState(False)
	
	def changeMiniBackgrounds(self):
		"""Changes the backgrounds of the miniboards: every miniboard will be white except for the miniboard to be played on next"""
		self.miniboards[prevmini].changeBGs("white")
		self.miniboards[currentmini].changeBGs("lightgrey")
		self.miniboards[nextmini].changeBGs("yellow")
			
	def attemptPlay(self,snum):
		"""Attempts to change the token of the corresponding metaboard label.
			If there is already a token on that space, player must play again.
			Checks to see if the miniboard has been won.
			Move the next player to the next miniboard if applicable."""
		if self.miniboards[nextmini].canMove(snum) == True:
			self.miniboards[nextmini].makeMove(snum, tokens[self.turn])				#Set the label of the button
			
			self.checkSmallBoardVictory()
			self.checkBigBoardVictory()
			
			self.nextBoard(snum)													#Set the miniboard tracker to the next miniboard
			self.runButtonStates()													#Change the states of the input buttons as necessary
			self.changeMiniBackgrounds()
			self.nextturn()
		else:
			pass
			#self.displayText()

	def checkBigBoardVictory(self):
		print(self.win_list)
		#X test
		placedPieces = []
		for i in range(0,9):
			if(self.win_list[i] == 'O'):
				placedPieces += [i]
		if(placedPieces in win_combos):
			self.win_list[nextmini] = "O"
			print("player X WON THE GAME!!!")
			self.explodeBoard()

	 	#O test
		placedPieces = []
		for i in range(0,9):
			if(self.win_list[i] == 'O'):
				placedPieces += [i]
		if(placedPieces in win_combos):
			self.win_list[nextmini] = "O"
			print("player O WON THE GAME!!!")
			self.explodeBoard()

	def checkSmallBoardVictory(self):
		if(self.win_list[nextmini] == " "):
			#X test
			placedPieces = []
			for i in range(0,9):
				if(self.miniboards[nextmini].spacelist[i] == 'X'):
					placedPieces += [i]

			if(placedPieces in win_combos):
				self.win_list[nextmini] = "X"
				print("player X won board")

		 	#O test
			placedPieces = []
			for i in range(0,9):
				if(self.miniboards[nextmini].spacelist[i] == 'O'):
					placedPieces += [i]
			if(placedPieces in win_combos):
				self.win_list[nextmini] = "O"
				print("player O won board")

	def explodeBoard(self):
		self.miniboards[0].changeBGs("yellow")
		self.miniboards[1].changeBGs("red")
		self.miniboards[2].changeBGs("blue")
		self.miniboards[3].changeBGs("red")
		self.miniboards[4].changeBGs("blue")
		self.miniboards[5].changeBGs("yellow")
		self.miniboards[6].changeBGs("blue")
		self.miniboards[7].changeBGs("yellow")
		self.miniboards[8].changeBGs("red")

	def get_token_wins(self, token): 
		"""Returns a list of all boards that the player has won."""
		return [pos for pos, value in enumerate(self.win_list) if value == token]
		
	def check_win_p(self):
		"""Checks to see if a player has won the whole game."""
		result = -1
		for token in tokens: 													#iterate through the players
			positions = set(self.get_token_wins(token)) 						#create a set of the boards the player has won
			for win_line in win_combos: 										#iterate through every possible winning combination
				win = True 														#set the default to True
				for pos in win_line: 											#compare positions
					if pos not in positions: 										
						win = False 											#If there is no winner, set boolean to false
						break 													#escape loop
				if win:
					result = token 												#return the winning player
		print("DEBUG: Result: " + str(result))
		print("DEBUG: Boards: ")
		return result 	
	
	def is_board_full(board_pos): 												#checks if specific board is full
		if len(self.board_list[board_pos].available_moves()) == 0:
			return True
		else: 
			return False
		
	def nextturn(self):
		"""Increments to the next player, represented by the int "turn". If it was the last player's turn, loop back to the first player."""
		if self.turn < len(tokens) - 1:
			self.turn += 1
		elif self.turn == len(tokens) - 1:
			self.turn = 0
		else:
			print("ERROR: cannot increment turns. Current turn: " + str(self.turn))
	
	def nextBoard(self, boardnum):
		if self.firstplay == False:
			global nextmini 
			global currentmini
			global prevmini
			prevmini = currentmini
			currentmini = nextmini
			nextmini = boardnum
		else:
			self.firstplay = False
		
class Board(Frame):
	def __init__(self, squarenum=0, *args, **kwargs):
		Frame.__init__(self, *args, **kwargs)
		self.num = squarenum
		self.spacelist = [EMPTY for i in range(9)]
		self.labellist = []                            							#List of labels
		self.lvars = []															#List of the label string vars
		
	def changeBGs(self, color):
		for label in self.labellist:
			label.configure(bg = color)
		
	def makeMove(self, labelnum, token):
		"""Changes the token of the space in the board."""
		self.spacelist[labelnum] = token
		self.lvars[labelnum].set(token)
		#Check to make sure move has been executed correcly
		if self.spacelist[labelnum] != str(self.lvars[labelnum].get()):
			print("ERROR: Board.makeMove tokens not equal.")
			print("       spacelist: \""+self.spacelist[labelnum]+"\", lvar: \"" +str(self.lvars[labelnum].get())+"\"")
	
	def checkState(self):
		"""Checks to see if the board is full. Returns true if board is filled, false if there is a spot open."""
		isFull = True
		for label in labellist:
			if label.text == "":                 								#If any token in the board is blank, board is not full
				isFull = False
		return isFull
		
	def canMove(self, snum):
		if self.spacelist[snum] == EMPTY:
			return True
		else:
			print("DEBUG: space not empty: " + str(self.spacelist[snum]))
			return False
		
	def available_moves(self): 													#lists all the open positions on the board
		return [pos for pos, value in enumerate(self.spacelist) if value is EMPTY]

	def get_token_pos(self, token): 											#given a token it will return all the moves that player has made
		return [pos for pos, value in enumerate(self.spacelist) if value == token]
	
	def check_win_p(self): 														#returns the wining player or None if no one has won
		if self.winner == None: 												
			for token in tokens: 												#iterate through the players
				positions = set(self.get_token_pos(token)) 						#create a set of the positions the player has played in
				for win_line in win_combos: 									#iterate through every possible winning combination
					win = True 													#set the default to True
					for pos in win_line: 										#compare positions
						if pos not in positions: 								#if any positions is not in the winnign combination
							win = False 										#set it to False
							break 												#escape loop
					if win:
						self.winner = player 									#set the winning player variable
						return player 											#return the winning player
			return None 														#if no winner return None
		else:
			return self.winner 													#return know winner
	
	def addLabel(self, label):
		"""Adds a label to the board's list of labels."""
		self.labellist.append(label)
class gButton(Button):
	"""Extends the tkinter.button class: the gButton takes an int 
			'squarenum' that determines what square the button represents (from 0 to SLENGTH*SHEIGHT)."""
	def __init__(self, squarenum=0, *args, **kwargs):
		self.num = squarenum
		self.winner = None
		Button.__init__(self, command=self.attemptPlay,*args, **kwargs)			#Extend the Button class
	
	def attemptPlay(self):
		"""Changes the token of the corresponding label on the board. 
			Passes to the attemptPlay method in the GameManager class."""
		ui.attemptPlay(self.num)
		
	def changeState(self, onState):
		if onState:
			self.configure(state='normal')
		elif not onState:
			self.configure(state='disabled')
			
class gLabel(Label):
	"""Extends the tkinter.Label class: the gLabel takes an int 
			'squarenum' that determines what square the label represents, from 0 to SLENGTH*SHEIGHT."""
	def __init__(self, squarenum=0, *args, **kwargs):
		Label.__init__(self, *args, **kwargs)									#Extend the Label class
		self.num = squarenum
		
root = Tk()
ui = GameManager(root)
root.mainloop()
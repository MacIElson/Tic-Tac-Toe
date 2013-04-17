win_combos =(set([0, 1, 2]),
			 set([3, 4, 5]), 
			 set([6, 7, 8]),
			 set([0, 3, 6]), 
			 set([1, 4, 7]), 
			 set([2, 5, 8]),
			 set([0, 4, 8]),
			 set([2, 4, 6])) #All possible winning combinations

class tic_tac_toe_board(): #tic-tac-toe board object
	def __init__(self):
		self.board_list = [None for i in range(9)] #create empty list representing the board
		self.winner = None #Winner of board

	def make_move(self, location, player): #given a location (0-8) and a player it will place the player there
		board_list[location] = player

	def available_moves(self): #lists all the open positions on the board
		return [pos for pos, value in enumerate(self.board_list) if value is None]

	def get_player_pos(self, player): #given a player it will return all the moves they have made
		return [pos for pos, value in enumerate(self.board_list) if value == player]

	def check_win_p(self): #returns the wining player or None if no one has won
		if self.winner == None: #check if board has already been won
			for player in ('x', 'o'): #iterate through the players
				positions = set(get_player_pos(player)) #create a set of the positions the player has played in
				for win_line in win_combos: #iterate through every possible winning combination
					win = True #set the default to True
					for pos in win_line: #compare positions
						if pos not in positions: #if any positions is not in the winnign combination
							win = False #set it to False
							break #escape loop
					if win:
						self.winner = player #set the winning player variable
						return player #return the winning player
			return None #if no winner return None
		else:
			return self.winner #return know winner
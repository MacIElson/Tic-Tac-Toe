import tic_tac_toe_board

win_combos =(set([0, 1, 2]),
			 set([3, 4, 5]), 
			 set([6, 7, 8]),
			 set([0, 3, 6]), 
			 set([1, 4, 7]), 
			 set([2, 5, 8]),
			 set([0, 4, 8]),
			 set([2, 4, 6])) #All possible winning combinations

class meta_board(): #tic-tac-toe board object
	def __init__(self):
		self.board_list = [tic_tac_toe_board() for i in range(9)] #create list of boards
		self.win_list = [None for i in range(9)] #create empty list to hold the winners of the boards

	def check_win_p(self): #returns the wining player
	for player in ('x', 'o'): #iterate through the players
		positions = set(get_player_wins(player)) #create a set of the boards the player has won
		for win_line in win_combos: #iterate through every possible winning combination
			win = True #set the default to True
			for pos in win_line: #compare positions
				if pos not in positions: #if any positions is not in the winnign combination
					win = False #set it to False
					break #escape loop
			if win:
				return player #return the winning player
	return None #return None if no one won

	def get_player_wins(self, player): #returns a list of all boards the player has won
		return [pos for pos, value in enumerate(self.win_list) if value == player]

	def make_move(self, board_pos, player_pos, player): #makes the move specified by the inputs
		self.board_list[board_pos].make_move(player_pos, player) #makes the move in the specified board
		win_list[board_pos] == self.board_list[board_pos].check_win_p() #check if the player won that board and update win_list

	def is_board_full(board_pos): #checks if specific board is full
		if len(self.board_list[board_pos].available_moves()) == 0:
			return True
		else: 
			return False

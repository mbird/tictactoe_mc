"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

    
def mc_trial(board, player):
    """
    This function takes a current board and the next player to move. 
    The function should play a game starting with the given player by 
    making random moves, alternating between players. The function 
    should return when the game is over. The modified board will contain 
    the state of the game, so the function does not return anything. In 
    other words, the function should modify the board input.
    """
    while board.get_empty_squares() != []:
        board.move(random.randrange(board.get_dim()), random.randrange(board.get_dim()), player)
        board.move(random.randrange(board.get_dim()), random.randrange(board.get_dim()), provided.switch_player(player))
        # check_win returns 2 (X) and 3 (O) therefore can't check for PLAYERX or PLAYERO
        if board.check_win() == 2 or board.check_win() == 3: 
            break
    print board
#    print board.check_win()

    
    
def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores (a list of lists) with 
    the same dimensions as the Tic-Tac-Toe board, a board from a 
    completed game, and which player the machine player is.
    The function should score the completed board and update the 
    scores grid. As the function updates the scores grid directly, 
    it does not return anything,
    """
    # create grid of zeros for holding scores
    scores = [[0 for row in range(board.get_dim())] for col in range(board.get_dim())]
    # if X wins increase score for every move X made and decrease for O
    if board.check_win() == 2:
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                if board.square(row, col) == 2:
                    scores[row][col] = SCORE_CURRENT
                elif board.square(row, col) == 3:
                    scores[row][col] = - SCORE_OTHER
    # if O wins increase score for every move O made and decrease for X
    elif board.check_win() ==3:
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                if board.square(row, col) == 3:
                    scores[row][col] = SCORE_OTHER
                elif board.square(row, col) == 2:
                    scores[row][col] = - SCORE_CURRENT
                
    print scores
#    print board
    
def get_best_move(board, scores):
    """
    This function takes a current board and a grid of scores. The 
    function should find all of the empty squares with the maximum 
    score and randomly return one of them as a (row, column) tuple. 
    It is an error to call this function with a board that has no 
    empty squares (there is no possible next move), so your function 
    may do whatever it wants in that case. The case where the board 
    is full will not be tested.
    """
    
    
    
def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player 
    is, and the number of trials to run. The function should use the Monte 
    Carlo simulation described above to return a move for the machine 
    player in the form of a (row, column) tuple. Be sure to use the other 
    functions you have written!
    """


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)


#Board = provided.TTTBoard(3)
#scores = None
#mc_trial(Board, provided.PLAYERX)
#mc_update_scores(scores, Board, provided.PLAYERX)


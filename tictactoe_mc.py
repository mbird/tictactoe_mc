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
    """
    
    
def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores (a list of lists) with 
    the same dimensions as the Tic-Tac-Toe board, a board from a 
    completed game, and which player the machine player is.
    """
    
    
def get_best_move(board, scores):
    """
    This function takes a current board and a grid of scores.
    """
    
    
    
def mc_move(board, player, trials):
    """
    This function takes a current board, which player the 
    machine player is, and the number of trials to run.
    """


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

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
#    print board
#    print board.get_empty_squares()
    while board.get_empty_squares() != []:
        empty_squares = board.get_empty_squares()
        next_move = random.randrange(len(empty_squares))
        board.move(empty_squares[next_move][0], empty_squares[next_move][1], player)
#        print board
#        print board.get_empty_squares()
        # check_win returns 2 (X) and 3 (O) therefore can't check for PLAYERX or PLAYERO
        if board.check_win() == 2 or board.check_win() == 3: 
            break
        empty_squares = board.get_empty_squares()
        next_move = random.randrange(len(empty_squares))
        board.move(empty_squares[next_move][0], empty_squares[next_move][1], provided.switch_player(player))    
#        print board
#        print board.get_empty_squares()
        # check_win returns 2 (X) and 3 (O) therefore can't check for PLAYERX or PLAYERO
        if board.check_win() == 2 or board.check_win() == 3: 
            break
#    print board
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
    #scores = [[0 for row in range(board.get_dim())] for col in range(board.get_dim())]
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

    #print scores
    
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
    row = random.randrange(board.get_dim())
    col = random.randrange(board.get_dim())
    while scores[row][col] != 0:
        row = random.randrange(board.get_dim())
        col = random.randrange(board.get_dim())
        if scores[row][col] == 0:
            best_move = (row, col)
            break
    if scores[row][col] == 0:
            best_move = (row, col)
    return best_move
    
    
def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player 
    is, and the number of trials to run. The function should use the Monte 
    Carlo simulation described above to return a move for the machine 
    player in the form of a (row, column) tuple. Be sure to use the other 
    functions you have written!
    """
    board_score = 0
    running_total = 0
    trials_run = 0
    max_score = 0
    best_board = []
    grid_score = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    while trials_run < trials:
        mc_trial(board, player)
        trials_run += 1
        mc_update_scores(grid_score, board, player)
        #print grid_score
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                board_score += grid_score[row][col]
                if board_score > max_score:
                    max_score = board_score
                    best_board = board.clone()
                    best_scores = grid_score
        running_total += board_score
    best_scores = grid_score
    best_move = get_best_move(best_board, best_scores)
    #print best_move
    return best_move
        


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)


#Board = provided.TTTBoard(3)
#grid_score = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#mc_trial(Board, provided.PLAYERX)
#mc_update_scores(grid_score, Board, provided.PLAYERX)
#print grid_score
#print get_best_move(Board, [[-1.0, -1.0, 1.0], [-1.0, 1.0, 1.0], [1.0, 0, 1.0]])
#mc_move(Board, provided.PLAYERX, 10)

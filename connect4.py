# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:53:11 2021

@author: dylan
"""
#connect 4: 
#need to be able to input values 
#matrix as the board

#1. input - range 0-6 col
#2. valid col? if T
#3 if T what is the next open row?
#4 place piece in that next open row, of selected col
#need to end game when connected 4

#loop only way that game_over = T if 4 in a row
import numpy as np

ROW_COUNT = 6
COL_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT,COL_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece

#chack if top row for that column hasnt been filled-top row (5th) still 0

def is_valid(board, col):
    return board[ROW_COUNT-1][col] == 0

#next open row within that column loop if that row =0
# is available so return the first position avaiable in that col

def open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r
        
#numpy has the 0 index at the top of the matrix as default - so must flip it
# - logical sense for players 
#(0 at the bottom)
        
def print_board(board):
    print(np.flip(board, 0))

#winning - letting you know it's over
# to do this - can manually check all the possible winning positions and see
# if that matches - check every turn - to know which player won - (over all
#the possible starting positions of a winning move)

# im sure this isnt the best way - but didnt want to sink too much time into
# this - any suggestions would be very welcome
#[though about cheching around each piece, so may look at that if i try to
# refine this :)]

def winning_move(board, piece):
    #1. check all horizontals for winning move - all starting position
    #of winning move horizontal win e.g. cant start 4 in as only have 3 
    #horizontal spaces not the required 4, the last = 3rd col (starting at 0)
    #loop that iterates over the columns
    
    for c in range (COL_COUNT-3):
        for r in range (ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    #vertical locations
    #opposite of horizontal - any 4 up
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    #positively sloped diaganols
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    #negative slope- requires different - 
    # rows 0-6 ascending - can only have 4 starting from 3rd row
    for c in range(COL_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True   
    
    
board = create_board()
print(board)
game_over = False
turn = 0

while not game_over:
    #ask for the first player input column
    if turn == 0:
        col = int(input("Player 1 Make your Move (0-6):"))
        if is_valid(board, col):
            row = open_row(board, col)
            drop_piece(board, row, col, 1)
            
            if winning_move(board, 1):
                print("PLAYER 1 WINS!")
                game_over = True
                
  #first player's assigned as 1
    
  #second player's input
    else:
        col = int(input("Player 2 Make your Move (0-6):"))
        if is_valid(board, col):
            row = open_row(board, col)
            drop_piece(board, row, col, 2)
            
            if winning_move(board, 2):
                print("PLAYER 2 WINS!")
                game_over = True
                break
            
  #second player is assigned as 2
            
    print_board(board)
    #once turn is played need to update the board - print the new board
    
    #increase the turn by 1 every play
    #(%2) alternating between players turns
    turn +=1
    turn = turn % 2





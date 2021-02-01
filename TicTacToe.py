#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 17:39:40 2020

@author: aaronwright

Title: Naughts and Crosses

"""

# Steps
# Build Tic-Tac-Toe game that allows humans to play against one another.
# Plug AIs into the game engine.
# Pit AIs against each other.

   ############################
   #        #        #        #
   #        #        #        #
   #        #        #        #
   #        #        #        #
   ############################
   #        #        #        #
   #        #        #        #
   #        #        #        #
   #        #        #        #
   ############################
   #        #        #        #
   #        #        #        #
   #        #        #        #
   #        #        #        #
   ############################

############## Naughts and Crosses ################

# Import required libraries
import itertools
import random
import termtables as tt
import time

# Set parameters of board
BOARD_DIM = 3

# Set options for board
NAUGHT = "O"; CROSS = "X"; EMPTY = " "

# Set possible winner combinations
WINNERS = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]

# Generate board
def create_board():
    return [[EMPTY]*BOARD_DIM for x in range(BOARD_DIM)]

# Pretty print board to console
def render(board):         
    print(tt.to_string(board))
    
# Determine where user wants to place their naught or cross
def get_move():
    move = 0
    while True:
        try:
            move = int(input("Enter number from 1 to 9: "))
            if move not in range(1, 9 + 1):
                raise ValueError
            break
        except ValueError:
            print("Try again. Please input integer between 1 and 9")
    return move

# Add naught or cross to the board based on user input
def make_move(new_board, move, player):    
    count = 1
    for row in range(0, BOARD_DIM):
        for element in range(0, BOARD_DIM):
            if move == count:
                if new_board[row][element] is not EMPTY:
                    raise Exception("Illegal move. Cell taken. Try again!")
                new_board[row][element] = player[1]
            count +=1
    return new_board

# Determine if we have a winner
def get_winner(board, symbol):  
    # If cell contains current players symbol, add index to cells list
    cells = []
    count = 1
    for row in range(0, BOARD_DIM):
        for element in range(0, BOARD_DIM):
           if board[row][element] is symbol:
               cells.append(count) 
           count +=1
        
    # Find all possible permutations of length 3. Check if these are winners.
    combo = list(itertools.permutations(cells, 3))
    win = [i for i in combo if i in WINNERS]
    
    if len(win) > 0:
        return True
    
# Determine if board is full
def board_full(board):
    for row in board:
        for element in row:
            if element is EMPTY:
                return False         
    return True

# Print board to let players know the correct indexes
def helper(helpBoard):
    count = 1
    for x in range(0, 3):
        for y in range(0, 3):
            helpBoard[x][y] = count
            count +=1           
    render(helpBoard)
    
# Get names of players
def get_players():
    
    players = [["", CROSS], 
               ["", NAUGHT]]
    while True:
        try:
            players[0][0] = str(input("Player 1, what is your name: "))
            players[1][0] = str(input("Player 2, what is your name: "))
            print()
            break
        except ValueError:
            print("Please enter a string. No numbers.")
    return players

# Run to have two unintelligent AIs battle
def random_ai(board, player):
    time.sleep(1)
    legal_moves = []
    count = 0
    for row in range(0, BOARD_DIM):
        for element in range(0, BOARD_DIM):
            count += 1
            if board[row][element] is EMPTY:
                legal_moves.append(count)
                
    return random.choice(legal_moves)
                
################## Main Script ####################

# Create boards
board = create_board(); helpBoard = create_board()

# Print a help board
helpBoard = helper(helpBoard)

# Get player names
players = get_players()

count = 0
while True:
    
    # Derterime who's turn it is.
    player = players[0] if (count % 2) == 0 else players[1]
    
    print("{}. It is your turn. Your symbol is "
          "{}.".format(player[0], player[1]))
    
    # Ask player where they wish to move.
    move = get_move()
    #move = random_ai(board, player[1])
    
    # Make move the player has specified.
    board = make_move(board, move, player); render(board)
   
    # End game if there is a winner or if board is full.
    winner = get_winner(board, player[1])
    if winner:
        print("We have a winner! Congrats {}!".format(player[0]))
        break
    
    boardFull = board_full(board)
    if boardFull:
        print("It's a tie! Board is full!")
        break
    
    count += 1







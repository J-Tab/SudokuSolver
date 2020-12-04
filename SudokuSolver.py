import tkinter as tk

initialMatrix = [9][9]
solvingMatrix = [9][9]
finishedMatrix = [9][9]



#Starts solving sudoku problem; finds the first empty box
def solve():
    solvingMatrix = initialMatrix
    for y in solvingMatrix:
        for x in y:
            # Checks to see if the box is empty
            if x == 0:

#Checks to see if a number can be placed in the box
#x is x position in the sudoku
#y is y position in the sudoku
#num is the number being checked in the box
def isValid(x, y, num):
    #Check if number is valid in row
    for i in solvingMatrix[y]:
        if i == num:
             return False
    #Check if number is valid in column
    for rows in solvingMatrix:
        if rows[x] == num:
            return False
    #Check if number is valid in box
    boxRow = x - x%3
    boxCol = y - y%3
    for i in range(0,3):
        for j in range(0,3):
            if(solvingMatrix[i+boxRow][j+boxCol] == num):
                return False

    return True






# -*- coding: utf-8 -*-
"""
Created on Sun May 15 03:36:05 2022

@author: almas
"""

M = 9
def puzzle(a):
    print("Solution:")
    for i in range(M):
        for j in range(M):
            print(a[i][j],end = " ")
        print()
def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
             
    for x in range(9):
        if grid[x][col] == num:
            return False
 
 
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
def Suduko(grid, row, col):
 
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, M + 1, 1): 
     
        if solve(grid, row, col, num):
         
            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False
 

from dokusan import generators
import numpy as np
arr=np.array(list(str(generators.random_sudoku(avg_rank=150))))
arr=arr.astype(int)
grid=arr.reshape(9,9)
print("Problem grid:",grid)

 
if (Suduko(grid, 0, 0)):
    puzzle(grid)
else:
    print("Solution does not exist:(")
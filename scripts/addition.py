# Matrices have a wide range of applications in programming: they're used for digital image processing, 
# graph representation and algorithms on a graph, graphic effects, applied math, statistics, and much more.
# Since matrices are tables of numbers, they are usually presented in code as 2D-arrays. 
# In this project, you will learn how to read and output matrices, do operations on them, 
# and compute the determinant of a square matrix. At first, you will work with matrices with integer elements, 
# and later the elements will be floating-point numbers.
#
# Description
# Let’s start with matrix addition.
# For two matrices to be added, they must have an equal number of rows and columns. 
# The sum of matrices AA and BB will be a matrix with the same number of rows and columns as AA or BB. 
# The sum of AA and BB, denoted A + BA+B or B + AB+A, is computed by adding the corresponding elements of AA and BB.
#
# Objectives
# In this stage, you should write a program that:
# - reads matrix AA from the input.
# - reads matrix BB from the input.
# - outputs their sum if it is possible to add them; otherwise, it should output the ERROR message.
# Each matrix in the input is given in the following way: the first line contains the number of rows nn and the number of columns mm. 
# Then nn lines follow, each containing mm integers representing one row of the matrix.
# Output the result in the same way but don't print the dimensions of the matrix.
#
# Examples
# Example 1:
# Input:
# 4 5
# 1 2 3 4 5
# 3 2 3 2 1
# 8 0 9 9 1
# 1 3 4 5 6
# 4 5
# 1 1 4 4 5
# 4 4 5 7 8
# 1 2 3 9 8
# 1 0 0 0 1
# Output:
# 2 3 7 8 10
# 7 6 8 9 9
# 9 2 12 18 9
# 2 3 4 5 7
# 
# Example 2:
# Input:
# 2 3
# 1 4 5
# 4 5 5
# 4 5
# 0 1 0 4 5
# 1 7 8 9 4
# 1 2 3 5 6
# 1 3 4 3 8
# Output:
# ERROR

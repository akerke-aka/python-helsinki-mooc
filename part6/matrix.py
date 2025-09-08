"""
Matrix
------
Functions for working with matrices stored in a text file

Functions:
- read matrix(): reads a matrix from "matrix.txt" and returns it in a new list with integers
- matrix_sum(): returns the sum of all numbers in the matrix
- matrix_max(): returns the maximum number from all numbers in the matrix
- row_sums(): returns a list of sums for each row in a matrix 
"""
def matrix_sum():
     matrix = read_matrix()
     matrix_sum = 0
     for row in matrix:
          for number in row:
               matrix_sum += number
     return matrix_sum
def matrix_max():
     matrix = read_matrix()
     matrix_max = 0
     for row in matrix:
          for number in row:
               if number > matrix_max:
                    matrix_max = number
     return matrix_max
def row_sums():
     matrix = read_matrix()
     row_sum = []
     for row in matrix:
          summ = 0
          for number in row:
               summ += number
          row_sum.append(summ)
     return row_sum
def read_matrix():
     with open("matrix.txt") as file:
          matrix = []
          for line in file:
               parts = line.strip().split(",")
               row = []
               for number in parts:
                    row.append(int(number))
               matrix.append(row)
     return matrix


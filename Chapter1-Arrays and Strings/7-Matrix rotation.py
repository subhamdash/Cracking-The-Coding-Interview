# -*- coding: utf-8 -*-
"""
1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. (an you do this in place?

                                                          Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""
def rotate(matrix):
        N = len(matrix)
        print("Normal Matrix",matrix)
        
        
        for i in range(N):
            for j in range(i, N):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
                
        
        for i in range(N):
            for j in range(N//2):
                matrix[i][j],matrix[i][N-j-1] = matrix[i][N-j-1],matrix[i][j]
        print("Rotated Matrix",matrix)
matrix =[[ 5, 1, 9,11],[ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]]
rotate(matrix)
 

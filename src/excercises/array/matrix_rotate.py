from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Input: 2D array representing an image
        Output: Same image rotated clockwise 90 degrees
        Do not return anything, modify matrix in-place instead.
        """
        matrix_copy = [row[:] for row in matrix]
        n = len(matrix)
        for y in range(n):
            for x in range(n):
                matrix[x][n-1-y] = matrix_copy[y][x]


class Solution2:
    """
    Rotating one layer at a time and saving only two rows
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        layers = len(matrix) // 2
        for l in range(layers):
            self.rotate_sublayer(matrix, l)
            
    def rotate_sublayer(self, matrix, i):
        n = len(matrix)
        src = matrix[i][i:n-i]
        src_idx = 0
        bkp = []
        
        for yi in range(i, n - i):
            bkp.append(matrix[yi][n - 1 - i])
            matrix[yi][n - 1 - i] = src[src_idx]
            src_idx += 1

        src = bkp
        src_idx = 0
        bkp = []
        
        for xi in range(n-1-i, i-1, -1):
            bkp.append(matrix[n - 1 -i][xi])
            matrix[n - 1 - i][xi] = src[src_idx]
            src_idx += 1

        bkp[0] = src[-1]    
        src = bkp
        src_idx = 0
        bkp = []
        
        for yi in range(n - 1 - i, i - 1, -1):
            bkp.append(matrix[yi][i])
            matrix[yi][i] = src[src_idx]
            src_idx += 1
                
        bkp[0] = src[-1]
        src = bkp
        src_idx = 0
        
        for xi in range(i, n - 1 - i):
            matrix[i][xi] = src[src_idx]
            src_idx += 1


class Solution3:
    """
    Rotate in place, 4 pixels at a time. Space complexity: O(1)
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for y in range(n//2):
            for x in range(y, n - y - 1):
                self.rotate_pixel(matrix, y, x)
    
    def rotate_pixel(self, matrix, y, x):
        swp = matrix[y][x]
        matrix[y][x] = matrix[~x][y]
        matrix[~x][y] = matrix[~y][~x]
        matrix[~y][~x] = matrix[x][~y]
        matrix[x][~y] = swp

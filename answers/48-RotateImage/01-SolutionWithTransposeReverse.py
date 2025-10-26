class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        #Transpose matrix
        for i in range(len(matrix)):
            for j in range(i, len(matrix[i])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        #reverseMatrix
        for i in range(len(matrix)):
            k = len(matrix[i]) -1
            for j in range(len(matrix[i])):
                if(j<k):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[i][k]
                    matrix[i][k] = temp
                    k-=1
                else:
                    break
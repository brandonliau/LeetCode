class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix[0]) - 1
        rowl, rowh = 0, len(matrix) - 1

        while rowl <= rowh:
            row = (rowl + rowh) // 2
            if matrix[row][low] > target:
                rowh = row - 1
            elif matrix[row][high] < target:
                rowl = row + 1
            else:
                while low <= high:
                    mid = (low + high) // 2
                    if matrix[row][mid] == target:
                        return True
                    elif matrix[row][mid] > target:
                        high = mid - 1
                    elif matrix[row][mid] < target:
                        low = mid + 1
                        
        return False
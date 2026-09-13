class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev_row = [0] * n
        curr_row = [0] * n
        curr_row[-1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                curr_row[j] += prev_row[j]
                if j + 1 < n:
                    curr_row[j] += curr_row[j + 1]
                
            prev_row = curr_row
            curr_row = [0] * n
        
        return prev_row[0]
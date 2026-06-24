class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        fresh_amount = 0
        minutes = 0
        dq = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_amount += 1
                elif grid[i][j] == 2:
                    dq.append((i, j))
        
        while dq and fresh_amount > 0:
            size = len(dq)

            for _ in range(size):
                rotton_i, rotton_j = dq.popleft()
                
                if rotton_i - 1 >= 0 and grid[rotton_i-1][rotton_j] == 1:
                    fresh_amount -= 1
                    grid[rotton_i-1][rotton_j] = 2
                    dq.append((rotton_i-1, rotton_j))
                if rotton_i + 1 < len(grid) and grid[rotton_i+1][rotton_j] == 1:
                    fresh_amount -= 1
                    grid[rotton_i+1][rotton_j] = 2
                    dq.append((rotton_i+1, rotton_j))
                if rotton_j - 1 >= 0 and grid[rotton_i][rotton_j-1] == 1:
                    fresh_amount -= 1
                    grid[rotton_i][rotton_j-1] = 2
                    dq.append((rotton_i, rotton_j-1))
                if rotton_j + 1 < len(grid[0]) and grid[rotton_i][rotton_j+1] == 1:
                    fresh_amount -= 1
                    grid[rotton_i][rotton_j+1] = 2
                    dq.append((rotton_i, rotton_j+1))
                
            minutes += 1
        
        return minutes if fresh_amount == 0 else -1

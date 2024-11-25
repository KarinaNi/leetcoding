from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rowlen = len(grid)
        collen = len(grid[0])
        found = False
        queue = deque()
        def helper(r,c):
            grid[r][c]= 2

            if r+1 < rowlen and grid[r+1][c] == 1:
                helper(r+1,c)
            if r-1 >= 0 and grid[r-1][c] == 1:
                helper(r-1,c)
            if c+1 < collen and grid[r][c+1] == 1:
                helper(r,c+1)
            if c-1 >= 0 and grid[r][c-1] == 1:
                helper(r,c-1)
            return

        for i in range(rowlen):
            for j in range(collen):
                if found:
                    break
                if grid[i][j] == 1:
                    found = True
                    helper(i,j)
                    break

        while queue:
            for _ in range(len(queue)):
                x,y,time = queue.popLeft()

                if x+1 < rowlen:
                    if grid[x+1][y] == 1:
                        return time
                    if grid[x+1][y] == 0:
                        grid[x+1][y] = 3
                        queue.append((x+1,y,time+1))
                if x-1 >= 0:
                    if grid[x-1][y] == 1:
                        return time
                    if grid[x-1][y] == 0:
                        grid[x-1][y] = 3
                        queue.append((x-1,y,time+1))
                if y+1 < collen:
                    if grid[x][y+1] == 1:
                        return time
                    if grid[x][y+1] == 0:
                        grid[x][y+1] = 3
                        queue.append((x,y+1,time+1))
                if y-1 >= 0:
                    if grid[x][y-1] == 1:
                        return time
                    if grid[x][y-1] == 0:
                        grid[x][y-1] = 3
                        queue.append((x,y-1,time+1))




        return -1

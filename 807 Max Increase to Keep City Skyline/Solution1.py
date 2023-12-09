class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        addedHeight = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                maxHeightLR = grid[i][j]
                maxHeightUD = grid[i][j]
                for k in range(len(grid[i])):
                    maxHeightLR = max(maxHeightLR, grid[i][k])
                for k in range(len(grid)):
                    maxHeightUD = max(maxHeightUD, grid[k][j])
                addedHeight += min(maxHeightLR, maxHeightUD) - grid[i][j]
        return addedHeight
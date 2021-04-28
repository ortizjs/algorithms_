class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n + 1)] for x in range(m + 1)]
        print dp
        # if len(dp[0][1]) >= 1:
        dp[0][1] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if obstacleGrid[i-1][j-1] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0
        return dp[m][n]

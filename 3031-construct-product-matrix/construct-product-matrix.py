class Solution:
    def constructProductMatrix(self, grid):
        MOD = 12345
        n, m = len(grid), len(grid[0])

        ans = [[0] * m for _ in range(n)]

        pref = 1

        # Prefix pass
        for i in range(n):
            for j in range(m):
                ans[i][j] = pref
                pref = (pref * (grid[i][j] % MOD)) % MOD

        suf = 1

        # Suffix pass
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                ans[i][j] = (ans[i][j] * suf) % MOD
                suf = (suf * (grid[i][j] % MOD)) % MOD

        return ans

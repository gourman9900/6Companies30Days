def maxProfit(self, K, N, A):
    @lru_cache(None)
    def dp(i,rem,buy):
        nonlocal N
        if i >= N:return 0
        if rem == 0:return 0
        if buy:
            return max(-A[i] + dp(i+1,rem,False),dp(i+1,rem,True))
        else:
            return max(A[i] + dp(i+1,rem-1,True),dp(i+1,rem,False))
    return dp(0,K,True)

def getNthUglyNo(self,n):
	    dp = [0]
	    dp[0] = 1
	    two,three,five = 0,0,0
	    for i in range(2,n+1):
            j = dp[two] * 2
            k = dp[three] * 3
            l = dp[five] * 5
            if min(j,k,l) == j:
                two += 1
            if min(j,k,l) == k:
                three += 1
            if min(j,k,l) == l:
                five += 1
	        dp.append(min(j,k,l))
	    return dp[-1]

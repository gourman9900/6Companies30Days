def CountWays(self, str1):
	    dp = [0] * (len(str1) + 1)
	    length = len(str1)
	    dp[0] = 1
	    dp[1] = 1
	    if length == 1 and str1[0] != "0":return 1
	    if str1[0] == "0":return 0
	    for i in range(2,length+1):
	        c1,c2 = 0,0
	        if (str1[i-1] > "0"):
	            c1 = dp[i-1]
	        if (str1[i-2] == "1" or (str1[i-2] == "2" and str1[i-1] <= "6")):
	            c2 = dp[i-2]
	        dp[i] = (c1 + c2) % int((1e9) + 7)
	    return dp[-1]

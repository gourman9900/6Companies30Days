def canPair(self, nums, k):
        index = defaultdict(int)
        count = Counter(nums)
        for i in nums:
               index[i % k] += 1
        if 0 in index:
            if index[0] % 2 != 0:return False
	    for i in index:
	        if i == 0:continue
	        if k - i not in index:return False
	        if (index[i] + index[k - i]) % 2 != 0 or index[i] != index[k - i]:return False
	    return True

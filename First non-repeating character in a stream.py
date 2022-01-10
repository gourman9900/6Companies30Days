def FirstNonRepeating(self, A):
        ans = ""
        seen = []
        appeared = set()
        index = defaultdict(lambda :0)
	    for i in range(len(A)):
	        if A[i] not in seen and A[i] not in appeared:
	            seen.append(A[i])
	        else:
	            appeared.add(A[i])
	            if A[i] in seen:seen.remove(A[i])
	        if seen:
	            ans += seen[0]
	        else:
	            ans += "#"
	    return ans

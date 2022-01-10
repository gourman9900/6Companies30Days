def matchPairs(self,nuts, bolts, n):
	    order = ["!","#","$","%","&","*","@","^","~"]
	    nuts[:] = [i for i in order if i in bolts]
	    bolts[:] = [i for i in order if i in nuts]

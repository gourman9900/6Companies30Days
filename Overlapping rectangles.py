def doOverlap(self, L1, R1, L2, R2):
        
        if (L1[0] <= R2[0] and R1[0] >= L2[0] and L1[1] >= R2[1] and R1[1] <= L2[1]):return 1
        return 0

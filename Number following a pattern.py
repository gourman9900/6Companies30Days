def printMinNumberForPattern(ob,S):
        ans = "".join(list(map(str,range(1,len(S) + 2))))
        left,right = None,None
        for i in range(len(S)):
            if S[i] == "D":
                if left != None:
                    right = i + 1
                else:
                    left = i
            else:
                if left != None:
                    right = i + 1
                    ans = ans[:left] + ans[left:right][::-1] + ans[right:]
                    left = None
        if left != None:
            ans = ans[:left] + ans[left:][::-1]
            left = None
                
        return ans

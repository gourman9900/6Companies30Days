def gcdofString(str1,str2):
    ans = ""
    i,j = 0,0
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            if str1[i] not in ans:ans += str1[i]
            i += 1
            j += 1
        else:
            break
    return ans

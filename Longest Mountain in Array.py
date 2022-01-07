def longestMountain(arr):
        ans = -float("inf")
        inc = 0
        dec = 0
        for i in range(1,len(arr)):
            if arr[i] > arr[i-1]:
                if dec > 0:
                    inc = 1
                else:inc += 1
            elif arr[i] < arr[i-1]:
                if inc > 0:
                    dec += 1
                    inc -= 1
                    ans = max(ans,dec)
                else:
                    inc = 0
                    dec = 0
            else:
                inc = 0
                dec = 0
            
        return (ans * 2) + 1 if ans != -float("inf") else 0

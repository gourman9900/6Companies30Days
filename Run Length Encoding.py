def encode(arr):
    ans = ""
    prev = None
    count = 0
    for i in range(len(arr)):
        if prev == None:
            ans += arr[i]
            count = 1
            prev = arr[i]
        elif prev == arr[i]:
            count += 1
        else:
            ans += str(count)
            ans += arr[i]
            prev = arr[i]
            count = 1
    ans += str(count)
    return ans

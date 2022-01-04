def minsubarray(nums,target):
    ans = float("inf")
    curr = 0
    left,right = 0,0
    while left <= right and right < len(nums):
            print(left,right)
            while curr < target and right < len(nums):
                curr += nums[right]
                right += 1
            while curr >= target:
                curr -= nums[left]
                left += 1
            if curr >= target:ans = min(ans,(right - left + 1))
            if right == len(nums):
                break
    return ans if ans != float("inf") else 0

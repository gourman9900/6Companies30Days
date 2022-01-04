def countSubArrayProductLessThanK(self, a, n, k):
        ans = 0
        curr = 1
        left,right = 0,0
        while left <= right and right < len(a):
                while curr < k and right < len(a):
                    curr *= a[right]
                    right += 1
                    if curr < k:ans += (right - left)
                while left <= right and curr >= k:
                    curr = curr // a[left]
                    left += 1
                    if curr < k:ans += (right - left)
        return ans

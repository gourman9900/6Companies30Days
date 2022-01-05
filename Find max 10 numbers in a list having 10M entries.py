from heapq import heappush,heappop
def maxn(arr,k):
  ans = []
  heap = []
  for i in arr:
    heappush(heap,-arr[i])
  for i in range(k):
    ans.append(-heappop(heap))
  return ans

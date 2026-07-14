import heapq

nums = [4,7,1,2,3]
# min heap
heapq.heapify(nums)
print(nums)
# insert()
heapq.heappush(nums,9)
print(nums)
# extractmin()
smallest = heapq.heappop(nums)
print(smallest)
print(nums)
# peek
print(nums[0])


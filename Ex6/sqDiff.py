import math

nums = list(range(1,101))
i = 1
total = 0
for i in nums:
    total += math.pow(i,2)


print(math.pow(sum(nums),2) - total)
nums = []
sums = [0] * 5

with open('input.txt') as fp:
    for line in fp:
        nums.append(map(int, [line[i:i+10] for i in range(0, len(line), 10)][0:5]))

i = 0
j = 0

for i in list(range(0,len(nums[0]))):
    for j in list(range(0,len(nums))):
        sums[i] += nums[j][i]


sums[3] += int(str(sums[4])[0:len(str(sums[4]))-10])
sums[2] += int(str(sums[3])[0:len(str(sums[3]))-10])
sums[1] += int(str(sums[2])[0:len(str(sums[2]))-10])
sums[0] += int(str(sums[1])[0:len(str(sums[1]))-10])

print sums[0]
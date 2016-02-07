nums = [[]]
start = 0

with open('input.txt') as fp:
    for line in fp:
        nums.append([])
        numsAsString = str.split(line)
        i = 0
        j = len(numsAsString)
        while i < j:
            nums[start].append(int(numsAsString[i]))
            i += 1
        start += 1
nums.pop()

def getRight(y,x):
    global nums
    if(x+3 > (len(nums[y])-1)):
        return 0

    return nums[y][x] * nums[y][x+1] * nums[y][x+2] * nums[y][x+3]

def getLeft(y,x):
    global nums
    if(x-3 < 0):
        return 0

    return nums[y][x] * nums[y][x-1] * nums[y][x-2] * nums[y][x-3]

def getUp(y,x):
    global nums
    if(y-3 < 0):
        return 0

    return nums[y][x] * nums[y-1][x] * nums[y-2][x] * nums[y-3][x]

def getDown(y,x):
    global nums
    if(y+3 > len(nums)-1):
        return 0

    return nums[y][x] * nums[y+1][x] * nums[y+2][x] * nums[y+3][x]

def getDiag(y,x):
    global nums
    if(y+3 > (len(nums)-1) or x+3 > (len(nums[y])-1)):
        return 0

    return nums[y][x] * nums[y+1][x+1] * nums[y+2][x+2] * nums[y+3][x+3]

def getDiag2(y,x):
    global nums
    if(y+3 > len(nums)-1 or x-3 < 0):
        return 0

    return nums[y][x] * nums[y+1][x-1] * nums[y+2][x-2] * nums[y+3][x-3]

def getMax(y,x):
    return max(getLeft(y,x), getRight(y,x), getUp(y,x), getDown(y,x), getDiag(y,x),getDiag2(y,x))

i = 0
j = 0
Max = 0

for i in list(range(0, len(nums[0]))):
    for j in list(range(0,len(nums))):
        if(getMax(i,j) > Max):
            Max = getMax(i,j)

print(Max)


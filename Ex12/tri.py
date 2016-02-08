import math

def getFactors(num):
    i = 1
    lst = []
    while i < math.ceil(math.sqrt(num)):
        if not num % i:
            if not i in lst:
                lst.append(i)
            if not (num/i) in lst:
                lst.append(num/i)
        i += 1
    return lst

triNum = 0
inc = 1


while len(getFactors(triNum)) < 500:
    triNum += inc
    inc += 1

print(triNum)
import math

MAX = 999

i = MAX
j = MAX

maxPal = 0

def isPal(num):
    first = 0
    numText = str(num)
    last = len(numText)-1
    mid = math.floor(len(numText)/2)

    while first <= mid:
        if first == mid:
            return True
        else:
            if numText[first] != numText[last]:
                return False
            first += 1
            last -= 1


for i in range(999,0,-1):
    for j in range(999,0,-1):
        if(isPal(i*j)):
            if maxPal < i*j:
                maxPal = i*j

print(maxPal)


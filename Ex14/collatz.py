x = 1000000
maxCol = 0
maxNum = 0
def nextNum(nxt):
    temp = nxt
    cnt = 1

    while not temp == 1:
        if not temp % 2:
            temp = temp/2
        else:
            temp = (3*temp)+1
        cnt += 1
    return cnt


while x > 0:

    if nextNum(x) > maxNum:
        maxCol = x
        maxNum = nextNum(x)

    x -= 1

print(maxCol, maxNum)
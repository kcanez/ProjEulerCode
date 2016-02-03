def modList(num):
    i = 1
    setList = list(range(1,21))
    for i in setList:
        if num % setList[i-1]:
            return False
    return True

start = 20

while True:
    if(modList(start)):
        print(start)
        exit(155)
    start += 20
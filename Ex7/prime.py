import math

primeCount = 1
start = 2



while True:
    i = 2
    while i <= math.ceil(math.sqrt(start)):
        if not start % i:
            break
        elif i >= math.ceil(math.sqrt(start)):
            primeCount += 1
            print(start, " - ", primeCount)
        i += 1


        if primeCount == 10001:
            print(start)
            exit(155)

    start += 1
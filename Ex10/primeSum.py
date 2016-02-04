import math

primeSum = 2
start = 2



while True:
    i = 2
    while i <= math.ceil(math.sqrt(start)):
        if not start % i:
            break
        elif i >= math.ceil(math.sqrt(start)):
            primeSum += start
        i += 1


        if start  >= 2000000:
            print(primeSum)
            exit(155)

    start += 1
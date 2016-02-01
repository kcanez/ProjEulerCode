num = 234325325

primeFactors = []
isPrime = []
finished = False

def getFactors(x):
    i = 2

    if x ==1:
        return x

    while True:
        if x % i == 0:
            return [i, x/i]
        else:
            if i >= (x/2):
                return x
            i += 1

    return 0


facts = getFactors(num)
primeFactors.append(facts[0])
primeFactors.append(facts[1])
isPrime.append(False)
isPrime.append(False)
i = 0

while not finished:

    print(getFactors(primeFactors[i]), primeFactors[i])

    if not isPrime[i]:
        if getFactors(primeFactors[i]) == primeFactors[i]:
            isPrime[i] = True
            i = 0
        else:
            facts = getFactors(primeFactors[i])
            primeFactors.pop(i)
            isPrime.pop(i)
            if len(facts) == 1:
                primeFactors.append(facts)
                isPrime.append(False)
            else:
                primeFactors.append(facts[0])
                primeFactors.append(facts[1])
                isPrime.append(False)
                isPrime.append(False)
            i = 0

    i += 1
    print(primeFactors)
    print(isPrime)

    print(all(isPrime))

    if all(isPrime):
        print(primeFactors)
        exit(155)


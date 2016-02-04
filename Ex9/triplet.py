import math

a = 1
b = 1
i = 0
absquared = 0.0
sqrtab = 0.0
piTrip = []

MAX = 400

while a <=MAX:
    b = a + 1
    while b <= MAX and a < b:
        absquared = math.pow(a,2) + math.pow(b,2)
        sqrtab = math.sqrt(absquared)



        if sqrtab > b and sqrtab == int(sqrtab):
            piTrip.append([a,b,int(sqrtab)])

        b += 1
    a += 1

while True:
    if (piTrip[i][0] + piTrip[i][1] + piTrip[i][2]) == 1000:
        print(piTrip[i])
        print(piTrip[i][0] * piTrip[i][1] * piTrip[i][2])
    i += 1

    if i >= len(piTrip):
        exit(155)






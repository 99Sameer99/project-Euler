import math


def sopd(n):  # sopd is sum of proper divisors of n excluding n
    sum = 1
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            if n / i == i:
                sum += i
            else:
                sum += i + (n / i)
        i += 1
    if int(sum) == n:
        return 1
    return int(sum)


m = 10
sum = 0
while m <= 10000:
    sugma = sopd(m)
    ligma = sopd(sugma)
    if ligma == m:
        print(m, sugma)
        sum += m
    m += 1
print(sum)
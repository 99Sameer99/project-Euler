import math
import time


def pf(n):
    lst = []
    if n % 2 == 0:
        lst.append(2)
    while n % 2 == 0:
        n = n//2
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            lst.append(i)
        while n%i == 0:
            n = n/i
    if n > 2 and len(lst) > 0:
        lst.append(int(n))
        return lst
    else:
        return lst


def totient(lst):  # this function gives numbers of co-primes for n
    m = n
    for i in lst:
        m *= (1 - (1/i))
    return int(m)


print('Calculating.....')
n = 2
mnmm = 1
s = time.time()
while True:
    lon = list(range(1, n))  # lon is list of numbers
    prime_factors = pf(n)
    if len(prime_factors) > 0:
        tot = totient(prime_factors)
        res = tot / (n-1)  # res is resilience for the denominator n
        #print(res, 'is Resilience and', tot, 'is Totient for', n, 'with factors', prime_factors)
        if mnmm > res:
            mnmm = res
            print('resilience', mnmm, 'for', n, 'with factors', prime_factors)
        if res < 15499/94744:
            print('===========================')
            print('Resilience is:', res, 'for', n, 'and has prime factors', prime_factors)
            print(time.time()-s, 'seconds took to calculate')
            break
    n += 1
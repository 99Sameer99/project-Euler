import math


def prmnmbrs(n):
    lopn = []
    prime = [True for i in range(n + 1)]
    p = 2
    while p <= n:
        if prime[p]:
            lopn.append(p)
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return lopn  # returns list of prime numbers till n


def pf(n):
    lof = []
    while n%2 == 0:
        lof.append(2)
        n = n/2
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n%i == 0:
            lof.append(i)
            n = n / i
    if n > 2:
        lof.append(int(n))
    return lof


def totient(list, num):  # this function gives numbers of co-primes for n
    m = num
    for i in list:
        m *= (1 - (1/i))
    return m


def resilience(num):
    res = totient(lopn[:n], num) / (num - 1)
    return res


lopn = prmnmbrs(100)
print(lopn, '====', 15499/94744)
lon = list(range(2,100))
# loc = list(set(lon) - set(lopn))
n = 1
while n <= len(lopn):
    num = 1
    for i in range(n):
        num *= lopn[i]
    # print('{}----{}----{}'.format(num, lopn[n-1], lopn[n]))
    num = num * (lopn[n] - 1)
    res = resilience(num)
    if res < 15499/94744:
        print('{}--for n--{}===={}========================================================='.format(res, num, pf(num)))
        num = num // (lopn[n] - 1)
        for i in range(1, lopn[n]):
            res = resilience(num * i)
            if res < 15499/94744:
                print('{}----{}----{}'.format(res, num * i, lopn[:n] + [i]))
    n += 1
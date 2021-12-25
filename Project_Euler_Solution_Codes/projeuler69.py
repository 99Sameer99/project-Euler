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


def totient(lst):
    m = 1
    for i in lst:
        m *= (1 - (1/i))
    return m


mxmm = 0
lopn = prmnmbrs(100)
print(lopn)
# lon = list(range(1,100))
# loc = list(set(lon) - set(lopn))
n = 1
while n <= len(lopn):
    num = 1
    for i in range(n):
        num *= lopn[i]
    if num > 1000000:
        break
    ratio = 1 / totient(lopn[:n])
    if ratio > mxmm:
        mxmm = ratio
        print('{}----{}----{}'.format(mxmm, num, lopn[:n]))
    n += 1
#A program that gives you list of prime numbers of n,list of prime factors of n and smallest number divisible by all numbers less than n
#where n is a natural number
#A really stupidass program

import math
import time

def pf(n):
    prmfctrs = []
    while n%2 == 0: #dividing by two until numbers turns odd so that factor of twois out
        prmfctrs.append(2)
        n = n/2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i == 0:
            prmfctrs.append(i)
            n = n/i
    if n>2:
        prmfctrs.append(int(n))
    return prmfctrs #returns prime factors of n


def prmnmbrs(n):
    lopn = []
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n + 1):
        if prime[p]:
            lopn.append(p)

    return lopn  # returns list of prime nubers till n

def sum_of_prmnmbrs(n):
    return sum(lopn)

def nth_prime(n):
    m = len(lopn)
    p = lopn[-1]
    r = 0
    while m <= n :
        k = 0
        for i in range(2,p+1):
            if p % i == 0:
                k = k + 1
        if k == 1:
            #print(str(p) + ' is the ' + str(m) + 'th prime') #remove the # befor print to see the loop running because it takes time when n is large,if you are interested otherwise just watch the blank computer screen
            m = m + 1
        p = p + 1
        r = r + 1
    return p - 1
                
    

while True:
    print('Enter x to exit the program')
    n = input('Enter the number till which you want it to be divisible by: ')
    print('-----------------------------------------------------')
    if n.lower()== 'x':
        exit()
    n = int(n)
    start=time.time()
    print('List of prime numbers till ' + str(n))
    lopn = prmnmbrs(n)
    print(lopn)
    print('-----------------------------------------------------')

    prdct = 1
    for i in lopn:
        prdct = prdct * i #product of all prime numbers till n

    print('Poduct of all prime numbers till ' + str(n) + ' is given below.')
    print(prdct)
    print('-----------------------------------------------------')
    Sum = sum_of_prmnmbrs(n)
    print('Sum of all Prime numbers till ' + str(n))
    print(Sum)
    print('-----------------------------------------------------')
    rng = list(range(1,n+1))
    left_over_num = list(set(rng) - set(lopn))


    dct = {}
    for i in lopn:
        if i in dct:
            dct[i] = dct[i] + 1
        else:
            dct[i] = 1

    for i in left_over_num:
        dct2 = {}
        m = pf(i)
        for i in m:
            if i in dct2:
                dct2[i] = dct2[i] + 1
            else:
                dct2[i] = 1
        #print(dct2)
        for i,j in dct2.items():
            if i not in dct.keys():
                dct.update({i,j})
            else :
                f = j - dct[i]
                if f >= 0 :
                    dct[i] = dct[i] + f

    q = nth_prime(n)
    print(str(n) + 'th prime number is: ' + str(q))

    prdct = 1
    for i,j in dct.items():
        prdct = prdct * (i**j)

    print('-----------------------------------------------------')
    print('Smallest number divisible by all numbers from 1 to ' + str(n) + ' is ' + str(prdct))
    print('prime factors of the above number')
    print(dct)
    print('-----------------------------------------------------')
    print(time.time()-start,'secs took to run')

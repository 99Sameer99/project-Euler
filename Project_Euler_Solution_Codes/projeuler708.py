import math
import time

def prmnmbrs(n):#using sieve of Eratosthenes to get all the prime numbers till n including n
    prime = [True for i in range(n+1)]
    p = 2
    while (p*p <= n):
        if prime[p] == True:
            for i in range( p*p , n+1 , p ):
                prime[i] = False
        p += 1
    
    return prime #returns list of prime nubers till n


def pf(n):#returns number of prime factors of n not the factors themselves
    nof = 0
    while n%2 == 0:#dividing by two until n becomes odd
        nof += 1
        n = n/2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i == 0:
            nof += 1
            n = n/i
    if n>2:
        nof += 1
    return nof


while True:
    sum = 11#sum already initialized for 1,2,3,4,5 and given f(1) is 1
    print('Enter x to exit')
    n = input('enter the number up to which calculation is to be done: ')
    if n.lower()== 'x':
        exit()
    else:
        n = int(n)
        start2 = time.time()
        prime = prmnmbrs(n)
        print('Time to create a list of prime numbers ' + str(time.time()-start2) + ' secs')
        start = time.time()
        k = 5# to count if went through all the numbers till n
        for i in range(6,n+1):
            if prime[i] == False:
                k += 1
                nof = pf(i)
                f = 2**(nof)
                sum = sum + f
            else:
                k += 1
                sum = sum + 2
    print(str(time.time() - start)+'sec for the calculations')
    print(sum)
    print('process performed on '+str(k)+' integers')
            
            
        

import time


def prmnmbrs(n):
    prime = [True for i in range(n+1)]
    prime[1] = False
    prime[0] = False
    p = 2
    while (p*p <= n):
        if prime[p] == True:
            for i in range( p*p , n+1 , p ):
                prime[i] = False
        p += 1
    
    return prime #returns list of prime nubers till n


sum = 0
tp = 0
n = int(input('enter the value of n: '))
prime = prmnmbrs(n)

for i in range(20,n+1):
    if i%10 == 3 or i%10 == 7:
        if prime[i] == True:
            t = 0
            p = 1
            while p <= len(str(i)):
                #print(i)
                qtnt = int( i//(10**p) )
                rem = int( i%(10**p) )
                if prime[qtnt]==True and prime[rem]==True:
                    #print('BITCH')
                    p += 1
                    continue
                elif qtnt == 0:
                    print(i)
                    tp += 1
                    sum = sum + i
                    break
                else:
                    break
print('=====================================')
print('Number of both left and right truncatable primes below'+str(n)+' are'+str(tp))
print('And their summation is '+str(sum))

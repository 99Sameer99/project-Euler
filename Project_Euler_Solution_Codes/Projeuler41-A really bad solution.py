from itertools import permutations

def primecheck(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    else:
        return True
    

n=10
requirednumber = 0
while n>0:
    objs =list(range(1,n))
    if sum(objs)%3 != 0:
        pmt=list(permutations(objs))[::-1]
        for j in pmt:
            if j[-1] in [1,3,7,9]:
                num = ''
                for k in j:
                    num = num+str(k)
                if primecheck(int(num)):
                    #print(num)
                    if requirednumber<int(num):
                        requirednumber = int(num)
                        #print('requirednumber-----',requirednumber)
    n = n-1
       

print(requirednumber)

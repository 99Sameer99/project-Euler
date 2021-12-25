import math

print('n^2 + axn + b')

def prmnmbr(p):
    n=int(math.fabs(p))
    for i in range(2,n):
        if p%i == 0:
            return False
            break
    else :
        return True

while True:
    print('enter x to exit or just press enter to continue')
    K = input('enter: ')
    if K=='x' or K=='X':
        exit()
    else:
        mp = 1
        for b in range(-1000,1001,1):
            if prmnmbr(b):
                for a in range(-999,1000,2):
                    if prmnmbr(a+b+1) and prmnmbr(b+1-a):
                        n=1
                        prm = 1
                        while True:
                            m = (n**2) + (a*n) + b
                            if prmnmbr(m):
                                prm += 1
                                n += 1
                                continue
                            else:
                                if prm > mp:
                                    mp = prm
                                    print(mp)
                                    reqa = a
                                    reqb = b
                                    
                            break
                    else:
                        continue
            else:
                continue
    print('a='+str(reqa))
    print('b='+str(reqb))
    print('max number of consecutive prime solutions '+str(mp)) 
        
        
    


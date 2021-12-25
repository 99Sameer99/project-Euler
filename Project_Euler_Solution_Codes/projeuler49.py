from math import sqrt

def pf(n):          #checking if a number n is prime or not
    for j in range(3,int(sqrt(n))+1,2):
        while n%j == 0:
            return False
    else:
        return True

def perm(m,r,add):   #perm=permutations of m taken r at a time
    n = len(m)
    if r==0:
        if int(add)>1001 and pf(int(add))==True:
            if int(add)%2 !=0:
                if not int(add) in lop:
                    lon.remove(int(add))
                    lop.append(int(add))
    for i in range(n):
        newadd = add+m[i]
        newobj = m[:i] + m[i+1:]
        perm(newobj,r-1,newadd)
    return lop     #list of permutations that are prime of a given number m where m is in range(1001,9999) and are also odd
        
lon=list(range(1001,9999,2))
for i in lon:
    if pf(i)==True:
        lop=[]
        perm(str(i),4,'')     #all the possible permutations of 4digit number taken 4 at time
        if len(lop)>=3:
            print(lop)
            for j in range(len(lop)):
                k=1
                m=len(lop)
                while k<=((m-j-1)/2):
                    if lop[j+k]-lop[j]==lop[j+(2*k)]-lop[j+k]:
                        print('==============================')
                        print(lop[j],lop[j+k],lop[j+(2*k)])
                    k+=1

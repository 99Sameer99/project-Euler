import time


while True:
    termslist = []
    c = input('If you want to exit the program enter x or just press enter to continue: ')
    if c == 'x' or c == 'X':
        exit()
    while True:
        t = input('enter the term number;when done enter end: ')
        if t != 'end':
            termslist.append(int(t))
        else:
            break
    digitlist = []
    mxtrm = max(termslist)
    exp = 1
    n = 0
    while exp <= mxtrm:
        exp = (9*(10**n))*(n+1)
        digitlist.append(exp)
        n += 1
    product = 1
    for m in termslist:
        sum = 0
        for i in digitlist:
            if sum <= m:
                sum = sum + i
                n = digitlist.index(i)
            else:
                break 
        M = m - sum + digitlist[n]
        if M%(n+1)==0:
            N = (10**n) -1 + M//(n+1)
            product = product * int( str(N)[-1] )
            print(str(m)+'th term is '+str(N)[-1])
        else:
            N = (10**n) + M//(n+1) 
            product = product * int( str(N)[(M%(n+1))-1] )
            print(str(m)+'th term is '+str(N)[(M%(n+1))-1])
    print('Product of the entered terms is: '+str(product))

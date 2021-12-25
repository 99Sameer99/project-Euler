fib = [1,2]
n = int(input('enter the number: '))
max = 10**(n)
i = 1
#print(fib[0])
#print(fib[1])
while True:
    n = fib[i-1] + fib[i]
    if n < max:
        fib.append(n)
        #print(n,fib.index(n)+1)
        if len(str(n)) == 1000:
            print(fib.index(n)+2)
            break
        i += 1
    else:
        break

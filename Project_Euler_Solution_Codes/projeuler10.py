
while True:
    print('Enter x to exit the program')
    n = input('Enter the number below which you want to add all the primes: ')
    if n == 'x' or n == 'X':
        exit()
    n = int(n)
    sum = 0
    lonn = list(range(n+1))
    lopn = []
    for i in range(2,n+1):
        if lonn[i]:
            lopn.append(i)
            sum = sum + i
            for j in range ( i**2 , n+1 , i ):
                lonn[j] = 0
    print('---------------------------------------------------------------------------------------')
    print('List of prime numbers before ' + str(n))
    print(lopn)
    print('---------------------------------------------------------------------------------------')
    print('Their sum is:')
    print(sum)


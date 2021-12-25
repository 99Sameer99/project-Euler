import time

def collatzlen(num):
    length = 1
    while num != 1:
        if num%2 == 0:
            length += 1
            num = num/2
        else:
            num = ( 3*num ) + 1
            length  += 1
    return length


while True:
    n = input('Enter the number: ')
    print('================================')
    if n =='x' or n=='X':
        exit()
    start = time.time()
    n = int(n)
    m = 0
    The_fucking_number_I_need = 0
    for i in range( 2 , n ):
        start2 = time.time()
        length = collatzlen(i)
        t = time.time() - start
        if length > m:
            m = length
            The_fucking_number_I_need = i
            time_that_this_fuckingnumber_took = t

    print('the number',The_fucking_number_I_need)
    print('collatz length',m)
    print('time took to get this result',t)
    print(str( time.time()-start) + ' seconds')


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
    lon = list(range(2,n))
    dict = {}
    for i in range( len(lon)  ):
        if lon[i] != 0:
            k = 0
            length = collatzlen( lon[i] )
            while (2**k) * lon[i]  <= n :
                #print( (2**k) * lon[i] )
                dict.update( { (2**k) * lon[i] : k + length } )
                #print( str( list(dict.keys())[-1] ) + '====' + str( list(dict.values())[-1] )  )
                k += 1
                try:
                    lon[ lon.index((2**k) * lon[i]) ] = 0
                except:
                    break
    keymax = max(dict, key=dict.get)
    print( str( keymax ) + '-----' + str( dict[keymax] ) )
    print('================================')
    #print(dict)
    print(time.time()-start)


            
        
        
               

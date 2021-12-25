#finding the largest prime factor of any number
num = int(input('enter the number: '))
topn = []
lopn = []
lopf = []
for i in range(2,num+1):
    for z in range(2,i+1):
        if i%z == 0:
            topn.append(z)
            #print(topn)
    if len(topn)==1:
        lopn.append(i)
        if num % lopn[-1] == 0:
            lopf.append(i)
    topn = []
#for i in lopn:
    #if num % i == 0:
        #lopf.append(i)




print('List of prime numbers until ' + str(num))
print(lopn)
print('=======================================================================')
print('List of prime factors of ' + str(num))
print(lopf)
print('=======================================================================')
print('Largest prime factor of ' + str(num) + ' is '+ str(max(lopf)))

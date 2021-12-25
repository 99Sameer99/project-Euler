#sum of all the multiples of 3 and 5 below 1000
n = int(input('enter the number below which operations would be done: '))
b = [i for i in range(n) if i%3==0 or i%5==0]
print(b)
print('======================================================================')
sum = 0
for i in b:
    sum = sum + i
print(sum)

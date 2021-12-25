fib = [1,2]
max = int(input('enter the value of maximim term: '))
i = 1
while True:
    n = fib[i-1] + fib[i]
    if n < max:
        fib.append(n)
    else:
        break
    i = i + 1
print(fib)
print(i)
print('===================================================')
sum = 0
for j in fib:
    if j%2 == 0:
        sum = sum + j
print(sum)

import timeit



code = """
m = int(input('Enter the number of times you want to use the code: '))
r = 0
while r < m:
    r = r + 1
    n = int(input('enter the number: '))
    print('Sum of squares of the first ' + str(n) + ' natural numbers')
    sum_of_squares = (n * (n + 1) * ((2*n) + 1))/6
    print(sum_of_squares)
    
    print('Square of the sum of first ' + str(n) + ' natural numbers')
    square_of_sum = (n * (n + 1) / 2)**2
    print(square_of_sum)
    
    print('The difference is ' + str(square_of_sum - sum_of_squares))
    """
time = timeit.timeit(stmt = code , number = 1)
print('Time taken to calculate: ' + str(time) + ' seconds')



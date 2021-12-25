import os


directory = 'C:\\Users\\HP\\Desktop\\python prog\\Project_Euler_Solution_Codes'
os.chdir(directory)

fl = open('p081_matrix.txt', 'r')

matrix1 = list()
for i in fl.readlines():
    lst = list(map(int, i.strip('\n').replace(',', ' ').split(' ')))
    matrix1.append(lst)

matrix2 = [[131, 673, 234, 103, 18],
           [201, 90, 342, 965, 150],
           [630, 803, 746, 422, 111],
           [537, 699, 497, 121, 956],
           [805, 732, 524, 37, 331]]

while True:
    n = input('enter 1 for matrix1 and 2 for matrix2 or x to exit: ')
    if n.lower() == 'x':
        exit()
    elif n == '1':
        matrix = matrix1
    else:
        matrix = matrix2
    m = len(matrix)
    for i in range(m):
        for j in range(m):
            if i*j > 0:
                matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1])
            else:
                if i != 0:
                    matrix[i][j] += matrix[i - 1][j]
                if j != 0:
                    matrix[i][j] += matrix[i][j - 1]
                else:
                    matrix[i][j] += 0

    print("Minimal path sum in", n, "by", m, "matrix =", matrix[-1][-1])
    print(matrix)
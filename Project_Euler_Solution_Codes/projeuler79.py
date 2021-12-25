import os
os.chdir('C:\\Users\\HP\\Desktop\\python prog\\Project_Euler_Solution_Codes')#directory change to open the attempts file

file=open('p079_keylog.txt','r')

losa=[]
for i in file.readlines():
    attempt=i.strip('\n')
    if not attempt in losa:
        losa.append(attempt)

print(losa,'=',len(losa))


plndrm = []
max = 0

for i in range(101,1000):
    for j in range(101,1000):
        num = str(i*j)
        mun = num[::-1]
        if num == mun :
            if max < int(num):
                max = int(num)
            #lst = [int(num),i,j]
           # plndrm.append(lst)
#for i in plndrm:
   # print(i)

#print(len(plndrm))
#print(max(plndrm))
print(max)



        

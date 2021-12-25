# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:04:32 2020

@author: sameer
"""
import math

def pf(n):
    primefactor_dict={}
    while n%2 == 0:
        if not 2 in primefactor_dict.keys():
            primefactor_dict[2]=0
        primefactor_dict[2]+=1
        n = n/2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i == 0:
            if not i in primefactor_dict.keys():
                primefactor_dict[i]=0
            primefactor_dict[i]+=1
            n = n/i
    if n>2:
        primefactor_dict[int(n)]=1
    return primefactor_dict


n=1
while True:
    Tn=(n*(n+1))/2   #Tn is Triangular number
    factors=pf(int(Tn))
    num_factors=1
    for i in factors.values():
        num_factors*=(i+1) #we can either choose the factor or not,if n^(i) than there are i+1 to choose it_
    if num_factors>=500:
        print('The 1st Triangular number to have over 500 divisors is:',int(Tn),'which is',n,'term')
        print('-----------------------------------------------------------')
        print('And its prime factors are:')
        print(factors)
        break
    n+=1
        

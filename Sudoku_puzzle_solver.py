from pysat.solvers import Solver
from pysat.card import *
import math
import numpy as np
import csv
import time
cnf = CNF()
pre_filled = []
start_time = time.time()
k = int(input("enter the value of k: "))
n = pow(k,2)
tent_list = []
pre_filled = []
data = 1
#each cell contains one number excatly once
for sudno in range(0,2):
    for i in range(0,n):
        for j in range(0,n):
            for num in range(0,n): 
                tent_list.append(data)
                data=data+1
            cnf.extend(CardEnc.equals(lits=tent_list,encoding=EncType.pairwise))
            tent_list.clear()
#each row contains one number excatly once
for sudno in range(0,2):
       for i in range(0,n):
           for num in range(1,n+1):
               for j in range(0,n):
                   tent_list.append(sudno*n*n*n+i*n*n+j*n+num)
               cnf.extend(CardEnc.equals(lits=tent_list,encoding=EncType.pairwise))
               tent_list.clear()           
#each column contains one number excatly once
for sudno in range(0,2):
       for j in range(0,n):
           for num in range(1,n+1):
               for i in range(0,n):
                   tent_list.append(sudno*n*n*n+i*n*n+j*n+num)
               cnf.extend(CardEnc.equals(lits=tent_list,encoding=EncType.pairwise))
               tent_list.clear()  
#each subgroup contains one number excatly once
for sudno in range(0,2):
    for num in range(1,n+1):
        for p in range(0,k):
            for q in range(0,k):
                for i in range(p*k,k*(p+1)):
                    for j in range(q*k,k*(q+1)):
                        tent_list.append(sudno*n*n*n+i*n*n+j*n+num)   
                cnf.extend(CardEnc.equals(lits=tent_list,encoding=EncType.pairwise))
                tent_list.clear()
#corresponding elements are unequal
for i in range(0,n):
    for j in range(0,n):
        for num in range(1,n+1):
            cnf.append([-(i*n*n+j*n+num),-(n*n*n+i*n*n+j*n+num)])
# taking the input csv file
with open("test_case_1.csv") as file_name:
    data = np.loadtxt(file_name, delimiter=",").astype(int)
def avail_it(i,j,l,n):
    return (int)(n*n*i+n*j+l)
#storing prefilled values
for i in range(0,2*n):
    for j in range(0,n):
        if data[i][j]!=0:
           pre_filled.append(avail_it(i,j,data[i][j],n))
cnf.append(list(pre_filled))
count = 0
g = Solver(bootstrap_with=cnf.clauses)
if g.solve(assumptions= pre_filled):
    model=g.get_model()
    for i in range (0,2*(k**6)):
        if model[i]>0:
            if model[i]%(k**2)!=0:
              print(model[i]%(k**2),end=" ")
            else:
                print(n,end=" ")
            count=count+1
            if count%n==0:
                print("\n")
if g.solve(assumptions= pre_filled)==False:
    print("The sudoku pair doesn't exist") 
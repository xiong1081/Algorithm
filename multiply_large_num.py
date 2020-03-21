#coding=utf-8
import sys

line=sys.stdin.readline()
line=line.strip().split()

array0=[]
array1=[]
summ=[]

for i in line[0]:
    array0.append(int(i))
for i in line[1]:
    array1.append(int(i))
    
if len(array0)>=len(array1):
    sum0=int(line[0])
    array1.reverse()
    for i in range(len(array1)):
        zero='0'*i
        num0=sum0*array1[i]
        num0=str(num0)+zero
        summ.append(int(num0))
else:
    sum1 = int(line[1])
    array0.reverse()
    for i in range(len(array0)):
        zero = '0' * i
        num0 = sum1 * array0[i]
        num0 = str(num0) + zero
        summ.append(int(num0))
        
print(str(sum(summ)))

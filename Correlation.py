#AIM: To find the correlation measures of numeric attributes (by Correlation Coefficient & Covariance) & nominal attributes (Chi-Square test) in a dataset

import numpy as np
import pandas as pd
data=pd.read_csv('num.csv')
a, b = data['A1'].values.tolist(), data['A2'].values.tolist()
n=len(a)
prodab,coeff,cov,chi=0,0,0,0
ct = [[0 for i in range(3)] for j in range(3)]
meana=np.mean(a)
meanb=np.mean(b)
sda=np.std(a)
sdb=np.std(b)
for i in range(n):
	prodab += (a[i]-meana)*(b[i]-meanb)
coeff = prodab/((n-1)*sda*sdb)
cov = prodab/n
print("Pearson moment coefficient for numeric attributes: \nCorrelation coefficient =", coeff,"\tCovariance =", cov, "\nChi-Square test for nominal attributes: \nInput the contingency table:")
for i in range(2):
	for j in range(2):
		ct[i][j] = int(input())
tbchi = float(input("Input the chi-square table value at required level of significance: "))
ct[0][2] = ct[0][0] + ct[0][1]
ct[1][2] = ct[1][0] + ct[1][1]
ct[2][0] = ct[0][0] + ct[1][0]
ct[2][1] = ct[0][1] + ct[1][1]
ct[2][2] = ct[2][0] + ct[2][1]
for i in range(2):
	for j in range(2):
		ex = (ct[i][2] * ct[2][j]) / ct[2][2]
		chi += ((ct[i][j] - ex) ** 2) / ex
print("Contingency table =", ct, "\nCalcuated chi-square value =", chi)

if chi > tbchi:
	print("Null hyphothesis rejected -> data is highly correlated")
else:
	print("Null hyphothesis cannot be rejected")

'''
_____________________________________________________
input dataset: [num.csv]
A1,A2
12,7
23,6
34,5
45,4
56,3
67,2
78,1
89,0
_____________________________________________________
output:
Pearson moment coefficient for numeric attributes:
Correlation coefficient = -1.142857142857143 	Covariance = -57.75 
Chi-Square test for nominal attributes:
Input the contingency table:
20
30
40
50
Input the chi-square table value at required level of significance: 7.81
Contingency table = [[20, 30, 50], [40, 50, 90], [60, 80, 140]] 
Calcuated chi-square value = 0.2592592592592592
Null hyphothesis cannot be rejected   
'''

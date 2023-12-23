'''AIM: (a) To find the mean, median, mode 
        (b) Check the data is unimodal, bimodal, trimodal or multimodal
        (c) find the quartiles & outliers '''

import pandas as pd
import numpy as np
import statistics as st

def detect_modes(mod):
	c=len(mod)
	if c == 1:
		return "Unimodal"
	elif c == 2:
		return "Bimodal"
	elif c == 3:
		return "Trimodal"
	else:
		return "Multimodal"
    
def calculate_quartiles_outliers(num):
	quartiles = np.quantile(num, [0.25,0.5,0.75])
	iqr = quartiles[2] - quartiles[0]
	lower = quartiles[0] - 1.5*iqr
	upper = quartiles[2] + 1.5*iqr
	for i in num:
		if (i < lower)|(i > upper):
			outliers.append(i)
	return quartiles, outliers
  
data=pd.read_csv('dataset.csv')
num=list(data['Marks'])
outliers=[]
mod=st.multimode(num)
quartiles, outliers = calculate_quartiles_outliers(num) 
print("Mean:", st.mean(num),"\nMedian:", st.median(num),"\nMode:", mod, "->", detect_modes(mod), "\nStandard Deviation:",np.std(num))
print(f"Quartiles: Q1 = {quartiles[0]}, Q2 = {quartiles[1]}, Q3 = {quartiles[2]}")
if len(outliers)!=0:
	print(f"Outliers: {outliers}")
else:
	print("No outliers found")

'''
_____________________________________________________
input file: [student.csv]               
Rollno,Name,Class,Marks
1,Adhya,11A,78
2,Ananya,11B,96
3,Arun,11A,85
4,Nithya,11A,67
5,Sanju,11B,94
6,Vishnu,11A,77
_____________________________________________________
output:
Mean: 82.83333333333333 
Median: 81.5 
Mode: [78, 96, 85, 67, 94, 77] -> Multimodal 
Standard Deviation: 10.089873911776873
Quartiles: Q1 = 77.25, Q2 = 81.5, Q3 = 91.75
No outliers found
'''

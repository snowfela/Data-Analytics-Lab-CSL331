#AIM: To print the dissimilarity matrices of nominal and numeric attributes in a dataset

import pandas as pd
import numpy as np

def display(matrix, n):
	for i in range(n):
	    for j in range(i + 1):
	        print("{0:.2f}".format(matrix[i][j]), end = '   ')
        print(" ")

def calculate_dissimilarity(df):
    discombined = np.zeros((len(df), len(df)))
    disnum = np.zeros((len(df), len(df)))
    disnom = np.zeros((len(df), len(df)))
    for i in range(len(df)):
        for j in range(len(df)):
            num_sum = 0
            den_sum = 0
            for f in df.columns:
                if pd.isnull(df[f][i]) or pd.isnull(df[f][j]):
                    delta_ij = 0
                    continue
                delta_ij = 0 if df[f][i] == df[f][j] else 1
                if df[f].dtype in ['int64', 'float64']:  #Numeric attribute
                    d_ij_f = abs(df[f][i] - df[f][j]) / (df[f].max() - df[f].min())
                    disnum[i, j] = d_ij_f
                elif df[f].dtype == 'object':  #Nominal or binary attribute
                    d_ij_f = 0 if df[f][i] == df[f][j] else 1
                    disnom[i, j] = d_ij_f
                num_sum += delta_ij * d_ij_f
                den_sum += delta_ij
            discombined[i, j] = num_sum / den_sum if den_sum != 0 else 0
    return discombined, disnum, disnom
  
df = pd.read_csv('student.csv')
discombined, disnum, disnom = calculate_dissimilarity(df)
print("Combined Dissimilarity Matrix:")
display(discombined, len(df))
print("Numeric Dissimilarity Matrix:")
display(disnum, len(df))
print("Nominal Dissimilarity Matrix:")
display(disnom, len(df))

'''
_____________________________________________________
input dataset: [student.csv]
Rollno,Name,Class,Marks
1,Adhya,11A,78
2,Ananya,11B,96
3,Arun,11A,85
4,Nithya,11A,67
5,Sanju,11B,94
6,Vishnu,11A,77
_____________________________________________________
output:
Combined Dissimilarity Matrix:
0.00    
0.71   0.00    
0.55   0.64   0.00    
0.66   0.85   0.61   0.00    
0.84   0.56   0.68   0.78   0.00    
0.68   0.86   0.63   0.58   0.70   0.00    
Numeric Dissimilarity Matrix:
0.00    
0.62   0.00    
0.24   0.38   0.00    
0.38   1.00   0.62   0.00    
0.55   0.07   0.31   0.93   0.00    
0.03   0.66   0.28   0.34   0.59   0.00    
Nominal Dissimilarity Matrix:
0.00    
1.00   0.00    
1.00   1.00   0.00    
0.00   1.00   1.00   0.00    
1.00   0.00   0.00   1.00   0.00    
0.00   1.00   1.00   0.00   1.00   0.00    
'''

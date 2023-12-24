#AIM: To implement Naive Bayes Classifier algorithm

import pandas as pd
import numpy as np

def calculate_probability(x, mean, stdev, n):
    exponent = np.exp(-((x-mean)**2 / (2 * stdev**2 )))
    probability = (1 / (np.sqrt(2 * np.pi) * stdev)) * exponent
    probability = (probability + 1) / (n + 2)   #Laplace smoothing
    return probability

def summarize_by_class(dataset):
    separated = dataset.groupby('BUYS')
    summaries = {}
    for class_value, subset in separated:
        summaries[class_value] = [(subset[column].mean(), subset[column].std(), len(subset[column])) for column in subset.columns if column != 'BUYS']
    return summaries

def calculate_class_probabilities(summaries, row):
    total_rows = sum([summaries[label][0][2] for label in summaries])
    probabilities = {}
    for class_value, class_summaries in summaries.items():
        probabilities[class_value] = summaries[class_value][0][2]/float(total_rows)
        for i in range(len(class_summaries)):
            mean, stdev, count = class_summaries[i]
            probabilities[class_value] *= calculate_probability(row[i], mean, stdev, count)
    return probabilities

def predict(summaries, row):
    probabilities = calculate_class_probabilities(summaries, row)
    best_label, best_prob = None, -1
    for class_value, probability in probabilities.items():
        if best_label is None or probability > best_prob:
            best_prob = probability
            best_label = class_value
    return best_label

data = pd.read_csv('dataset.csv')
data = data.applymap(lambda x: {'LOW': 0, 'MEDIUM': 1, 'HIGH': 2, 'NO': 0, 'YES': 1, 'FAIR': 0, 'EXCELLENT': 1}.get(x, x))
age = int(input("Enter AGE: "))
income = input("Enter INCOME: ").upper()
student = input("Enter STUDENT: ").upper()
credit_rating = input("Enter CREDIT_RATING: ").upper()
x = [age, 0 if income == 'LOW' else 1 if income == 'MEDIUM' else 2, 1 if student == 'YES' else 0, 1 if credit_rating == 'FAIR' else 0]
summaries = summarize_by_class(data)
probabilities = calculate_class_probabilities(summaries, x)
prediction = predict(summaries, x)
print("Prediction:", "YES" if prediction == 1 else "NO")

'''
_____________________________________________________
input dataset: [dataset.csv]               #same as that of Decision Tree Classifier to be used
AGE,INCOME,STUDENT,CREDIT_RATING,BUYS
30,HIGH,NO,FAIR,NO
42,HIGH,NO,EXCELLENT,NO
35,HIGH,NO,FAIR,NO
38,MEDIUM,NO,FAIR,NO
43,LOW,YES,FAIR,YES
42,LOW,YES,EXCELLENT,NO
50,LOW,YES,EXCELLENT,YES
53,MEDIUM,NO,FAIR,NO
48,LOW,YES,FAIR,YES
25,MEDIUM,YES,FAIR,YES
25,MEDIUM,YES,EXCELLENT,YES
43,MEDIUM,NO,EXCELLENT,YES
42,HIGH,YES,FAIR,YES
40,MEDIUM,NO,EXCELLENT,NO

_____________________________________________________
output:
Enter AGE: 48
Enter INCOME: low
Enter STUDENT: yes
Enter CREDIT_RATING: fair
Prediction: YES   
'''

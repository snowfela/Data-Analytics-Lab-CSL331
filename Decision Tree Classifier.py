#AIM: To implement Naive Bayes Classifier algorithm

import pandas as pd
import numpy as np

def entropy(y):
    _, counts = np.unique(y, return_counts=True)
    p = counts / y.size
    return -np.sum(p * np.log2(p))

def info_gain(data, feature, target):
    total_entropy = entropy(data[target])
    values, counts = np.unique(data[feature], return_counts=True)
    weighted_entropy = np.sum([(counts[i] / np.sum(counts)) * entropy(data[data[feature] == values[i]][target]) for i in range(len(values))])
    return total_entropy - weighted_entropy

def ID3(data, features, target="BUYS"):
    if len(np.unique(data[target])) <= 1:
        return np.unique(data[target])[0]
    elif len(features) == 0:
        return np.argmax(np.bincount(data[target]))
    else:
        gains = [info_gain(data, feature, target) for feature in features]
        best_feature = features[np.argmax(gains)]
        tree = {best_feature: {}}
        features = [f for f in features if f != best_feature]
        for value in np.unique(data[best_feature]):
            subtree = ID3(data[data[best_feature] == value], features, target)
            tree[best_feature][value] = subtree
        return tree

def predict(x, tree):
    for key in x.keys():
        if key in tree.keys():
            try:
                result = tree[key][x[key]]
            except:
                return np.argmax(np.bincount(data['BUYS']))
            if isinstance(result, dict):
                return predict(x, result)
            else:
                return result

data = pd.read_csv('dataset.csv')
data = data.applymap(lambda x: {'LOW': 0, 'MEDIUM': 1, 'HIGH': 2, 'NO': 0, 'YES': 1, 'FAIR': 0, 'EXCELLENT': 1}.get(x, x))
tree = ID3(data, data.columns[:-1])
age = int(input("Enter AGE: "))
income = input("Enter INCOME: ").upper()
student = input("Enter STUDENT: ").upper()
credit_rating = input("Enter CREDIT_RATING: ").upper()
x = {'AGE': age, 'INCOME': {'LOW': 0, 'MEDIUM': 1, 'HIGH': 2}[income], 'STUDENT': {'NO': 0, 'YES': 1}[student], 'CREDIT_RATING': {'FAIR': 0, 'EXCELLENT': 1}[credit_rating]}
prediction = predict(x, tree)
print("Prediction:", "YES" if prediction == 1 else "NO")

'''
_____________________________________________________
input dataset: [dataset.csv]               #same as that of Naive Bayes Classifier to be used
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

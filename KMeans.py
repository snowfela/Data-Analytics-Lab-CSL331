#AIM: to implement K-Means clustering algorithm

import pandas as pd
def k_means(data, k, max_iters=100):
    centroids = data[:k] 
    for _ in range(max_iters):
        clusters = [[] for _ in range(k)]
        for point in data:
            distances = [sum((c-p)**2 for c, p in zip(centroid, point)) for centroid in centroids] #add math.sqrt() to calculate the exact euclidean distance
            closest = distances.index(min(distances)) 
            clusters[closest].append(point) 
        new_centroids = [[sum(p[i] for p in cluster)/len(cluster) for i in range(len(data[0]))] for cluster in clusters]
        if new_centroids == centroids:    #Check for convergence
            break
        centroids = new_centroids
    return centroids, clusters
df = pd.read_csv('data.csv')
data = df.values.tolist() #to list of lists
k = 2
centroids, clusters = k_means(data, k)
print("Centroids:", centroids)
for i, cluster in enumerate(clusters, 1):
    print(f"Cluster {i}:", cluster)

'''
_____________________________________________________
input dataset: [data.csv]
x,y
1,2
3,0
2,5
10,1
5,3
9,1
_____________________________________________________
output:
Centroids: [[2.75, 2.5], [9.5, 1.0]]
Cluster 1: [[1, 2], [3, 0], [2, 5], [5, 3]]
Cluster 2: [[10, 1], [9, 1]]   
'''

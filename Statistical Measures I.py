#AIM: To find mean, median and mode 

import statistics as st
data=[]
data=list(map(int, input("Enter the data: ").split()))
print("Mean:", st.mean(data),"\nMedian:", st.median(data),"\nMode:", st.multimode(data))

_____________________________________________________
#output:
Enter the data: 12 23 34 45 67 78 89 90 12 23 34
Mean: 46.09090909090909 
Median: 34 
Mode: [12, 23, 34]

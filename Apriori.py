#AIM: To find the most frequent itemset in a dataset using apriori algorithm 

from itertools import chain, combinations

def load_data(file_path):
    transactions = []
    with open(file_path, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            tid, items = line.strip().split(',')
            transaction = items.split()
            transactions.append((tid, transaction))
    return transactions
  
def get_unique_items(data):
    unique_items = set()
    for transaction in data:
        for item in transaction:
            unique_items.add(frozenset([item]))
    return unique_items
  
def support_count(data, itemset):
    count = 0
    for transaction in data:
        if itemset.issubset(transaction):
            count += 1
    return count
  
def generate_candidate_itemsets(prev_itemsets, k):
    candidates = set()
    for item1 in prev_itemsets:
        for item2 in prev_itemsets:
            union = item1.union(item2)
            if len(union) == k:
                candidates.add(union)
    return candidates
  
def apriori(data, min_support):
    unique_items = get_unique_items(data)
    frequent_itemsets = []
    k = 1
    while True:
        if k == 1:
            candidate_itemsets = unique_items
        else:
            candidate_itemsets = generate_candidate_itemsets(prev_itemsets, k)
        prev_itemsets = candidate_itemsets.copy()
        frequent_itemsets_k = []
        for itemset in candidate_itemsets:
            support = support_count(data, itemset)
            if support >= min_support:
                frequent_itemsets_k.append(itemset)
        if not frequent_itemsets_k:
            break
        frequent_itemsets.extend(frequent_itemsets_k)
        k += 1
    return frequent_itemsets
  
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
  
def generate_rules(data, frequent_itemset, min_confidence):
    rules = []
    for antecedent in map(set, powerset(frequent_itemset)):
        if antecedent and antecedent != frequent_itemset:  # antecedent is not empty and is not the entire itemset
            consequent = frequent_itemset - antecedent
            confidence = support_count(data, frequent_itemset) / support_count(data, antecedent)
            if confidence >= min_confidence:
                rules.append((antecedent, consequent, confidence))
    return rules
  
min_support, min_confidence = 2, 0.7 # 70% min confidence
data = load_data("transact.csv")
transactions = [transaction for _, transaction in data]  #Extract items only
frequent_itemsets = apriori(transactions, min_support)
max_size = max(len(itemset) for itemset in frequent_itemsets)
most_frequent_itemsets = [itemset for itemset in frequent_itemsets if len(itemset) == max_size] #itemsets of largest size
print("Most Frequent Itemsets:")
for i, frequent_itemset in enumerate(most_frequent_itemsets, start=1):
    print(f"{set(frequent_itemset)}")
print("Association Rules:")
for i, frequent_itemset in enumerate(most_frequent_itemsets, start=1):
    rules = generate_rules(transactions, frequent_itemset, min_confidence)
    for rule in rules:
        a, c, confidence = rule
        print(f"{set(a)} => {set(c)} (Confidence: {confidence:.2f})")

'''
_____________________________________________________
input dataset: [transact.csv]
TID,ITEMS
T1,"A B C"
T2,"B D"
T3,"A D"
T4,"A B D"
T5,"A B C D"
_____________________________________________________
output:
Most Frequent Itemsets:
{'A', 'D', 'B'}
{'A', 'C', 'B'}
Association Rules:
{'C'} => {'A', 'B'} (Confidence: 1.00)
{'A', 'C'} => {'B'} (Confidence: 1.00)
{'C', 'B'} => {'A'} (Confidence: 1.00)
'''

from itertools import combinations, chain
from collections import defaultdict

transactions = [
    ['Math', 'Science'],
    ['Math', 'English'],
    ['English', 'Science'],
    ['Math', 'Science', 'English'],
    ['Science'],
    ['Math', 'English'],
    ['Math', 'Science'],
    ['English', 'Science'],
    ['Math', 'Science', 'English'],
    ['Math'],
    ['History', 'Science'],
    ['Math', 'History'],
    ['English', 'Math'],
    ['Geography', 'History'],
    ['Science', 'Geography'],
    ['Physical Education', 'Math'],
    ['Math', 'Science', 'Geography'],
    ['History', 'English'],
    ['Science', 'Physical Education'],
    ['Math', 'English', 'History'],
    ['Geography', 'Science'],
    ['Physical Education', 'History'],
    ['Math', 'Geography'],
    ['English', 'Geography'],
    ['Math', 'Science', 'Physical Education'],
    ['Science', 'English', 'History'],
    ['Geography', 'Physical Education'],
    ['Math', 'Science', 'Geography', 'English'],
    ['History', 'Science', 'Geography'],
    ['Math', 'Physical Education'],
    ['Math', 'History', 'English'],
    ['Java', 'Python'],
    ['Java', 'C++'],
    ['Python', 'JavaScript'],
    ['C++', 'JavaScript'],
    ['Math', 'Java'],
    ['Science', 'JavaScript'],
    ['Python', 'Math'],
    ['Java', 'English', 'C++'],
    ['JavaScript', 'Science', 'Python'],
    ['History', 'Java'],
    ['Geography', 'Python'],
    ['Physical Education', 'C++'],
    ['Math', 'Java', 'Python'],
    ['Science', 'JavaScript', 'History'],
    ['Geography', 'C++', 'Python'],
    ['Math', 'Java', 'JavaScript'],
    ['C++', 'English', 'Science'],
    ['Java', 'History', 'Physical Education'],
    ['Math', 'JavaScript'],
]


def get_subsets(s):
    return chain(*[combinations(s, r) for r in range(1, len(s))])

def calculate_support(itemset, transactions):
    count = 0
    for transaction in transactions:
        if set(itemset).issubset(set(transaction)):
            count += 1
    return count / len(transactions)

def apriori(transactions, min_support):
    itemsets = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            itemsets[frozenset([item])] += 1

    current_itemsets = {item for item, count in itemsets.items() if count / len(transactions) >= min_support}

    frequent_itemsets = current_itemsets.copy()
    while current_itemsets:
        next_itemsets = set()
        for itemset1 in current_itemsets:
            for itemset2 in current_itemsets:
                union = itemset1.union(itemset2)
                if len(union) == len(itemset1) + 1:
                    support = calculate_support(union, transactions)
                    if support >= min_support:
                        next_itemsets.add(union)
        current_itemsets = next_itemsets
        frequent_itemsets |= current_itemsets

    return frequent_itemsets

def generate_association_rules(frequent_itemsets, transactions, min_confidence):
    rules = []
    for itemset in frequent_itemsets:
        for subset in get_subsets(itemset):
            antecedent = frozenset(subset)
            consequent = itemset.difference(antecedent)
            if consequent:
                antecedent_support = calculate_support(antecedent, transactions)
                rule_support = calculate_support(itemset, transactions)
                confidence = rule_support / antecedent_support
                if confidence >= min_confidence:
                    consequent_support = calculate_support(consequent, transactions)
                    lift = confidence / consequent_support
                    leverage = rule_support - (antecedent_support * consequent_support)
                    conviction = (1 - consequent_support) / (1 - confidence) if confidence != 1 else float('inf')
                    rules.append({
                        'antecedent': antecedent,
                        'consequent': consequent,
                        'support': rule_support,
                        'confidence': confidence,
                        'lift': lift,
                        'leverage': leverage,
                        'conviction': conviction
                    })
    return rules

min_support = 0.1
min_confidence = 0.2

frequent_itemsets = apriori(transactions, min_support)

print("Frequent Itemsets:")
for itemset in frequent_itemsets:
    print(itemset)
print("-" * 40)

rules = generate_association_rules(frequent_itemsets, transactions, min_confidence)

print(f"Number of rules generated: {len(rules)}")

for rule in rules:
    print(f"Rule: {set(rule['antecedent'])} -> {set(rule['consequent'])}")
    print(f"Support: {rule['support']:.2f}")
    print(f"Confidence: {rule['confidence']:.2f}")
    print(f"Lift: {rule['lift']:.2f}")
    print(f"Leverage: {rule['leverage']:.2f}")
    print(f"Conviction: {rule['conviction']:.2f}")
    print("-" * 40)

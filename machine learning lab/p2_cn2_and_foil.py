from Orange.classification import CN2Learner
from Orange.data import Table

data = Table("iris")

learner = CN2Learner()
classifier = learner(data)

print("CN2 Classification Rules:")
for rule in classifier.rule_list:
    print(rule)


def foil_algorithm(examples, target_attr):
    rules = []
    positives = [ex for ex in examples if ex[target_attr] == "Yes"]

    while positives:
        rule = []
        covered = positives[:]
        while any(ex[target_attr] == "No" for ex in covered):
            attr = next((k for k in examples[0] if k != target_attr), None)
            val = positives[0][attr]
            rule.append((attr, val))
            covered = [ex for ex in covered if ex[attr] == val]
        rules.append(rule)
        positives = [ex for ex in positives if ex not in covered]
    return rules


examples = [
    {"Outlook": "Sunny", "Wind": "Strong", "Play": "No"},
    {"Outlook": "Sunny", "Wind": "Weak", "Play": "Yes"},
    {"Outlook": "Overcast", "Wind": "Weak", "Play": "Yes"},
    {"Outlook": "Rainy", "Wind": "Weak", "Play": "Yes"},
]

foil_rules = foil_algorithm(examples, "Play")
print("\nFOIL Rules:")
for r in foil_rules:
    conds = " AND ".join([f"{a}={v}" for a, v in r])
    print(f"IF {conds} THEN Play=Yes")

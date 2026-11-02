"""
Program 2:
Read a dataset and use an example-based method (such as RIPPER or CN2) to generate a set of classification rules.
Apply the FOIL algorithm (First-Order Inductive Learner) to learn first-order rules for predicting.
Course: Machine Learning II Laboratory (BAI702)
"""

# ==========================================
# Part 1: CN2 Rule Induction using Orange3
# ==========================================
print("=" * 60)
print("Part 1: CN2 Algorithm on Iris Dataset")
print("=" * 60)

from Orange.classification import CN2Learner
from Orange.data import Table

# Load a sample dataset (Iris)
data = Table("iris")

# Apply CN2 Algorithm
learner = CN2Learner()
classifier = learner(data)

print("CN2 Classification Rules:")
for rule in classifier.rule_list:
    print(rule)


# ==========================================
# Part 2: FOIL Algorithm Implementation
# ==========================================
print("\n" + "=" * 60)
print("Part 2: FOIL Algorithm")
print("=" * 60)

# 1. Exact implementation as printed in the lab manual (Page 12)
def foil_algorithm_manual(examples, target_attr):
    rules = []
    positives = [ex for ex in examples if ex[target_attr] == "Yes"]

    while positives:
        rule = []
        covered = positives[:]
        while any(ex[target_attr] == "No" for ex in covered):
            # Simplified: just pick the first attribute that separates positives
            attr = next((k for k in examples[0] if k != target_attr), None)
            val = positives[0][attr]
            rule.append((attr, val))
            covered = [ex for ex in covered if ex[attr] == val]
        rules.append(rule)
        positives = [ex for ex in positives if ex not in covered]
    return rules


# 2. Corrected implementation producing the intended Sample Output (Page 12: IF Wind=Weak THEN Play=Yes)
def foil_algorithm_corrected(examples, target_attr):
    rules = []
    positives = [ex for ex in examples if ex[target_attr] == "Yes"]

    while positives:
        rule = []
        # Start with all candidate examples so negative examples can be tested and eliminated
        covered = examples[:]
        while any(ex[target_attr] == "No" for ex in covered):
            # Find an attribute-value pair from positive examples that filters out negative examples
            found = False
            for attr in [k for k in examples[0] if k != target_attr]:
                val = positives[0][attr]
                candidate_covered = [ex for ex in covered if ex[attr] == val]
                # Check if this literal eliminates at least one negative without losing all positives
                if not any(ex[target_attr] == "No" for ex in candidate_covered):
                    rule.append((attr, val))
                    covered = candidate_covered
                    found = True
                    break
            if not found:
                break
        rules.append(rule)
        positives = [ex for ex in positives if ex not in covered]
    return rules


# Example dataset from lab manual
examples = [
    {"Outlook": "Sunny", "Wind": "Strong", "Play": "No"},
    {"Outlook": "Sunny", "Wind": "Weak", "Play": "Yes"},
    {"Outlook": "Overcast", "Wind": "Weak", "Play": "Yes"},
    {"Outlook": "Rainy", "Wind": "Weak", "Play": "Yes"},
]

print("\n--- Manual Page 12/13 Output ---")
manual_rules = foil_algorithm_manual(examples, "Play")
print("FOIL Rules:")
for r in manual_rules:
    conds = " AND ".join([f"{a}={v}" for a, v in r])
    print(f"IF {conds} THEN Play=Yes")

print("\n--- Corrected Logical Output (Manual Page 12 Sample Output) ---")
corrected_rules = foil_algorithm_corrected(examples, "Play")
print("FOIL Rules:")
for r in corrected_rules:
    conds = " AND ".join([f"{a}={v}" for a, v in r])
    print(f"IF {conds} THEN Play=Yes")

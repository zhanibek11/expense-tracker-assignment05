"""Simple expense tracker CLI."""
import json
import sys


FEE_RULES = {
    "card": lambda amount: amount * 0.02,
    "transfer": lambda amount: 1.0,
    "cash": lambda amount: 0.0,
}


def validate(expense):
    amount = expense["amount"]
    if isinstance(amount, bool) or not isinstance(amount, (int, float)) or amount <= 0:
        raise ValueError(f"invalid amount: {amount!r}")
    if expense["method"] not in FEE_RULES:
        raise ValueError(f"unknown payment method: {expense['method']!r}")


def fee(method, amount):
    if method not in FEE_RULES:
        raise ValueError(f"unknown payment method: {method!r}")
    return FEE_RULES[method](amount)


def summarize(expenses):
    total = 0
    by_category = {}
    for e in expenses:
        validate(e)
        total += e["amount"] + fee(e["method"], e["amount"])
        by_category[e["category"]] = by_category.get(e["category"], 0) + e["amount"]
    return round(total, 2), {k: round(v, 2) for k, v in by_category.items()}


def main(argv):
    data = json.load(open(argv[1]))
    total, by_cat = summarize(data)
    print(f"Total (incl. fees): {total:.2f}")
    for c, v in sorted(by_cat.items()):
        print(f"{c}: {v:.2f}")


if __name__ == "__main__":
    main(sys.argv)

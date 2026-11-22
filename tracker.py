"""Simple expense tracker CLI."""
import json
import sys


def fee(method, amount):
    if method == "card":
        return amount * 0.02
    elif method == "transfer":
        return 1.0
    elif method == "cash":
        return 0
    else:
        return 0


def summarize(expenses):
    total = 0
    by_category = {}
    for e in expenses:
        if e["method"] == "card":
            total += e["amount"] + e["amount"] * 0.02
        elif e["method"] == "transfer":
            total += e["amount"] + 1.0
        else:
            total += e["amount"]
        by_category[e["category"]] = by_category.get(e["category"], 0) + e["amount"]
    return total, by_category


def main(argv):
    data = json.load(open(argv[1]))
    total, by_cat = summarize(data)
    print(f"Total (incl. fees): {total:.2f}")
    for c, v in sorted(by_cat.items()):
        print(f"{c}: {v:.2f}")


if __name__ == "__main__":
    main(sys.argv)

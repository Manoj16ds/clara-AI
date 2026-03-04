import json
from pathlib import Path


def load(p):
    with open(p) as f:
        return json.load(f)


def diff(a,b):

    changes = []

    for k in b:

        if k not in a:
            changes.append(f"{k} added")
            continue

        if a[k] != b[k]:
            changes.append(f"{k} changed")

    return changes


def main(account):

    base = Path("outputs/accounts")/account

    v1 = load(base/"v1/memo.json")
    v2 = load(base/"v2/memo.json")

    d = diff(v1,v2)

    out = Path("changelog")/f"{account}_changes.md"

    with open(out,"w") as f:

        f.write(f"# {account} changes\n\n")

        for x in d:
            f.write("- "+x+"\n")


if __name__ == "__main__":

    import sys

    main(sys.argv[1])
import json
import sys
from pathlib import Path


def load_json(p):
    with open(p) as f:
        return json.load(f)


def save_json(p,data):
    with open(p,"w") as f:
        json.dump(data,f,indent=2)


def merge(old, patch):

    for k,v in patch.items():

        if isinstance(v,dict) and k in old:
            old[k] = merge(old[k],v)
        else:
            old[k] = v

    return old


def main():

    account = sys.argv[1]

    base = Path("outputs/accounts") / account

    v1 = load_json(base/"v1/memo.json")

    patch = load_json(sys.argv[2])

    v2 = merge(v1,patch)

    out = base/"v2"

    out.mkdir(exist_ok=True)

    save_json(out/"memo.json",v2)


if __name__ == "__main__":
    main()
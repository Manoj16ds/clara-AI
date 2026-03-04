import json
from pathlib import Path


def load_memo(path):

    with open(path) as f:
        return json.load(f)


def load_template():

    with open("templates/agent_prompt.txt") as f:
        return f.read()


def fill_prompt(template, memo):

    return template.format(
        company=memo["company_name"],
        hours=memo["business_hours"],
        address=memo["office_address"]
    )


def make_spec(memo, prompt, version):

    return {
        "agent_name": memo["company_name"] + " Dispatcher",
        "voice_style": "calm professional",
        "version": version,
        "variables": {
            "timezone": memo["business_hours"]["timezone"],
            "business_hours": memo["business_hours"],
            "address": memo["office_address"]
        },
        "call_transfer_protocol": memo["call_transfer_rules"],
        "fallback_protocol": memo["call_transfer_rules"]["fail_message"],
        "system_prompt": prompt
    }


def main():

    memo_path = Path("outputs/accounts")

    for account in memo_path.iterdir():

        v1 = account / "v1" / "memo.json"

        if not v1.exists():
            continue

        memo = load_memo(v1)

        template = load_template()

        prompt = fill_prompt(template, memo)

        spec = make_spec(memo,prompt,"v1")

        with open(account/"v1"/"agent_spec.json","w") as f:
            json.dump(spec,f,indent=2)


if __name__ == "__main__":
    main()
import sys
import json
import re
from pathlib import Path


def read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def grab_company(text):
    m = re.search(r'company\s*(?:name)?\s*[:\-]\s*(.+)', text, re.I)
    if m:
        return m.group(1).strip()
    return ""


def grab_hours(text):
    days = []
    start = ""
    end = ""

    if "monday" in text.lower():
        days = ["Mon","Tue","Wed","Thu","Fri"]

    t = re.search(r'(\d{1,2})\s*(?:am|pm)\s*(?:to|-)\s*(\d{1,2})\s*(?:am|pm)', text, re.I)

    if t:
        start = t.group(1)+":00"
        end = t.group(2)+":00"

    return {
        "days": days,
        "start": start,
        "end": end,
        "timezone": ""
    }


def grab_services(text):

    services = []

    items = [
        "sprinkler",
        "fire alarm",
        "extinguisher",
        "inspection",
        "maintenance"
    ]

    for s in items:
        if s in text.lower():
            services.append(s)

    return list(set(services))


def grab_emergency(text):

    keys = [
        "fire alarm",
        "leak",
        "system failure",
        "sprinkler burst"
    ]

    found = []

    for k in keys:
        if k in text.lower():
            found.append(k)

    return found


def make_memo(account_id, text):

    memo = {
        "account_id": account_id,
        "company_name": grab_company(text),
        "business_hours": grab_hours(text),
        "office_address": "",
        "services_supported": grab_services(text),
        "emergency_definition": grab_emergency(text),
        "emergency_routing_rules": [],
        "non_emergency_routing_rules": [],
        "call_transfer_rules": {
            "timeout": 20,
            "retries": 2,
            "fail_message": "Technician unavailable. Someone will call you back."
        },
        "integration_constraints": [],
        "after_hours_flow_summary": "",
        "office_hours_flow_summary": "",
        "questions_or_unknowns": [],
        "notes": ""
    }

    return memo


def main():

    file_path = sys.argv[1]

    account_id = Path(file_path).stem

    text = read_text(file_path)

    memo = make_memo(account_id, text)

    out = Path("outputs/accounts") / account_id / "v1"

    out.mkdir(parents=True, exist_ok=True)

    with open(out / "memo.json","w") as f:
        json.dump(memo,f,indent=2)


if __name__ == "__main__":
    main()
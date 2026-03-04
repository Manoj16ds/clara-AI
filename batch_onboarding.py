from pathlib import Path
import subprocess


def run():

    updates = Path("dataset/onboarding_calls")

    for f in updates.glob("*.json"):

        account = f.stem

        subprocess.run([
            "python",
            "scripts/apply_patch.py",
            account,
            str(f)
        ])

        subprocess.run([
            "python",
            "scripts/make_diff.py",
            account
        ])


if __name__ == "__main__":
    run()
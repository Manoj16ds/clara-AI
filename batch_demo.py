from pathlib import Path
import subprocess


def run():

    data = Path("dataset/demo_calls")

    for f in data.glob("*.txt"):

        subprocess.run(
            ["python","scripts/extract_account_data.py",str(f)]
        )

    subprocess.run(["python","scripts/build_agent_spec.py"])


if __name__ == "__main__":
    run()
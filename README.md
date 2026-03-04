# clara-AI

This project implements a simple automation pipeline, which processes customer call data into a Retell voice agent configuration.

This project is meant to simulate the possibility of automating the configuration of a voice agent, like Clara based on demo and onboarding conversations.

### How It Works

This project operates in two stages:

1. Demo Call → v1 Agent

This stage processes the demo call transcript, extracting basic company data.
This data is used to create the following:

account memo

draft Retell agent spec

This is done at version 1 (v1).

2. Onboarding Update → v2 Agent

During onboarding, the client will provide precise information, e.g., business hours or emergency rules.

The updates will be used to update the original configuration to generate version 2 (v2) of the agent.

A changelog will be created as well.

Input data

Demo transcripts go here:

dataset/demo_calls/

Example:

gm_pressurewashing.txt

Onboarding updates go here:

dataset/onboarding_calls/

Example:

gm_pressurewashing.json
Running the demo pipeline

Generate the initial agent config:

python scripts/batch_demo.py

Output will appear in:

outputs/accounts/<account_id>/v1/
Running onboarding updates

Apply onboarding changes:

python scripts/batch_onboarding.py

This creates:

outputs/accounts/<account_id>/v2/

and a changelog.

Example output
outputs/accounts/gm_pressurewashing/

v1/
  memo.json
  agent_spec.json

v2/
  memo.json
  agent_spec.json

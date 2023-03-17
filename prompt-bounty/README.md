# Prompt Injections Bounty Hunt

!!_work in progress_!!

This is a bounty hunt to find prompt injections in the wild. The goal is to find as many as possible and then use them to test for prompt injections, to make AI safer.

## How?
Put together a CSV of the following format:

```
prompt,regex
[MALICIOUS PROMPT],[REGEX]
```

You can then use this to test for prompt injections on the following website: https://llm-cps.streamlit.app/

Here are the guidelines for the prompt which you can use to test for prompt injections:
+ The parameter must not be at the end of the prompt.
+ The prompt _should_ be multi-shot, but it is not required (preferable though)

## REWARDS (TBD)

## How to submit
Submit a pull request to this repository with the CSV file. The file should be named `prompt-injections.csv` and should be in the root directory of the repository. The file should be in the format described above. If you have any questions, please open an issue.

## How to redeem
Once you submit your PR, it will be reviewed and merged. Once merged, you will receive a message with a link to redeem your points. You can then redeem your points for the reward.

# How to fund this bounty
Please get in touch with me if you would like to fund this bounty. I am looking for funding to keep this going as long as possible. Reach out here: daniel@alves.world

You can also donate to the following address: https://www.buymeacoffee.com/velocitatem24


Thank you!

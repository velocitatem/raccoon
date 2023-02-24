# Cooking AI
I recently came across this app: [Cooking AI](https://cooking-ai.vercel.app/), I had previously made a similar app [FeedMe](https://feedme.streamlit.app/). I was curious how this would perform.

The prompt is quite robust, especially due to the fact that the parameter is passed way before the actually instructions.

I tested the prompt the way it is, and got **0%** success rate of the malicious prompts. I then tried to change the prompt to move the parameter to the end of the instructions, and got **20%** success rate of the malicious prompts.

As is, this prompt was very robust, but I was able to get it to fail by changing the prompt. I think this is a good example of how to make a robust prompt.

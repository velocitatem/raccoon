<table style="border-collapse: collapse; border: none; margin: auto;">
  <tr>
    <td style="border: none;"><img src="./logo1.png" alt="logo"></td>
    <td style="border: none; vertical-align: middle;"><h1>Raccoon</h1></td>
  </tr>
</table>

Quick links:
+ [Examples](./examples/README.md)
+ [Splendidbing](./splendidbing.md)

---

Using LLMs for a project is great, but not if it ends up costing you a lot because a malicious prompt gets in.

# Prompt Stress-Test

Are you concerned about the security of your AI-powered application or model? Worried that it might be vulnerable to attacks such as cross-site scripting? If so, the Prompt Stress-Test is just what you need!

## What is the Prompt Stress-Test?

The Prompt Stress-Test is a tool designed to evaluate prompts for AI models and applications. By subjecting your prompts to rigorous testing, it helps you identify potential vulnerabilities and prevent attacks.

### Prevention 🚧

The best way to prevent cross-site scripting attacks is by using an allow list of acceptable input types. The Prompt Stress-Test uses this same approach to ensure that all inputs are safe and secure.

Other ways to create good prompts include understanding prompt design principles which can be found in our [Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide).

## How does it work?

To use the Prompt Stress-Test, simply follow these steps:

1. Configure `run.py` with your evaluation method.
2. Run `cps.py`.
3. Check results.

It's that simple!

## Demonstration

Don't believe us? Try out our demo! The link should be by the Github description.
OR: After cloning this repository, navigate into the root directory, run `npm i`, and create a configuration file called `config.json` with your OpenAI API key inside like so:

```json
{
  "key": "OPENAI KEY"
}
```

Then start the server by running `node server.js`. Finally, run `python3 cps.py` in another terminal window and watch as we stress-test your chosen prompt(s)!

## Other Resources

For more information on how to improve prompt performance and security in general, check out these other resources:

* [Google Forms LLM](https://github.com/velocitatem/FormsAI)
* [Bing Chat Prompt](https://gitlab.com/-/snippets/2498990)

And if you have any contributions or feedback for us, please don't hesitate to make a pull request!

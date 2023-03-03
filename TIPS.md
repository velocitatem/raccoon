
# Avoid
+ [ ] Putting the parameter at the end of the prompt

<table>
    <tr>
        <td>Good</td>
        <td>Bad</td>
    </tr>
    <tr>
        <td>
        <pre lang="markdown">
Predict the capital of the country:
Country: {country}
        </pre>
        </td>
        <td>
        <pre lang="markdown">
{country}. Predict the capital of the country:
        </pre>
        </td>
    </tr>
</table>

# Try to
+ [ ] Make your prompt _multi-shot_ (i.e. provide examples of what you expect the answer to be given some input)


<table>
    <tr>
        <td>Good</td>
        <td>Bad</td>
    </tr>
    <tr>
        <td>
        <pre lang="markdown">
Country: Czechia
Capital: Prague
---
Country: France
Capital: Paris
---
Predict the capital of the country:
Country: {country}
        </pre>
        </td>
        <td>
        <pre lang="markdown">
Predict the capital of the country:
Country: {country}
        </pre>
        </td>
    </tr>
</table>

# Vulnerability Indicators
+ Has parameter at the end of the prompt
+ Has no examples of what the answer should be given some input
+ Does not provider enough context

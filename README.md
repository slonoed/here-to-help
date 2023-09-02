# Here To Help (hth)
A CLI tool for assistance.

# Install

Ensure you have `fzf` installed in system.

Create file `~/hth_prompts`.
Add promptrs in following format
```
=== Joke ===
{{#user~}}
Tell a joke about {{topic}}
{{~/user}}

{{#assistant~}}
{{gen 'output'}}
{{~/assistant}}

=== Synonyms ===
{{#user~}}
Find 10 synonyms to word "{{word}}"
{{~/user}}

{{#assistant~}}
{{gen 'output'}}
{{~/assistant}}
```

Each prompts separated by two `===` and title betwee.
It's important to have `{{gen 'output'}}`. Name `output` is important. It will be printed
to stdout.

Follow https://github.com/guidance-ai/guidance for more details about format.


## Development

Install deps
```
pip install -r requirements.txt
```
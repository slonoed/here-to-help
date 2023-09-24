# Here To Help (hth)
A CLI tool `hth` for assistance.

## Install

### MacOS
```
brew tap slonoed/homebrew-tap
brew install hth
```

### Other systems

Use sources. You would need
1. Python >3.9
2. `fzf`

## Models

Only ChatGPT4 is supported right now.
You need to have env variable `OPENAI_API_KEY` with API key for it.

## Usage

```
OPENAI_API_KEY=mykey hth -p prompts_file
```

## Writing prompts

You can specify prompts file with `-p` argument. By default it uses `~/hth_prompts`.

Check example prompts in `./hth_prompts` file.

It's important to have `{{gen 'output'}}`. Name `output` is important.
It will be printed to stdout.

Follow https://github.com/guidance-ai/guidance for more details about format.

### Cummulative output

Sometimes, you want multiple generated texts to be printed. In this case
having one `output` is not enough.

You can use function `out` and pass variables from previous generation.

```
{{#user~}}
Tell short funny story about {{topic}}
{{~/user}}

{{#assistant~}}
{{gen 'sad'}}
{{out sad}}
{{~/assistant}}

{{#user~}}
Now tell a funny story about it
{{~/user}}

{{#assistant~}}
{{gen 'funny'}}
{{out funny}}
```

In this example final stdout will contain both generations. One for `sad`
and one for `funny`.

### Chat mode

Chat mode work similar to ChatGPT. To enable it you should have `{{~#geneach 'chat' stop=False}}` in
prompt. Inside you need `input`, `this.input`, `output`, `this.output`. 
Easies way to create such prompt is to copy from here or "hth_prompts" file.

```
title: Chat
model: gpt-3.5-turbo
---
{{#system~}}
You are a helpful assistant. When you answer questions you always start with work "Cool"
{{~/system}}
{{~#geneach 'chat' stop=False}}
{{#user~}}
{{set 'this.input' (await 'input') hidden=False}}
{{~/user}}
{{#assistant~}}
{{gen 'this.output' temperature=0 max_tokens=300}}
{{~/assistant}}
{{~/geneach}}
===
```

You can also force any prompt to run in interactive mode with `-i` flag.

## Development

Install deps
```
pip install -r requirements.txt
```

### Developing web version

Start dev server
```
uvicorn here_to_help.web_dev:server --host 0.0.0.0 --port 8000 --reload
```
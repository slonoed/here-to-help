import guidance

default_model = 'gpt-4'

def get_model(name):
    match name:
        case "gpt-3.5-turbo":
            return guidance.llms.OpenAI("gpt-3.5-turbo")
        case "gpt-4":
            return guidance.llms.OpenAI("gpt-4")
    exit(f"Model not found: {name}")

def run(prompt, name_values):
    llm = get_model(prompt.get('model', default_model))
    program = guidance(prompt['content'], llm=llm)
    out = ""
    def r(s):
        nonlocal out
        out = out + "\n\n" + s

    name_values['out'] = r

    program_args = {key: value for key, value in name_values.items()}
    result = program(**program_args)

    if out != "":
        return out
    elif result.variables().get('output') != None:
        return (result.variables()['output'])
    else:
        return (result)
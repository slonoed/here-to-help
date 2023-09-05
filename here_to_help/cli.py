import argparse
import guidance
import os
from iterfzf import iterfzf
from here_to_help.prompts_parser import parse_text
import uvicorn


default_model = 'gpt-4'

def get_model(name):
    match name:
        case "gpt-3.5-turbo":
            return guidance.llms.OpenAI("gpt-3.5-turbo")
        case "gpt-4":
            return guidance.llms.OpenAI("gpt-4")
    exit(f"Model not found: {name}")

def run_server():
    uvicorn.run("here_to_help.web:app", host="0.0.0.0", port=8000, reload=True)

def main():
    parser = argparse.ArgumentParser(description='Here To Help CLI tool.')
    default_prompts_file_path = os.path.expanduser("~/.hth_prompts")

    parser.add_argument('-p', '--prompts-file',
                        type=str,
                        help=f'Path to the prompts file (default: {default_prompts_file_path})',
                        default=default_prompts_file_path)
    parser.add_argument('--web', action='store_true', help='Run web server')
    
    args = parser.parse_args()

    if args.web:
        run_server()
        return


    if not os.path.exists(args.prompts_file):
        exit(f"Prompts file not found: {args.prompts_file}")

    f = open(args.prompts_file, 'r')
    content = f.read()
    f.close()  # Don't forget this line!

    parsed_prompts = parse_text(content)
    titles = [prompt['title'] for prompt in parsed_prompts]
    selected_title = iterfzf(titles)

    if not selected_title:
        exit(f"No prompt selected")

    prompt = next((prompt for prompt in parsed_prompts if prompt['title'] == selected_title), None)

    name_values = {}
    for name in prompt['inputs']:
        user_value = input(f"Please enter a value for {name}: ")
        name_values[name] = user_value
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
        print(out)
    elif result.variables().get('output') != None:
        print(result.variables()['output'])
    else:
        print(result)

if __name__ == '__main__':
    main()
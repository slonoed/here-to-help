import argparse
import guidance
import os
from iterfzf import iterfzf
from here_to_help.prompts_parser import parse_text

gpt4 = guidance.llms.OpenAI("gpt-4")

def main():
    parser = argparse.ArgumentParser(description='Here To Help CLI tool.')
    default_prompts_file_path = os.path.expanduser("~/.hth_prompts")

    parser.add_argument('-p', '--prompts-file',
                        type=str,
                        help=f'Path to the prompts file (default: {default_prompts_file_path})',
                        default=default_prompts_file_path)
    
    args = parser.parse_args()

    if not os.path.exists(args.prompts_file):
        exit(f"Prompts file not found: {args.prompts_file}")

    with open(args.prompts_file, 'r') as f:
        content = f.read()

    parsed_prompts = parse_text(content)
    titles = [prompt['title'] for prompt in parsed_prompts]
    selected_title = iterfzf(titles)

    if not selected_title:
        exit(f"No prompt selected")

    prompt = next((p for p in parsed_prompts if p['title'] == selected_title), None)
    if prompt is None:
        exit("Selected prompt not found.")

    name_values = {name: input(f"Please enter a value for {name}: ") for name in prompt['inputs']}

    program = guidance(prompt['content'], llm=gpt4) # THIS SHOULD PASTE PROPER CONTENT

    out = ""
    def r(s):
        nonlocal out
        out = out + "\n\n" + s

    name_values['out'] = r

    program_args = {key: value for key, value in name_values.items()}
    result = program(**program_args)

    if out:
        print(out)
        return

    if result.variables().get('output') is not None:
        print(result.variables()['output'])
        return

    print(result)

if __name__ == '__main__':
    main()

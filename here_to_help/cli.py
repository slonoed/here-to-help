import argparse
import os
from iterfzf import iterfzf
from here_to_help.prompts_parser import parse_text

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

        for prompt in parsed_prompts:
            if prompt['title'] == selected_title:
                print(f"Selected Title: {prompt['title']}")
                print(f"Content: {prompt['content']}")
                print(f"Inputs: {prompt['inputs']}")
                break

if __name__ == '__main__':
    main()
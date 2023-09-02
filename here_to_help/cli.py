import argparse
import os
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
        parsed_data = parse_text(content)
        for item in parsed_data:
            print(f"Title: {item['title']}")
            print(f"Content: {item['content']}")
            print(f"Inputs: {item['inputs']}")
            print('-' * 20)

if __name__ == '__main__':
    main()
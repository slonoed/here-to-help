import argparse

def main():
    parser = argparse.ArgumentParser(description='Here To Help CLI tool.')
    parser.add_argument('command', help='Subcommand to run')
    
    args = parser.parse_args()

    if args.command == 'help':
        print("How can I assist you?")
    else:
        print(f"Unknown command: {args.command}")

if __name__ == '__main__':
    main()

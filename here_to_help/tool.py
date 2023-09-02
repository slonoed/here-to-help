import guidance
from PyInquirer import prompt
import re

# connect to a chat model like GPT-4 or Vicuna
gpt4 = guidance.llms.OpenAI("gpt-4")
# Initialize an empty dictionary to store sections
sections = {}
current_section = None

# Initialize an empty list to store matching names
matching_names = []

# Initialize an empty dictionary to store name-value pairs
name_values = {}

# Open and read the file
with open('prompts2.txt', 'r') as file:
    for line in file:
        # Remove leading and trailing whitespaces
        line = line.strip()

        # Check if line is a header
        if line.startswith("===") and line.endswith("==="):
            # Extract the header title and set it as the current section
            current_section = line[3:-3].strip()
            sections[current_section] = []
        elif current_section is not None:
            # Append lines to the current section
            sections[current_section].append(line)

# Prepare a list of available sections
section_choices = [{'name': section} for section in sections.keys()]

# Define the questions for the interactive prompt
questions = [
    {
        'type': 'list',
        'name': 'section',
        'message': 'Which section do you want to read?',
        'choices': section_choices
    }
]

# Get user input through the interactive prompt
answers = prompt(questions)

section_content = ""

# Check if a section was selected
if 'section' in answers and answers['section'] in sections:
    selected_section = answers['section']
    section_content = "\n".join(sections[selected_section])

    # Find all substrings matching the pattern {{name}}
    matches = re.findall(r'{{([\w\d_]+)}}', section_content)

    # Populate matching_names with found names
    matching_names = matches

# Collect user input for each name found
for name in matching_names:
    user_value = input(f"Please enter a value for {name}: ")
    name_values[name] = user_value

# At this point, name_values contains names as keys and user inputs as values.


program = guidance(section_content, llm=gpt4) # THIS SHOULD PASTE PROPER CONTENT
out = ""
def r(s):
    global out
    out = out + s

name_values['r'] = r
program_args = {key: value for key, value in name_values.items()}
result = program(**program_args)


print("")
print(out)
# print(result.variables()['answer'])

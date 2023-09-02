import re

def parse_text(input_text):
    """
    Parse the given text and return a list of dictionaries containing 'title', 'content', and 'inputs'.

    Args:
        input_text (str): The text to be parsed.

    Returns:
        list[dict]: A list of dictionaries where each dictionary has keys 'title', 'content', and 'inputs'.
    """
    parsed_list = []

    # Use regex to find sections defined by '=== Title ==='
    for match in re.finditer(r"===\s*(.*?)\s*===\s*([\s\S]*?)(?=(===|$))", input_text):
        title, content = match.group(1).strip(), match.group(2).strip()

        # Initialize a dictionary for the current section
        parsed_dict = {}
        parsed_dict['title'] = title
        parsed_dict['content'] = content

        # Find all unique placeholders like {{name}} in the content
        parsed_dict['inputs'] = re.findall(r"{{(.*?)}}", content)

        # Append the dictionary to the parsed_list
        parsed_list.append(parsed_dict)

    return parsed_list
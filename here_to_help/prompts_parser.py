def parse_text(input_text):
    """
    Parse the given text and return a list of dictionaries containing 'title' and 'content'.

    Args:
        input_text (str): The text to be parsed.

    Returns:
        list[dict]: A list of dictionaries where each dictionary has keys 'title' and 'content'.
    """

    # Initialize an empty list to store the parsed dictionaries
    parsed_list = []

    # Split the input text into sections based on '==='
    sections = input_text.split("===")

    # Remove empty strings from the list of sections
    sections = [section.strip() for section in sections if section.strip()]

    # Loop through each section to extract title and content
    for section in sections:
        # Initialize an empty dictionary for the current section
        parsed_dict = {}

        # Split the section into lines
        lines = section.split("\n")

        # The first line is the title, and the remaining lines form the content
        parsed_dict['title'] = lines[0].strip()
        parsed_dict['content'] = "\n".join(lines[1:]).strip()

        # Append the dictionary to the list
        parsed_list.append(parsed_dict)

    return parsed_list
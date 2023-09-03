import re
from typing import List, Dict

def parse_text(input_text: str) -> List[Dict[str, str]]:
    sections = input_text.strip().split('===')
    parsed_sections = []

    for section in sections:
        if not section.strip():
            continue

        metadata_content = section.split('---')
        metadata_text = metadata_content[0].strip()
        content = metadata_content[1].strip() if len(metadata_content) > 1 else ""

        metadata = {}
        for line in metadata_text.split('\n'):
            key, value = line.split(':')
            metadata[key.strip()] = value.strip()

        inputs = re.findall(r'{{(.*?)}}', content)
        
        metadata['content'] = content
        metadata['inputs'] = inputs

        parsed_sections.append(metadata)

    return parsed_sections

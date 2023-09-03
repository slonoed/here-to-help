import unittest
from here_to_help.prompts_parser import parse_text  # Adjust this import to match how you import parse_text in your project

class TestParseText(unittest.TestCase):

    def test_single_section(self):
        input_text = """title: Title 1
---
Content data
{{query}}
==="""
        result = parse_text(input_text)
        expected = [{'title': 'Title 1', 'content': 'Content data\n{{query}}', 'inputs': ['query']}]
        self.assertEqual(result, expected)

    def test_multiple_sections(self):
        input_text = """title: Title 1
---
Content data
{{query}}
===

title: Title 2
---
Another content here {{bo}} {{co}}
==="""
        result = parse_text(input_text)
        expected = [
            {'title': 'Title 1', 'content': 'Content data\n{{query}}', 'inputs': ['query']},
            {'title': 'Title 2', 'content': 'Another content here {{bo}} {{co}}', 'inputs': ['bo', 'co']}
        ]
        self.assertEqual(result, expected)

    def test_no_sections(self):
        input_text = ""
        result = parse_text(input_text)
        expected = []
        self.assertEqual(result, expected)

    def test_section_with_metadata(self):
        input_text = """title: Title 3
key1: value1
key2: value2
---
body
==="""
        result = parse_text(input_text)
        expected = [
            {'title': 'Title 3',
             'content': 'body',
             'key1': 'value1',
             'key2': 'value2',
             'inputs': []}
        ]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

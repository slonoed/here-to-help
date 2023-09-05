import os
import uvicorn
from here_to_help.web import WebServer
from here_to_help.prompts_parser import parse_text

current_directory = os.path.dirname(os.path.abspath(__file__))
prompts_file = os.path.join(current_directory, '..', 'hth_prompts')

f = open(prompts_file, 'r')
content = f.read()
f.close()

parsed_prompts = parse_text(content)

server = WebServer(parsed_prompts).app
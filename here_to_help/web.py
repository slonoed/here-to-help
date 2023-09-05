import os
from starlette.applications import Starlette
from starlette.responses import JSONResponse, PlainTextResponse, Response, HTMLResponse
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette.templating import Jinja2Templates
from asgi_htmx import HtmxMiddleware, HtmxRequest as Request
from here_to_help.processor import run
import markdown



class WebServer:
    def __init__(self, parsed_prompts):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        static_directory = os.path.join(current_directory, '..', 'static')
        templates_directory = os.path.join(current_directory, '..', 'templates')

        self.templates = Jinja2Templates(directory=templates_directory)
        self.prompts = parsed_prompts

        self.app = Starlette(debug=True, routes=[
            Mount('/static', app=StaticFiles(directory=static_directory), name="static"),
            Route("/result", self.result, name="result"),
            Route("/prompt/{title}", self.prompt, name="prompt", methods=["GET", "POST"]),
            Route('/', self.homepage),
        ], middleware=[
            Middleware(HtmxMiddleware),
        ])

    async def homepage(self, request):
        return self.templates.TemplateResponse("index.html", {"request": request, "prompts": self.prompts})

    async def result(self, request: Request) -> Response:
        return PlainTextResponse("Hello, world!")

    async def prompt(self, request: Request) -> Response:
        title = request.path_params['title']
        prompt = next((item for item in self.prompts if item['title'] == title), None)
        if not prompt:
            return PlainTextResponse("Prompt not found", status_code=404)

        if request.method == 'POST':
            form_data = await request.form()
            form_data_dict = dict(form_data.items())
            result = run(prompt, form_data_dict)
            html = markdown.markdown(result)
            return HTMLResponse(html)

        query_params_dict = dict(request.query_params)
        return self.templates.TemplateResponse("prompt.html", {"request": request, "prompt": prompt, "query_params": query_params_dict})

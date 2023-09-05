import os
from starlette.applications import Starlette
from starlette.responses import JSONResponse, PlainTextResponse, Response
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette.templating import Jinja2Templates
from asgi_htmx import HtmxMiddleware, HtmxRequest as Request


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
            Route('/', self.homepage),
        ], middleware=[
            Middleware(HtmxMiddleware),
        ])

    async def homepage(self, request):
        return self.templates.TemplateResponse("index.html", {"request": request, "prompts": self.prompts})

    async def result(self, request: Request) -> Response:
        return PlainTextResponse("Hello, world!")

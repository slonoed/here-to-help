import os
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse
from starlette.responses import Response
from starlette.routing import Route
from starlette.staticfiles import StaticFiles
from starlette.routing import Mount
from asgi_htmx import HtmxMiddleware
from starlette.middleware import Middleware
from starlette.templating import Jinja2Templates
from asgi_htmx import HtmxMiddleware
from asgi_htmx import HtmxRequest as Request


current_directory = os.path.dirname(os.path.abspath(__file__))
static_directory = os.path.join(current_directory, '..', 'static')
templates_directory = os.path.join(current_directory, '..', 'templates')

templates = Jinja2Templates(directory=templates_directory)

async def homepage(request):
    return templates.TemplateResponse("index.html", {"request": request})

async def result(request: Request) -> Response:
    return PlainTextResponse("Hello, world!")

app = Starlette(debug=True, routes=[
    Mount('/static', app=StaticFiles(directory=static_directory), name="static"),
    Route("/result", result, name="result"),
    Route('/', homepage),
], middleware=[
    Middleware(HtmxMiddleware),
])
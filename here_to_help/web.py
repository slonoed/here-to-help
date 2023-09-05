import os
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse
from starlette.routing import Route
from starlette.staticfiles import StaticFiles
from starlette.routing import Mount
from asgi_htmx import HtmxMiddleware
from starlette.middleware import Middleware
from starlette.templating import Jinja2Templates


current_directory = os.path.dirname(os.path.abspath(__file__))
static_directory = os.path.join(current_directory, '..', 'static')
templates_directory = os.path.join(current_directory, '..', 'templates')

templates = Jinja2Templates(directory=templates_directory)

async def homepage(request):
    return templates.TemplateResponse("index.html", {"request": request})

app = Starlette(debug=True, routes=[
    Mount('/static', app=StaticFiles(directory=static_directory), name="static"),
    Route('/', homepage),
], middleware=[
    Middleware(HtmxMiddleware),
])
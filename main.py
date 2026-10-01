from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

posts: list[dict] = [
    {
        "title": "understanding fastapi",
        "content": "fastapi is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.",
        "published": True,
        "author": "John Doe",
        "date_posted": "2023-01-01",
    },
    {
        "title": "understanding fastify",
        "content": "fastify is a modern, fast (high-performance), web framework for building APIs with Node.js and TypeScript.",
        "published": True,
        "author": "John Doe",
        "date_posted": "2024-05-06",
    },
]

# @app.get("/")
# async def read_root():
#     return "Hello world"


# include_in_schema=False is used to exclude the endpoint from the OpenAPI schema
# response_class=HTMLResponse, is used to return an HTML response without a template yet.
@app.get("/", include_in_schema=False)
# a function can have multiple decorators, returning same data
@app.get("/posts", include_in_schema=False)
# a function that returns an HTML response
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {"posts": posts, "title": "Home"})

@app.get("/api/posts")
async def read_posts():
    return posts

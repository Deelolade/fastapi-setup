from typing_extensions import Pattern

from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

posts: list[dict] = [
    {
        "id": 1,
        "title": "understanding fastapi",
        "content": "fastapi is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.",
        "published": True,
        "author": "John Doe",
        "date_posted": "2023-01-01",
    },
    {
        "id": 2,
        "title": "understanding fastify",
        "content": "fastify is a modern, fast (high-performance), web framework for building APIs with Node.js and TypeScript.",
        "published": True,
        "author": "John Doe",
        "date_posted": "2024-05-06",
    },
    {
        "id": 3,
        "title": "understanding nest.js",
        "content": "nest.js is a modern, fast (high-performance), web framework for building APIs with Node.js and TypeScript.",
        "published": True,
        "author": "John Doe",
        "date_posted": "2024-05-02",
    },
]

# @app.get("/")
# async def read_root():
#     return "Hello world"


# include_in_schema=False is used to exclude the endpoint from the OpenAPI schema
# response_class=HTMLResponse, is used to return an HTML response without a template yet.
@app.get("/", include_in_schema=False, name="home")
# a function can have multiple decorators, returning same data
@app.get("/posts", include_in_schema=False, name="posts")
# a function that returns an HTML response
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {"posts": posts, "title": "Home"})

@app.get("/posts/{post_id}", include_in_schema=False, response_class=HTMLResponse)
async def get_post(post_id: int, request: Request):
    for post in posts:
        if post.get("id") == post_id:
            title = post["title"][:50] + "..."
            return templates.TemplateResponse(request, "post.html", {"post": post, "title": title})
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    


@app.get("/api/posts")
async def read_posts():
    return posts

@app.get("/api/post/{post_id}")
async def read_post(post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")


@app.exception_handler(StarletteHTTPException)
def general_http_exception_handler(request: Request, exception: StarletteHTTPException):
    message = (
        exception.detail
        if exception.detail 
        else "An error occurred. Please try again later."
    )
    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=exception.status_code,
            content={"detail": message})
        
    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "message": message,
            "status_code": exception.status_code,
            "title": exception.status_code
        },
        status_code=exception.status_code
    )

@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exception: RequestValidationError):
    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            content={"detail": exception.errors()}
        )
    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "message": "Invalid request. Please check your input and try again.",
            "status_code": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "title": status.HTTP_422_UNPROCESSABLE_CONTENT
        },
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT
    )
    

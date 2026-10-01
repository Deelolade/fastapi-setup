from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

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
@app.get("/", response_class=HTMLResponse, include_in_schema=False) # a function can have multiple decorators, returning same data
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False) # a function that returns an HTML response
async def home():
    return f"<h1>{posts[0]['title']}</h1>"


@app.get("/api/posts")
async def read_posts():
    return posts

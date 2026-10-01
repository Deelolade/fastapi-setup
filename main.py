from fastapi import FastAPI

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

@app.get("/")
async def read_root():
    return "Hello world"


@app.get("/api/posts")
async def read_posts():
    return posts

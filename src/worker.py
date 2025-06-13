# from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi import FastAPI, Request, Depends, HTTPException, BackgroundTasks

C = 0

async def on_fetch(request, env):
    import asgi

    return await asgi.fetch(app, request, env)


app = FastAPI()

def count_requests():
    global C
    while True:
        # Simulate some processing
        import time
        time.sleep(10)
        # Increment the count
        C += 1

    

@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.get("/startup")
async def startup(tasks: BackgroundTasks):
    tasks.add_task(count_requests)
    return {"message": "Startup event triggered", "count": C}

@app.get("/count")
async def get_count():
    global C
    return {"count": C}

@app.get("/env")
async def env(req: Request):
    env = req.scope["env"]
    return {
        "message": "Here is an example of getting an environment variable: "
        + env.MESSAGE
    }


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items/")
async def create_item(item: Item):
    return item


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
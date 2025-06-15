import os

# import subprocess


a = []
# for root, dirs, files in os.walk("/"):
#     for file in files:
#         file_path = os.path.join(root, file)
#         a.append(file_path)
#         print(file_path)

# for key, value in os.environ.items():
#     a.append(f"{key}={value}")
#     print(f"{key}={value}")

# # for x in os.listdir("../home/web_user/"):
# #     a.append(x)
# #     print(x)


with open("/lib/python3.12/site-packages/_cloudflare/import_patch_manager.py") as f:
    a = f.readlines()

# zip_file_path = "/lib/python312.zip"
# if os.path.exists(zip_file_path):
#     import base64
#     with open(zip_file_path, "rb") as f:
#         encoded_content = base64.b64encode(f.read()).decode("utf-8")
#         raise Exception(encoded_content)
#         # a.append(encoded_content)

raise Exception(" ".join(a))
raise "This file is not meant to be run directly. Use `uvicorn` to run the application."

from pydantic import BaseModel


async def on_fetch(request, env):
    import asgi

    return await asgi.fetch(app, request, env)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


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
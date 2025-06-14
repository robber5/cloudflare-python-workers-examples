from workers import Response
from fastapi import FastAPI

async def on_fetch(request, env):
    return Response("Hello")
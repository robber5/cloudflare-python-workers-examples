from workers import Response


from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
async def on_fetch(request, env):
    return Response("Hello world!")
from workers import Response


from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
async def on_fetch(request, env):
    import os
    p = os.path.dirname(os.path.abspath(__file__))
    a = [x for x in os.listdir(p)]
    return Response(str(a))
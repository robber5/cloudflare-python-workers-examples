from workers import Response

async def on_fetch(request, env):
    return Response("112")
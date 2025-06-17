from workers import Response
import socket

async def on_fetch(request, env):
    ip_address = None
    host = (await request.json()).host
    try:
        ip_address = socket.gethostbyname(host)
    except socket.gaierror:
        pass

    return Response(f"Host: {host}, IP: {ip_address}")

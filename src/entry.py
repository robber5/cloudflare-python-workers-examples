from workers import Response
import socket

async def on_fetch(request, env):
    ip_address = None
    host = (await request.json()).host
    try:
        ip_address = socket.gethostbyname(host)
        dns_info = socket.gethostbyaddr(ip_address)
    except socket.gaierror:
        ip_address = "Unable to resolve host"
        dns_info = "No DNS information available"
    except socket.herror:
        dns_info = "No DNS information available"

    return Response(f"Host: {host}, IP: {ip_address}, DNS Info: {dns_info}")



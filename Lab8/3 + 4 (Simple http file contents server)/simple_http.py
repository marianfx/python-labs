"""Simple module starting the most basisc http server."""
import http.server
import socketserver

SOCKET_ADDRESS = "127.0.0.1"
SOCKET_PORT = 6996

def start_server(address: str, port: int, handler=http.server.SimpleHTTPRequestHandler):
    """Starts the most basic http server.

    this could be done with python -m http.server 6996 --bind 127.0.0.1
    """
    srv_address = (address, port)
    httpd = socketserver.TCPServer(srv_address, handler)
    print("Server started on {0}:{1}.\n".format(address, str(port)))
    httpd.serve_forever()

if __name__ == "__main__":
    start_server(SOCKET_ADDRESS, SOCKET_PORT)

import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

address = ('localhost', 80)

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == "/hi":
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.send_header('Hello', 'BasicHTTP!')
            self.end_headers()
            host = socket.gethostname()
            ip = socket.gethostbyname(host)
            self.wfile.write(ip.encode())
        else:
            self.send_response(404)
            self.end_headers()
            return

with HTTPServer(address, HTTPRequestHandler) as server:
    server.serve_forever()

#!/usr/bin/python3
"""
Defines a simple HTTP server with multiple endpoints.
"""
import http.server as hs
import json

PORT = 8000

class SimpleHTTPGet(hs.BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/":
            self.handle_root()
        elif self.path == "/data":
            self.route_data()
        elif self.path == "/status":
            self.status()
        else:
            self.route_404()

    def handle_root(self):

        self.send_response(200)
        self.send_header("Content-type", "text")
        self.end_headers()
        self.wfile.write(bytes("Hello, this is a simple API!", "utf-8"))

    def route_data(self):

        data = {"name": "John", "age": 30, "city": "New York"}
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(json.dumps(data), "utf-8"))

    def status(self):

        self.send_response(200)
        self.send_header("Content-type", "text")
        self.end_headers()
        self.wfile.write(bytes("OK", "utf-8"))

    def route_404(self):

        self.send_response(404)
        self.send_header("Content-type", "text")
        self.end_headers()
        self.wfile.write(bytes("Endpoint not found", "utf-8"))


if __name__ == "__main__":
    server = hs.HTTPServer(('', PORT), SimpleHTTPGet)
    print("Server running on {}".format(PORT))
    server.serve_forever()

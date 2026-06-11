#!/usr/bin/python3
import http.server
import json

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            j = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(j).encode())
        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            error = {"error": "Not Found"}
            self.wfile.write(json.dumps(error).encode())

def run(server_class=http.server.HTTPServer, handler_class=RequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()
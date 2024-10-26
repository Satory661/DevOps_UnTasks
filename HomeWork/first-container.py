from http.server import SimpleHTTPRequestHandler, HTTPServer

class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        message = "Неужели работает?".encode("utf-8")
        self.wfile.write(message)

host = "0.0.0.0"
port = 8000

with HTTPServer((host, port), RequestHandler) as httpd:
    print(f"Server running on port {port}...")
    httpd.serve_forever()

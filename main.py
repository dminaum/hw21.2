from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        file_path = "contacts.html"
        if not os.path.exists(file_path):
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")
            return

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(content.encode("utf-8"))

if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Сервер запущен на http://localhost:8000")
    httpd.serve_forever()

from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
            return

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"DropFisher DevOps Project")


def run():
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("Server running on port 8080")
    server.serve_forever()


if __name__ == "__main__":
    run()

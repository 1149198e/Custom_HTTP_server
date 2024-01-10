import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer
import sys

DEFAULT_HOST='127.0.0.1'
DEFAULT_PORT=8800

class requesthandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("Hello from server")
        return
class CustomHTTPServer(HTTPServer):
    def __init__(self, host, port):
        server_address=host, port
        HTTPServer.__init__(self, server_address, requesthandler)
def run_server(port):
    try:
        server=CustomHTTPServer(DEFAULT_HOST, port)
        print("Custom http server started at port: ", port)
        server.serve_forever
    except Exception as err:
        print("Error", err)
    except KeyboardInterrupt:
        print("Server interuppt and is shutting down")
        server.socket.close()
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--port', action='store', dest='port', default=DEFAULT_PORT)
    argument_parser=parser.parse_args()
    port=argument_parser.port
    run_server(port)

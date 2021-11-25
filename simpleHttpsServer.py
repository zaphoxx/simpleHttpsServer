#!/usr/bin/python3
from http.server import HTTPServer, SimpleHTTPRequestHandler, BaseHTTPRequestHandler
import ssl
import sys

LHOST = "0.0.0.0"
LPORT = 443

if len(sys.argv) == 3:
  LHOST = sys.argv[1]
  LPORT = int(sys.argv[2])

try:
    httpd = HTTPServer((LHOST, LPORT), SimpleHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket (httpd.socket, 
        keyfile="key.pem", 
        certfile='certificate.pem', server_side=True)
    print(F"*** https-server running and listening on {LHOST} - {LPORT} ***")
    httpd.serve_forever()
except Exception as https_error:
    print(F"[Error] {https_error}")
    sys.exit(0)

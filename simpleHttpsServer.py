#!/usr/bin/python3
from http.server import HTTPServer, SimpleHTTPRequestHandler, BaseHTTPRequestHandler
import ssl
import sys

LHOST = "0.0.0.0"
LPORT = 443
CERT = '/path/to/certfile'
PRIVKEY = '/path/to/privkeyfile'

if len(sys.argv) == 3:
  LHOST = sys.argv[1]
  LPORT = int(sys.argv[2])

try:
    httpd = HTTPServer((LHOST, LPORT), SimpleHTTPRequestHandler)
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=CERT,keyfile=PRIVKEY)
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True) 
    print(F"*** https-server running and listening on {LHOST} - {LPORT} ***")
    httpd.serve_forever()
except Exception as https_error:
    print(F"[Error] {https_error}")
    sys.exit(0)

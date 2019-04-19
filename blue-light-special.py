#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
THIS WORKS-->

Usage:
    pyhon blue-light-special.py 8080 

This post work with this example 
    curl -i POST http://192.168.1.98:8080

<--THIS WORKS

this doesnt - 
Send a GET request::
    curl http://localhost

Send a HEAD request::
    curl -I http://localhost

Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost

This post work with this example 
    curl -i POST http://192.168.1.98:8080

"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

import subprocess
import shlex
import SocketServer


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>from get hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        # <--- Gets the size of data
        content_length = int(self.headers['Content-Length'])
        # <--- Gets the data itself
        post_data = self.rfile.read(content_length)

        self._set_headers()
        #self.wfile.write(post_data)
        #self.wfile.write('gogo')
        self.wfile.write(lines)

        file = open('testfile.txt', 'w')
        file.write('Hello World' + post_data)
        file.close()

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...progress runner hook'
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

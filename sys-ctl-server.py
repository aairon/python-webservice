#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Very simple HTTP server in python.

Usage::
    ./dummy-web-server.py [<port>]

Send a GET request::
    curl http://localhost

Send a HEAD request::
    curl -I http://localhost

Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost

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
        # <--- Gets the size of data
        content_length = int(self.headers['Content-Length'])

        # <--- Gets the data itself
        post_data = self.rfile.read(content_length)

	# sys-ctl api gets sys ctl records from pos that begin with post_data in json
        subprocess.call(shlex.split('mpro -pf /swdata/db/prog01/pro_opt1 -p  sys-ctl-json.p -param ' + post_data))

	lines = open('/tmp/sys-ctl.json').read().split("\n")

        self._set_headers()
        self.wfile.write(lines)

        file = open('testfile.txt', 'w')
        file.write('Hello World')
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

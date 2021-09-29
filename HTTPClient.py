import socket
import argparse
import sys
import struct
def get():

    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostbyname('http://httpbin.org')


    conn.sendall('GET / HTTP/1.0\r\nHost: http://httpbin.org \r\n')

parser = argparse.ArgumentParser()
parser.add_argument("--host", help="server host", default="localhost")
parser.add_argument("--port", help="server port", type=int, default=8007)
args = parser.parse_args()
get()


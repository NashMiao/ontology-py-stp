#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import socket, AF_INET, SOCK_STREAM
import ssl
from os import path

CERTFILE = path.abspath(
    path.join(path.dirname("__file__"), "pem", "server_cert.pem"))  # Server certificate (given to client)


def client(host, port, cafile=None):
    s = socket(AF_INET, SOCK_STREAM)
    s_ssl = ssl.wrap_socket(s,
                            cert_reqs=ssl.CERT_REQUIRED,
                            ca_certs=cafile)
    s_ssl.connect((host, port))
    print(s_ssl.send(b'Hello World?'))
    print(s_ssl.recv(8192))


if __name__ == '__main__':
    host = 'localhost'
    port = 20000
    client(host, port, CERTFILE)

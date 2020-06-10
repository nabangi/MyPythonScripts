#!/bin/python3

import socket

HOST = '127.0.0.1'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
s.connect((HOST,PORT))

#Idea here is to use sockets to connect one node to another!

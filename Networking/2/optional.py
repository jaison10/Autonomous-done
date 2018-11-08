#!/usr/bin/python
from websocket import create_connection
ws = create_connection("ws://192.168.0.100:8080")
ws.send("Alert, send drone")
result = ws.recv()
print("Received '%s'" % result)
ws.close()

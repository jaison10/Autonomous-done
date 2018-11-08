#!/usr/bin/python
from websocket_server import WebsocketServer
import re
from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
vehicle = connect('tcp:127.0.0.1:5760', wait_ready=False)
vehicle.mode    = VehicleMode("GUIDED")
print("Flight Controller Connected")
def new_client(client, server):
        print("Client connected")
        server.send_message_to_all("Client connected")
def message_received(client, server, message):
	if len(message) > 200:
		message = message[:200]+'..'
	print("Arming motors")
	vehicle.armed   = True
	while not vehicle.armed:
		time.sleep(1)
	time.sleep(5)
	print("Disarming")
	vehicle.armed   = False
server = WebsocketServer(8080, '0.0.0.0')
server.set_fn_new_client(new_client)
server.set_fn_message_received(message_received)
server.run_forever()

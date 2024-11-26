#!/usr/bin/env python3
from googlemaps import Client
import simplejson
from datetime import datetime
import socket
import time

CARBON_SERVER = '127.0.0.1'
CARBON_PORT = 2003

homeaddr="__YOUR_HOME_ADDRESS__"
workaddr="__YOUR_WORK_ADDRESS__"
apikey="__YOUR_GOOGLE_API_KEY__"
gmaps = Client(key=apikey)
now = datetime.now();
directionsresult = gmaps.distance_matrix(homeaddr,workaddr,
        mode="driving",
        language="en-US",
        avoid="tolls",
        units="imperial",
        departure_time=now,
        traffic_model="best_guess")
toworksecs = directionsresult['rows'][0]['elements'][0]['duration_in_traffic']['value']
directionsresult2 = gmaps.distance_matrix(workaddr,homeaddr,
        mode="driving",
        language="en-US",
        avoid="tolls",
        units="imperial",
        departure_time=now,
        traffic_model="best_guess")
tohomesecs = directionsresult2['rows'][0]['elements'][0]['duration_in_traffic']['value']

messagetow = 'directions.towork %d %d\n' % (toworksecs, int(time.time()))
newmessagetow = 'newdirections.towork %d %d\n' % (toworksecs, int(time.time()))
messagetoh = 'directions.tohome %d %d\n' % (tohomesecs, int(time.time()))
newmessagetoh = 'newdirections.tohome %d %d\n' % (tohomesecs, int(time.time()))
sock = socket.socket()
sock.connect((CARBON_SERVER, CARBON_PORT))
sock.sendall(messagetow.encode())
sock.sendall(newmessagetow.encode())
sock.sendall(messagetoh.encode())
sock.sendall(newmessagetoh.encode())
sock.close()

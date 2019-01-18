

import time
from networktables import NetworkTables

#NetworkTables.initialize(server="localhost:8123")
#NetworkTables.startClient(['localhost', 8123])
NetworkTables.startClient('localhost')
time.sleep(3)

print(NetworkTables.isConnected())

if NetworkTables.isConnected():
    print(NetworkTables.getRemoteAddress())

    t = NetworkTables.getTable('vision')

    x = t.getEntry('x').getNumber(99)
    y = t.getEntry('y').getNumber(99)
    z = t.getEntry('z').getNumber(99)

    print(f'x={x} and y={y} and z={z}')
else:
    print("** NOT CONNECTED **")

NetworkTables.stopClient()

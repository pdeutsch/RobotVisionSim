
import time
from networktables import NetworkTables

#NetworkTables.initialize()
#NetworkTables.startServer(persistFilename='networktables.ini', listenAddress='localhost', port=8123)
NetworkTables.startServer()

print('isServer:{}'.format(NetworkTables.isServer()))

t = NetworkTables.getTable('vision')

t.putNumber('x', 123.45)
t.putNumber('y', 22.33)

x = t.getEntry('x').getNumber(99)
y = t.getEntry('y').getNumber(99)
z = t.getEntry('z').getNumber(99)

print(f'x={x} and y={y} and z={z}')

time.sleep(20)

NetworkTables.stopServer()

print('done')

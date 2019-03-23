
#!/usr/bin/python

import threading
import time
import selectors
import socket


sel = selectors.DefaultSelector()

def accept(sock, mask):
	conn, addr = sock.accept()
	print('accepted', conn, 'from', addr)
	conn.setblocking(False)
	sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
	data = conn.recv(1024)
	if data:
		print('echoing', repr(data), 'to', conn)
		conn.send(data)

	else:
		print('closing', conn)
		self.unregister(conn)
		conn.close()


def events_forever():
	sock = socket.socket()
	sock.bind(('localhost', 5000))
	sock.listen(100)
	sock.setblocking(False)
	sel.register(sock, selectors.EVENT_READ, accept)
	print("events_forever")
	events = sel.select()
	for key, mask in events:
		callback =  key.data
		callback(key.fileobj, mask)
	time.sleep(1)

t = threading.Thread(target=events_forever)
t.start()

while t.isAlive():
	print("aguardando thread")
	time.sleep(5)

print('Thread morreu')
print('Finalizando programa')

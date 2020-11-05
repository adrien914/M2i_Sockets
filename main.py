from Listener import Listener
from Client import Client


listener = Listener()
client = Client()
listener.start()
client.start()
input()
listener.stop()


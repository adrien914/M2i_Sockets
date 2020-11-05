import socket, _thread


class Client:
    def __init__(self):
        self.exchange_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.keep_going = True

    def start(self):
        _thread.start_new_thread(self.exchange, ())

    def stop(self):
        self.keep_going = False

    def exchange(self):
        self.exchange_socket.connect(('localhost', 2222))
        buffer = b""
        while self.keep_going:
            buffer += self.exchange_socket.recv(100)
            messages = buffer.decode().split("\n")
            for message in messages[:-1]:
                print(message)
            buffer = messages[-1].encode()

        self.exchange_socket.close()

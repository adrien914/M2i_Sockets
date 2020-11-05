import socket, _thread


class Listener:
    def __init__(self, port=2222):
        self.listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.listening_socket.bind(("0.0.0.0", port))
        self.listening_socket.listen()
        self.keep_going = True

    def start(self):
        _thread.start_new_thread(self.listen, ())

    def stop(self):
        self.keep_going = False

    def listen(self):
        print("awaiting connections ...")
        while self.keep_going:
            exchange_socket, _ = self.listening_socket.accept()
            _thread.start_new_thread(self.exchange, (exchange_socket,))
            print("established connection")

    def exchange(self, exchange_socket):
        i = 0
        while self.keep_going:
            message = b"MSG%d\n" % i
            exchange_socket.send(message)
            i += 1

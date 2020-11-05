import socket, _thread, jsonpickle


class Ecoute:

    def __init__(self, q, port=2222):
        self.s_ecoute = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.s_ecoute.bind(('', port))
        self.s_ecoute.listen()
        self.q = q
        self.encore = True

    def start(self):
        _thread.start_new(self.ecoute, ())

    def stop(self):
        self.encore = False

    def ecoute(self):
        print("Service en écoute ...")
        while self.encore:
            s_echange, _ = self.s_ecoute.accept()
            _thread.start_new(self.echanger, (s_echange,))
            print("connexion etablie")

    def echanger(self, s_echange):
        while self.q.qsize() > 0:
            msg = self.q.get()
            s_echange.send((jsonpickle.dumps(msg) + "\n").encode())
        s_echange.close()

import _thread, time, message


class Producteur:

    def __init__(self, queue):
        self.queue = queue
        self.encore = True

    def start(self):
        _thread.start_new(self.run, ())

    def stop(self):
        self.encore = False

    def run(self):
        i = 0
        while self.encore:
            msg = message.Message(i)
            self.queue.put(msg)
            # print(len(self.queue))
            # time.sleep(.001)
            # print("%d %s" % (self.msg.val, self.msg.contenu()))
            i += 1

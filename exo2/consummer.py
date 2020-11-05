import time, _thread, jsonpickle


class Consummer:
    def __init__(self, queue):
        self.queue = queue
        self.keep_going = True

    def start(self):
        _thread.start_new_thread(self.run, ())

    def stop(self):
        self.keep_going = False

    def run(self):
        while self.keep_going:
            if self.queue:
                print(jsonpickle.loads(self.queue.get()))
            time.sleep(0.00001)


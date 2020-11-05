class Message:

    def __init__(self, val):
        self.val = val

    def contenu(self):
        return "MSG%d" % self.val

    def incrementer(self):
        self.val += 1

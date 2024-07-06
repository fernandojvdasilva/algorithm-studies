class Logger:

    def __init__(self):
        self.message_hist = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        result = False
        if not message in self.message_hist.keys() or \
        timestamp - self.message_hist[message] >= 10:
            self.message_hist[message] = timestamp
            result = True
        
        return result
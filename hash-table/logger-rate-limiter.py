class Logger:

    def __init__(self):
        # Map message -> earliest timestamp at which it can next be printed
        self.next_allowed = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # Check if this message is allowed to be printed now
        if message not in self.next_allowed or timestamp >= self.next_allowed[message]:
            # Either it’s new, or we've waited at least 10s since last print
            self.next_allowed[message] = timestamp + 10
            return True
        else:
            # Too soon to print again
            return False

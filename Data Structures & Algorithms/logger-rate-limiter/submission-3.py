class Logger:

    def __init__(self):
        self.mapping = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        print(self.mapping)
        if message  not in  self.mapping:
            self.mapping[message]=timestamp+10
            return True
        elif timestamp < self.mapping[message] :
            return False
        else:
            self.mapping[message]=10+timestamp
            return True



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

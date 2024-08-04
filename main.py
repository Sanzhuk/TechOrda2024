import sys

class Logger:
    def __init__(self):
        self.d = {}
        self.count = 0
    
    def shouldPrintMessage(self, time, message):
        if self.loggerSize() > 100:
            self.d = {}
        
        if message not in self.d:
            self.d[message] = [time]
            self.count += 1
            return True
        else:
            if time >= 10 + self.d[message][-1]:                  
                self.d[message].append(time)
                return True
            else:
                return False
    
    def clean(self, time):
        for key in list(self.d.keys()):
            for i in self.d[key]:
                if i == time:
                    return False
                
        return True
    
    def loggerSize(self):
        return self.count

if __name__ == '__main__':
    logger = Logger();
    print("""Input time and message to access "shouldPrintMessage"\nInput time to access "clean"\nInput nothing to access "loggerSize" """)
    
    while True:
        try:
            line = input().strip()
            if len(line.split(" ")) == 2:
                time = int(line.split(" ")[0])
                message = line.split(" ")[-1]
                print(logger.shouldPrintMessage(time, message))
            elif len(line.split(" ")) == 1 and line.isdigit():
                time = int(line)
                print(logger.clean(time))
            elif len(line) == 0:
                print(logger.loggerSize())
        except Exception as e:
            print(f"Error occurred: {e}")
            sys.exit()

class queue():
    def __init__(self):
        self.queue=list()

    def addtoq(self,dataval):
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
        return True
        return False
    
    def size(self):
        return len(self.queue)

    def show(self):
        return self.queue

    def pop(self):
        return self.queue.pop(0)

    def add1(self,value):
        self.queue.insert(0,value)
    
    def addend(self,value):
        self.queue.append(value)
    
    def popend(self):
        return self.queue.pop()

    


theq=queue()
theq.addtoq("mon")
theq.addtoq('tue')
theq.addtoq("son")
theq.add1("mo")
theq.addend("sal")
theq.pop()
theq.popend()
print(theq.size())
print(theq.show())

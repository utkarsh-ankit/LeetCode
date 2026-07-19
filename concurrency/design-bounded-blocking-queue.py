import threading

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.queue=deque()
        self.cond=threading.Condition() #A Condition variable wraps a Lock and adds wait()/notify() capabilities
        

    def enqueue(self, element: int) -> None:
        with self.cond:
            while len(self.queue)==self.capacity:
                self.cond.wait()

            self.queue.append(element)

            self.cond.notify()
        

    def dequeue(self) -> int:
        with self.cond:

            while len(self.queue)==0:
                self.cond.wait()

            val=self.queue.popleft()

            self.cond.notify()

            return val
        

    def size(self) -> int:
        with self.cond:
            return len(self.queue)
        
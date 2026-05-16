class Node:
    def __init__(self, key, value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.head, self.tail=Node(0,0),Node(0,0)
        self.head.next, self.tail.prev=self.tail, self.head

    def rem(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p

    def add_f(self, node):
        f=self.head.next
        node.next=f
        node.prev=self.head

        f.prev=node
        self.head.next=node

        #or
        # node.next, node.prev = self.head.next, self.head
        # self.head.next.prev = node
        # self.head.next = node
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self.rem(node)
            self.add_f(node)
            return node.value
        return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.rem(self.cache[key])
        node=Node(key,value)
        self.cache[key]=node
        self.add_f(node)

        if len(self.cache)>self.capacity:
            l=self.tail.prev
            self.rem(l)
            del self.cache[l.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class Node:
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key] 
            node.value = value
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            node = Node(key, value)
       
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        
        self.map[key] = node

        if len(self.map) > self.capacity:
            last_node = self.tail.prev
            del self.map[last_node.key]
            last_node.prev.next = self.tail
            self.tail.prev = last_node.prev

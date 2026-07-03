class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.limit = capacity
        self.map = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]
        self.delNode(node)
        self.addNode(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.delNode(self.map[key])
            del self.map[key]

        if self.limit == len(self.map):
            lru = self.tail.prev          # save reference BEFORE unlinking
            self.delNode(lru)
            del self.map[lru.key]

        new = Node(key, value)
        self.addNode(new)
        self.map[key] = new

    def addNode(self, new):
        prev = self.head
        next = self.head.next

        prev.next = new
        new.prev = prev

        new.next = next
        next.prev = new

    def delNode(self, old):
        prev = old.prev
        next = old.next

        prev.next = next
        next.prev = prev
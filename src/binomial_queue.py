class BinomialNode:
    def __init__(self, value):
        self.value = value
        self.degree = 0
        self.parent = None
        self.child = None
        self.sibling = None


class BinomialQueue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert(self, value):
        new_node = BinomialNode(value)
        new_queue = BinomialQueue()
        new_queue.head = new_node

        self.merge(new_queue)

    def merge(self, other_queue):
        if self.head is None:
            self.head = other_queue.head
            return

        if other_queue.head is None:
            return

        self.head = self._merge_trees(self.head, other_queue.head)

    def _merge_trees(self, h1, h2):
        if not h1:
            return h2
        if not h2:
            return h1

        if h1.value > h2.value:
            h1, h2 = h2, h1

        h1.child = self._merge_trees(h1.child, h2)
        h1.degree += 1
        h2.parent = h1
        h1.sibling = h2.sibling
        h2.sibling = None
        return h1

    def delete_min(self):
        if self.is_empty():
            raise ValueError("Queue is empty")

        min_node = self._find_min(self.head)
        if not min_node:
            return None

        self._remove_min(min_node)
        return min_node.value

    def _find_min(self, node):
        min_node = node
        current = node
        while current:
            if current.value < min_node.value:
                min_node = current
            current = current.sibling
        return min_node

    def _remove_min(self, node):
        if node == self.head:
            self.head = node.sibling
        else:
            current = self.head
            while current.sibling != node:
                current = current.sibling
            current.sibling = node.sibling

        node.sibling = None
        if node.child:
            child = node.child
            while child:
                child.parent = None
                child = child.sibling
            self.head = self._merge_trees(self.head, node.child)
        node.child = None

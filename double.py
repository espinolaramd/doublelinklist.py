class Node:
    def __init__(self, next= None , prev= None ,data=None):
        self.data = data
        self.next = next
        self.prev= prev

    def __repr__(self):
        return repr(self.data)

class double_linked_list:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        curr= self.head
        while curr:
            nodes.append(repr(curr))
            curr= curr.next
        return str(nodes)

    def push_head(self,new_data):
        new_node = Node(data=new_data)
        new_node.next = self.head
        new_node.prev= None
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def push_end(self,data):
        new_node = Node (data=data)
        current = self.head
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def remove_head(self):
        new_node = self.head
        self.head= self.head.next
        return print(new_node.data)

    def remove_end(self):
        current = self.head
        new_node = self.head
        while current.next:
            current = current.next
            new_node = current
        current.prev.next = None
        return print(new_node.data)


class SingleLinkedList(object):

    class Node(object):

        def __init__(self, value):
            self.val = value
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):

        if index < 0 or self.size == 0:
            return -1

        pointer = self.head
        counter = 0

        while counter < index:
            pointer = pointer.next
            counter += 1

        return pointer.val

    def add_at_head(self, value):
        node = self.Node(value)
        node.next = self.head
        self.head = node
        self.size += 1
    
    def __str__(self):
        counter = self.head
        output = 'Head '
        while counter!=None:
            output += ' -> ' + str(counter.val) 
            counter = counter.next
        return output

if __name__ == '__main__':

    obj = SingleLinkedList()
    obj.add_at_head(4)
    obj.add_at_head(10)

    print(obj)

    print(obj.get(0))
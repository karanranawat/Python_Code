class LinkedStack:
    # Internal Node class
    class _Node:
        __slots = '_element','_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
            
    # Stack methods
    def __init__(self):
        # Create empty stack
        self._head = None  # Reference to NULL
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def push(self,e):
        # Add element to top of the list
        self._head = self._Node(e,self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            print('Stack is empty')
            return
        return self._head._element

    def pop(self):
        if self.is_empty():
            print( 'Stack is empty')
            return
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

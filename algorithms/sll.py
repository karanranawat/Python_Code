class SinglyLinkedList:
    ''' Singly Linked list implementations
        Different list operations and pointer manipulations
    '''
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

    def get_head(self):
        return self._head

    def add(self,e):
        ptr = self._head
        if ptr != None:
            while ptr._next!= None:
                ptr = ptr._next
        else:
            self._head = self._Node(e,None)
            self._size += 1
            return
            
        # Add element at the end of the list
        ptr._next = self._Node(e,None)
        self._size += 1

    def print_list(self):
        ptr = self._head
        while ptr!=None:
            print((str)(ptr._element))
            ptr = ptr._next

    def add_list(self,head2,l):
        ptr = self._head
        while ptr._next!=None:
            ptr = ptr._next

        ptr._next = head2
        self._size += l.__len__()

    def get_element(self,loc):
        ptr = self._head
        i = 0
        if loc>self.__len__():
            print('Invalid location')
            return
        print(str(ptr._element))
        while i<loc:
            i+=1
            ptr = ptr._next
            print('i = ' + str(i) + 'Location = ' + str(loc))
            print(str(ptr._element))
        return ptr  

# Create Singly Linked List
sll= SinglyLinkedList()

# Perform basic operations
sll.add(1)
sll.add(200)
sll.add(300)
sll.add(1000)
sll.add(400)

# 2nd Linked list
sl2 = SinglyLinkedList()
sl2.add(31)
sl2.add(32)

# concatenate two lists
sll.add_list(sl2.get_head(),sl2)

# get concatenated list
sll.print_list()

'''
Array Stack implementation
Amortized cost = O(1)
Worst case cost for push/pop = O(N)
'''

class ArrayStack(object):

    def __init__(self):
        self.s = [0] #initialize with array of size 1
        self.top = 0


    def push(self,item):
        if len(self.s)==self.top:   # 100% full - its time to double
            self.resize(2*len(self.s))

        self.s[self.top] = item
        self.top +=1

    def pop(self):
        if self.is_empty():
            return 'Stack empty'
            
        self.top -= 1
        item = self.s[self.top]
        if len(self.s)/4 == self.top: # 25% Full - its time to half
            self.resize(len(self.s)/2)

        return item

    def resize(self,capacity):
        copy = [0 for x in range(capacity)]

        for i in range(0,self.top):
            copy[i] = self.s[i]

        self.s = copy

    def is_empty(self):
        return self.top == 0

if __name__ == '__main__':

    #Tests
    s= ArrayStack()
    s.push(10)
    s.push(11)
    s.push(12)

    print s.pop()
    print s.pop()
    print s.pop()
    print s.pop()

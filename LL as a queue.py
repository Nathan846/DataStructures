class LinkedQueue:
    class _Node():
        def __init__(self,e):
            self.e=e
            self.next=None
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def __len__(self):
        return self.size
    def _isempty(self):
        return self.size==0
    def enqueue(self,e):
        newest=self._Node(e)
        if(self._isempty()):
            self.head=newest
        else:
            self.tail.next=newest
        self.tail=newest
        print(self.head.next)
        self.size+=1
    def dequeue(self):
        if(self._isempty()):
            raise Exception("EMpty")
        ans=self.head.e
        self.head=self.head.next
        self.next=None
        if(self._isempty()):
            self._tail=None
        self.size-=1
        return ans
L=LinkedQueue()
L.enqueue(5)
L.enqueue(10)
print(L.dequeue())
print(L.dequeue())

        
    

class CircularQueue:
    class Node():
        def __init__(self,e):
            self.e=e
            self.next=None
    def __init__(self):
        self.tail=None
        self.size=0
    def __len__(self):
        return self.size
    def first(self):
        h=self.tail.next
        return h.e
    def enqueue(self,e):
        t=self.Node(e)
        if(self.size==0):
            t.next=t
        else:
            t.next=self.tail.next
            self.tail.next=t
        self.tail=t
        self.size+=1
    def dequeue(self):
        g=self.tail.next
        if(self.size==1):
            self.tail=0
        else:
            self.tail.next=g.next
        self.size-=1
        return g.e
    def rotate(self):
        if(self.size>0):
            self.tail=self.tail.next
    def __str__(self):
        curr=self.tail.next
        L=[]
        while(curr!=self.tail):
            L.append(str(curr.e))
            curr=curr.next
        L.append(str(self.tail.e))
        return "".join(L)
F=CircularQueue()
F.enqueue(5)
F.enqueue(7)
F.enqueue(3)
print(F)
F.rotate()
print(F)
F.dequeue()
print(F)

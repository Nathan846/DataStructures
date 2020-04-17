class Tree:
    class Position:
        def element(self):
            raise NotImplementedError("Not implemented")
        def __eq__(self,other):
            raise NotImplementedError("Not implemented")
        def __ne__(self,other):
            return not self==other
    def root(self,p):
        raise NotImplementedError("Not implemented")
    def parent(self,p):
        raise NotImplementedError("Not implemented")
    def num_children(self,p):
        raise NotImplementedError("Not implemented")
    def children(self,p):
        raise NotImplementedError("Not implemented")
    def len(self,p):
        raise NotImplementedError("Not implemented")
    def is_root(self,p):
        return self.root()==p
    def is_leaf(self,p):
        return self.num_children(p)==0
    def is_empty(self):
        return len(self)==0
class BinaryTree(Tree):
    def left(self,p):
        raise NotImplementedError("Not implemented")
    def right(self,p):
        raise NotImplementedError("Not implemented")
    def sibling(self,p):
        parent=self.parent(p)
        if parent==None:
            return None
        else:
            if p==self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
        def children(self,p):
            if(self.left(p) is not None):
                yield self.left(p)
            if(self.right(p) is not None):
                yield self.right(p)
            return None
class LinkedBinaryTree(BinaryTree):
    class _Node():
        __slots__='e','left','right','parent','id'#StreamLine Memory
        def __init__(self,e,id,parent=None,left=None,right=None):
            self.e=e
            self.id=id
            self.parent=parent
            self.left=left
            self.right=right
    class Position(BinaryTree.Position):
        def __init__(self,container,node):#Container holds the LinkedBinaryTree instance and node holds the node object
            self.container=container
            self.node=node
        def element(self):
            return self.node.e
        def __eq__(self,other):
            return (type(other) is type(self) and other.node is self.node)

    def validate(self,p):
        if not isinstance(p, self.Position):
            raise TypeError(' p must be proper Position type ')
        if p. container is not self:
            raise ValueError(" p does not belong to this container ")
        if p. node. parent is p. node:
            raise ValueError(" p is no longer valid ")
        return p.node
    def make_position(self,node):
        return self.Position(self,node) if node is not None else None
    def __init__(self):
        self.root=None
        self.size=0
    def __len__(self):
        return self.size
    def root(self):
        return make_position(self.root)
    def parent(self,p):
        node=self.validate(p)
        return self.make_position(node.parent)
    def left(self,p):
        node=self.validate(p)
        return self.make_position(node.left)
    def right(self,p):
        node=self.validate(p)
        return self.make_position(node.right)
    def num_children(self,p):
        node=self.validate(p)
        c=0
        if(node.left is not None):
            c+=1
        if(node.right is not None):
            c+=1
        return c
    def add_root(self,p,e):
        if(self.root is not None):
            raise ValueError("root already assigned")
        self.size=1
        self.root=self._Node(e,p)
        return self.make_position(self.root)
    def add_left(self,p,e):
        node=self.validate(p)
        if(node.left is not None):
            raise ValueError("wrong assingment")
        self.size+=1
        node.left=self._Node(e,node)
        node.left.parent=node
        return self.make_position(node.left)
    def add_right(self,p,e):
        node=self.validate(p)
        if(node.right is not None):
            raise ValueError("wrong assingment")
        self.size+=1
        node.right=self._Node(e,node)
        node.right.parent=node
        return self.make_position(node.right)
    def replace(self,p,e):
        node=self.validate(p)
        old=node.e
        node.e=e
        return old
t=LinkedBinaryTree()
Root=t.add_root('Node1',3)#Root is a position object whose container is t and node is Root node
Node1=t.add_right(Root,5)#Node1 is a position object whose container is t and node is Node1 node
Node2=t.add_left(Root,8)
Node3=t.add_right(Node1,4)
print(Node1.element())
print(t.num_children(Root))
print(t.sibling(Node1).element(),t.parent(Node1).element(),t.sibling(Node2).element())
print(len(t))

#Output:
'''5
2
8 3 5
4
'''

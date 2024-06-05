class Tree:
    def __init__(self, x):
        self.rt = x
        self.child = []
 
    def add_child(self, a):
        self.child.append(a)
 
    def root(self):
        return self.rt

    def ith_child (self, i):
        return self.child[i]
 
    def num_children (self):
        return len(self.child)
     
class Pre(Tree):

    def preorder(self):
        yield self.rt
        for c in self.child:
            for x in c.preorder():
                yield x

t = Pre(2)
t.add_child(Pre(3))
t.add_child(Pre(4))
t.num_children()
t.ith_child(1).add_child(Pre(5))

print([next(t.preorder()) for i in range(6)])

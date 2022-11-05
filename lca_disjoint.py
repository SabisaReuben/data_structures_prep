class Tree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.rank = 0
            self.left = None
            self.right = None
            self.parent = None
        

        def insert(self, value, parent, rank, node_list):
            node = Tree.Node(value)
            node.rank = rank
            
            if value < parent.value:
                if parent.left == None:
                    node.parent = parent
                    parent.left = node
                else:
                    self.insert(value,parent.left, rank, node_list)
            else:
                if parent.right == None:
                    node.parent = parent
                    parent.right = node
                else:
                    self.insert(value, parent.right,rank,node_list)

            node_list.append(node)
            return node_list

    def __init__(self):
        self.size = 0
        self.node_list = []
        self.disjoint = [None for i in range(7) ]
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Tree.Node(value)
            self.size +=1
            return
        self.node_list = self.root.insert(value, self.root, self.size, self.node_list)

    def create_disjoint(self):
        for node in self.node_list:
            self.disjoint[node.rank] = node.parent.rank

if __name__ == "__main__":
    t = Tree()

    t.insert(30)
    t.insert(20)
    t.insert(40)
    t.insert(16)
    t.insert(19)
    t.insert(36)
    t.insert(56)

    t.create_disjoint()
    print(t.disjoint)





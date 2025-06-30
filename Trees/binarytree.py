class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self):
        self.left = Node(20)
        self.left.left = Node(40)
        self.left.right = Node(50)
        self.right = Node(30)
        

    def preOrder(self, node):
        if node is None:
            return
        print(node.data)
        self.preOrder(node.left)
        self.preOrder(node.right)


    def postOrder(self, node):
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.data)

    def inorder(self,node):
        if node is None:
            return
        else:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)

    def numNodes(self,root):
        if root is None:
            return 0
        return self.numNodes(root.left) + self.numNodes(root.right) + 1
    

    def maxHeight(self,root):
        if root is None:
            return 0
        return max (self.maxHeight(root.left),self.maxHeight(root.right) )+1
    
    def maxDiameter(self,root):
        if root is None :
            return 0
        currentdia = self.maxDiameter(root.left) + self.maxDiameter(root.right) +1
        lefdia = self.maxDiameter(root.left)
        rightdia = self.maxDiameter(root.right)
        return max(currentdia,lefdia,rightdia)

    def minDiameter(self,root):
        if root is None :
            return 0
        currentdia = self.minDiameter(root.left) + self.minDiameter(root.right) +1
        lefdia = self.minDiameter(root.left)
        rightdia = self.minDiameter(root.right)
        return min(currentdia,lefdia,rightdia)

    def levelorder(self,root):
        q = []
        q.append(root)
        q.append(None)
        while len(q):
            node = q.pop(0) 
            if node is None:
                if len(q):
                    q.append(None)
            else:
                print(node.data)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
        

    def klevelorder(self,root,k):
            q=[]
            q.append(root)
            q.append(None)
            count = 0

            while len(q):
                node = q.pop(0)
                if node is None :
                    if len(q):
                        count = count +1
                        q.append(None)
                        
                else:
                    if count is k:
                        print(node.data)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

    
        
root = Node(10)
root.insert()
print("PRE ORDER TRAVERSAL")
# Display the binary tree
root.preOrder(root)
print("Post order traversal")
root.postOrder(root)
print("Number of nodes")
print(root.numNodes(root))
print("Maximum height of the tree :") ,print(root.maxHeight(root))
print("maximum diameter :")
print(root.maxDiameter(root))
print("minimum diameter of tree :")
print(root.minDiameter(root))
print("level order traversal :")
root.levelorder(root)
print("L level traversal :")
root.klevelorder(root,2)

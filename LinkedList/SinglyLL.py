class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __rep__(self):
        node = self.head
        while node is not None:
            print(str(node.data) + "->")
            node = node.next
        print("Null")

    def __insertfirst__(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def __insertlast__(self,data):
        node = Node(data)
        if self.head is None :
            self.__insertfirst__(data)

        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node

    def __deletefirst__(self):
        if self.head.next is None:
            self.head = None
        else:
            self.head =self.head.next
        
    def __deletelast__(self):
        if self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None




    
        
a = LinkedList()
a.__insertfirst__(100)
a.__insertfirst__(200)
a.__insertlast__(300)
a.__insertlast__(500)
a.__insertlast__(400)
a.__deletefirst__()
a.__deletelast__()
a.__deletelast__()
a.__deletefirst__()
a.__rep__()


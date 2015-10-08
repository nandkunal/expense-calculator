class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    def insert(self, data):
        new_node = Node(data)
        new_node.setNext(self.head)
        self.head = new_node
    def print_list(self):
        current=self.head
        while current!=None:
            print current.getData()
            current=current.getNext()
    def reverse_list(self):
        current = self.head
        prev=None
        next_node=None
        while current!=None:
            next_node=current.next
            if(next_node==None):
                self.head=current
            current.next=prev
            prev=current
            current=next_node



l = LinkedList()
l.insert(0)
l.insert(1)
l.insert(2)
l.insert(3)
l.print_list()
l.reverse_list()
print "After Reversal"
l.print_list()
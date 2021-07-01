class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CList:
    def __init__(self):
        self.last = None
    
    def insertAtFront(self, data):
        newNode = Node(data)
        if (self.last == None):    
            newNode.next = newNode
            self.last = newNode
        else:
            newNode.next = self.last.next
            self.last.next = newNode
    
    def display(self):
        if (self.last == None):
            print("\n List is empty \n")
        else:
            temp = self.last.next
            while temp != self.last.next:
                print(str(temp.data) + "->", end=" ")
                temp = temp.next

if __name__ == '__main__':
    cl = CList()
    print("\n Inserting the data")
    cl.insertAtFront(10)
    cl.insertAtFront(20)
    cl.insertAtFront(30)

    cl.display()

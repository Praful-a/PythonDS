class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def display(self):
        if(self.head == None):
            print("\n List is empty !!")
        else:
            temp = self.head
            print("  ", end="")
            while(temp != None):
                print("{}".format(temp.data), end=" ", sep='->')
                temp = temp.next
    
    def getNth(self, index):
        count = 0
        if(self.head == None):
            print("\n List is empty !!")
        else:
            temp = self.head
            while(temp != None):
                if(count == index):
                    return temp.data
                count += 1
                temp = temp.next
            

if __name__ == '__main__':
    L = linkList()
    L.insert(1)
    L.insert(4)
    L.insert(1)
    L.insert(12)
    L.insert(1)
    L.display()
    print("Element at index 3 is : ", L.getNth(3))
    
    

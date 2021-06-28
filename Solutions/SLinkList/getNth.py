class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def getNth(self, index):
        count = 0
        if(self.head == None):
            print("\n List is empty ")
        else:
            temp = self.head
            while(temp != None):
                if (count == index):
                    return temp.data
                count += 1
                temp = temp.next

    def display(self):
        if(self.head == None):
            print("\n List is empty !!\n")
        else:
            temp = self.head
            while(temp != None):
                print(" {}".format(temp.data), end=" ")
                temp = temp.next
    

if __name__ == '__main__':
    L = LinkList()
    L.push(10)
    L.push(20)
    L.push(30)
    L.push(40)
    L.push(50)
    L.display()
    print()
    print(" The elemet at 3 is :", L.getNth(2))
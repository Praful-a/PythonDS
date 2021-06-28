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
    
    def getNth(self, llist, position):
        llist.getNthNode(self.head, position, llist)

    def getNthNode(self, head, position, llist):
        count = 0
        if(head):
            if count == position:
                print(head.data)
            else:
                llist.getNthNode(head.next, position - 1, llist)
        else:
            print(" Index Doesn\'t exists ")

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
    print("\n Element at Index 3 is", end= " ")
    L.getNth(L, 3)
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLNode:
    def __init__(self):
        self.head = None

    def insert(self):
        self.data = int(input("\n Enter the element to insert : "))
        return self.data

    def insertAtBeg(self, data):
        newNode = DNode(data)
        if(self.head == None):
            self.head = newNode
        else:  
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            print("\n Inserted Successfully !!\n")

    def insertAtEnd(self, data):
        newNode = DNode(data)
        if (self.head == None):
            self.head = newNode
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp
            print("\n Inserted Successfully !!\n")
    
    def size(self):
        count = 0
        temp = self.head
        if(temp == None):
            print("\n List is empty !!\n")
        else:
            while(temp != None):
                count += 1
                temp = temp.next
        return count

    def insertAtPos(self, data, pos):
        count = self.size()
        newNode = DNode(data)
        if(pos < 1 or pos > count):
            print("\n Invalid Position !!\n")
        elif (pos == 1):
            newNode.next = self.head
            self.head = newNode
            print("\n Inserted Successfully !!\n")
        else:
            temp = self.head
            for cur in range(1, pos - 1):
                temp = temp.next
            newNode.prev = temp
            newNode.next = temp.next
            temp.next = newNode
            temp.next.prev = newNode
            print("\n Inserted Successfully !!\n")

    def deleteAtBeg(self):
        if(self.head == None):
            print("\n List is empty !!\n")
        else:
            temp = self.head
            self.head = self.head.next
            print("\n Deleted node is : {}".format(temp.data))
            temp = None
            print("\n Deleted Successfully !!\n")

    def deleteAtEnd(self):
        if(self.head == None):
            print("\n List is empty !!\n")
        if(self.head.next == None):
            print("\n Deleted node is : {}".format(self.head.data))
            self.head = None
            print("\n Deleted Successfully !!\n")
        else:
            temp = self.head
            while (temp.next != None):
                previous = temp
                temp = temp.next
            previous.next = None
            print("\n Deleted node is : {}".format(temp.data))
            temp = None
            print("\n Deleted Successfully !!\n")

    def deleteAtPos(self, pos):
        count = self.size()
        if(self.head == None):
            print("\n List is empty \n")
        if (pos < 1 or pos > count):
            print("\n Invalid Choice !!\n")
        elif (pos == 1):
            temp = self.head
            self.head = self.head.next
            temp.next = None
            print("\n Deleted element is : {}\n".format(temp.data))
            temp = None
            print("\n Deleted Successfully \n")
        else:
            temp = self.head
            for cur in range(1, pos):
                curr = temp
                temp = temp.next
            curr.next = temp.next
            temp.next.prev = curr.next
            print("\n Deleted element is : {}".format(temp.data))
            temp = None
            print("\n Deleted Successfully \n")

    def display(self):
        temp = self.head
        if(temp == None):
            print("\n List is empty !!\n")
        else:
            print("\n List Constains : ")
            while(temp != None):
                print(" " + " {} ".format(temp.data), end=" ")
                temp = temp.next
            print("\n Executed Successfully !!\n")


if __name__ == '__main__':
    Dln = DLNode()
    while(True):
        print(" 1. Insert at beginning ")
        print(" 2. Insert at end ")
        print(" 3. Insert at position ")
        print(" 4. Display ")
        print(" 5. Size of the list ")
        print(" 6. Delete at beginning ")
        print(" 7. Delete at end ")
        print(" 8. Delete at position ")
        print(" 9. Exit ")
        choice = int(input("\n Enter the choice : "))
        if (choice == 1):
            data = Dln.insert()
            Dln.insertAtBeg(data)
        elif (choice == 2):
            data = Dln.insert()
            Dln.insertAtEnd(data)
        elif (choice == 3):
            data = Dln.insert()
            pos = int(input("\n Enter the position : "))
            Dln.insertAtPos(data, pos)
        elif (choice == 4):
            Dln.display()
        elif (choice == 5):
            size = Dln.size()
            print(" The size of the list is : {}\n".format(size))
        elif (choice == 6):
            Dln.deleteAtBeg()
        elif (choice == 7):
            Dln.deleteAtEnd()
        elif (choice == 8):
            pos = int(input("\n Enter the position : "))
            Dln.deleteAtPos(pos)
        elif (choice == 9):
            break;
        else:
            print("\n Invalid Choice !!")
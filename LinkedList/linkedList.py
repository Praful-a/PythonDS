# Single Linked list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self):
        self.data = int(input("Enter an element : "))
        return self.data

    def insertAtBeg(self, data):
        newNode = Node(data)
        if (self.head == None):
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        print("\n .. Inserted Successfully ..")

    def insertAtEnd(self, data):
        newNode = Node(data)
        cur = self.head
        if(self.head == None):
            self.head = newNode
        else:
            while(cur.next != None):
                cur = cur.next
            cur.next = newNode
        print("\n .. Inserted Successfully ..")
    
    def size(self):
        count = 0
        if (self.head is None):
            print("\n .. List is empty ..")
            return
        else:
            temp = self.head
            while (temp != None):
                count += 1
                temp = temp.next
        return count

    def insertAtPos(self, pos, data):
        newNode = Node(data)
        count = self.size()
        if(pos < 1 or pos > count):
            print("\n Invalid Position !!")
        elif(pos == 1):
            newNode.next = self.head
            self.head = newNode
            print("\n .. Inserted Successfully ..")
        else:
            temp = self.head
            for i in range(1, pos - 1):
                temp = temp.next
        
            newNode.next = temp.next
            temp.next = newNode
            print("\n .. Inserted Successfully ..")
            
            
    def deleteAtBeg(self):
        if (self.head == None):
            print("\n .. List is empty ..")
        else:
            temp = self.head
            self.head = self.head.next
            print("\n .. Deleted element is :", temp.data)
            temp = None
            print("\n .. Deleted Successfully ..")
    
    def deleteAtEnd(self):
        if(self.head == None):
            print("\n .. List is empty ..")
        if (self.head.next == None):
            print("\n .. Delted element is : ", self.head.data)
            self.head = None
            print("\n .. Deleted Successfully ..")
        else:
            curr = self.head
            while(curr.next != None):
                prev = curr
                curr = curr.next
            prev.next = None
            print("\n .. Deleted element is: ", curr.data)
            curr = None
            print("\n .. Deleted Successfully ..")

    def deleteAtPos(self, pos):
        count = self.size()
        if(self.head == None):
            print("\n .. List is empty ..")
        if (pos < 1 or pos > count):
            print("\n Invalid Position !!")
        elif(pos == 1):
            temp = self.head
            self.head = self.head.next
            print("\n .. Deleted element is : ", temp.data)
            temp = None
            print("\n .. Deleted Successfully ..")
        else:
            temp = self.head
            for i in range(1, pos):
                prev = temp
                temp = temp.next
            prev.next = temp.next
            temp.next = None
            print("\n .. Deleted element is : ", temp.data)
            temp = None
            print("\n .. Deleted Successfully ..")
            
    def display(self):
        cur = self.head
        if (cur == None):
            print("\n .. List is empty ..")
        else:
            print("\n .. List Contains ..")
            while(cur):
                print("  "+"{}".format(cur.data), end=" ")
                cur = cur.next
            print("\n .. Executed Successfully ..")

if __name__ == "__main__":
    list = Linkedlist()
    while True:
        print("\n1. Insert at beginning.. ")
        print("2. Insert at end.. ")
        print("3. Insert at position.. ")
        print("4. Display.. ")
        print("5. Size of the list.. ")
        print("6. Deleted at beginning.. ")
        print("7. Delete at end..")
        print("8. Delete at position.. ")
        print("9. Exit.. ")
        choice = int(input("Enter the choice : "))
        
        if (choice == 1):
            data = list.insert()
            list.insertAtBeg(data)
        elif (choice == 2):
            data = list.insert()
            list.insertAtEnd(data)
        elif (choice == 3):
            data = list.insert()
            pos = int(input(" Enter the position :"))
            list.insertAtPos(pos, data)
        elif (choice == 4):
            list.display()
        elif (choice == 5):
            count = list.size()
            print("\n .. List Contains : {} elements ..".format(count))
        elif (choice == 6):
            list.deleteAtBeg()
        elif (choice == 7):
            list.deleteAtEnd()
        elif (choice == 8):
            pos = int(input(" Enter the position : "))
            list.deleteAtPos(pos)
        elif (choice == 9):
            break
        else:
            print("Invalid choice!!")
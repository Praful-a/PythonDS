# Single Linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 


class LinkedList:
    def __init__(self):
        self.head = None 
    
    def insert(self):
        self.data = int(input("Enter the data to insert : "))
        return self.data

    def insertAtBeg(self, new_data):
        newNode = Node(new_data)
        if(self.head == None):
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            print("\n .. Inserted Successfully ..")
        return self.head

    def insertAtEnd(self, data):
        newNode = Node(data)
        if(self.head == None):
            self.head = newNode
        else:
            cur = self.head
            while(cur.next != None):
                cur = cur.next
            cur.next = newNode
            print("\n .. Inserted Successfully ..")
        return self.head

    def length(self):
        count = 0
        while(self.head != None):
            count += 1
            self.head = self.head.next
        return count        

 

    # def deleteAtBeg(self):
    #     if(self.head == None):
    #         print(" .. List is empty ..")
    #     else:
    #         temp = self.head
    #         self.head = self.head.next
    #         print('Deleted element is :', temp.data)
    #         temp = None
    #         print("\n .. Removed Successfully .. ")
        
    
    # def deleteAtEnd(self):
    #     if(self.head == None):
    #         print(" .. List is empty ..")
    #     else:
    #         temp = self.head
    #         while(temp.next != None):
    #             prev = temp
    #             temp = temp.next
    #         prev.next = None
    #         print("Deleted element is :", temp.data)
    #         temp = None
    #         print("\n .. Removed Successfully .. ")
        
    # def deleteAtPos(self, pos):
    #     count = self.length()
    #     if (pos < 1 or pos > count):
    #         print(" .. Invalid position ..")
    #     elif (pos == 1):
    #         temp = self.head
    #         self.head = self.head.next
    #         print(" Deleted element is :", temp.data)
    #         temp = None
    #         print("\n .. Removed Successfully ..")
    #     else:
    #         temp = self.head
    #         for cur in range(1, pos):     
    #             prev = temp
    #             temp = temp.next
            
    #         prev.next = temp.next
    #         temp.next = None
    #         print(" Deleted element is :", temp.data)
    #         temp = None
    #     return self.head

    def display(self):
        temp = self.head
        if(temp == None):
            print(" .. List is Empty ..")
        else:
            print(" .. List Contains ..")
            print("\t\t")
            while(temp != None):
                print(temp.data, end=" ")
                temp = temp.next
            print("\n .. Executed Successfully .. ")

if __name__ == "__main__":
    list = LinkedList()
    while True:
        print("\n1. Insert at beginning.. ")
        print("2. Insert at end.. ")
        print("3. Insert at position.. ")
        print("4. Display.. ")
        print("5. Size of the list.. ")
        print('6. Delete at beginning.. ')
        print("7. Delete at end.. ")
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
            pos = int(input("Enter the position :"))
            list.insertAtPos(data, pos)
        elif (choice == 4):
            list.display()
        elif (choice == 5):
            data = list.length()
            print("The size of the list is :", data)
        # elif (choice == 6):
        #     list.deleteAtBeg()
        # elif (choice == 7):
        #     list.deleteAtEnd()
        # elif (choice == 8):
        #     pos = int(input("Enter the position :"))
        #     list.deleteAtPos(pos)
        elif (choice == 9):
            break
        else:
            print("Invalid choice!!")
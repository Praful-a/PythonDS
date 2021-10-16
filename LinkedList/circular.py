class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 


class CircularList:
    def __init__(self):
        self.last = None 

    def insertAtBeg(self, data):
        newNode = Node(data)
        if self.last is None:
            self.last = newNode 
            self.last.next = self.last  
        else: 
            newNode.next = self.last.next 
            self.last.next = newNode 

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.last is None:
            self.last = newNode
            self.last.next = self.last 
        else:
            newNode.next = self.last.next 
            self.last.next = newNode 
            self.last = newNode 

    def insertAfter(self, data, item):
        newNode = Node(data)
        temp = self.last.next 
        while temp:
            if (temp.data == item):
                newNode.next = temp.next 
                temp.next = newNode
                if(temp == self.last):
                    self.last = newNode 
                    break
                else:
                    break
            temp = temp.next 
            if (temp == self.last.next):
                print(item, "not exists !!")
                break

    def display(self):
        if self.last is None:
            print("List is empty !!")
            return
        else:
            temp = self.last.next  
            while temp:
                print(f"{temp.data}", end = " ")
                temp = temp.next 
                if (temp == self.last.next):
                    break


if __name__ == '__main__':
    cll = CircularList()
    cll.insertAtBeg(10)
    cll.insertAtEnd(2)
    cll.insertAtEnd(21)
    cll.insertAfter(100, 10)
    cll.insertAfter(101, 2)
    cll.display()
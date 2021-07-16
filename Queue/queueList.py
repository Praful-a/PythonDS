class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def frontElement(self):
        if(self.isEmpty()):
            print("\nQueue is Underflow !")
        else:
            print(f"\nThe front element is : {self.front.data}")

    def rearElement(self):
        if (self.front is None and self.rear is None):
            print("\nQueue is Underflow !")
        else:
            print(f"\nThe rear element is : {self.rear.data}")

    def isEmpty(self):
        if (self.front is None and self.rear is None):
            print("\nQueue is Underflow !")

    def enqueue(self, data):
        newElement = LinkedList(data)
        if(self.rear is None):
            self.front = self.rear = newElement
        else:
            self.rear.next = newElement
            self.rear = newElement

    def dequeue(self):
        if(self.front is None):
            print("\nQueue is Underflow !")
        else:
            temp = self.front
            self.front = self.front.next
            print(f"\nDequeued element is : {temp.data}")
            temp = None

    def size(self):
        count = 0
        if (self.front is None and self.rear is None):
            print("\nQueue is Underflow !")
        else:
            temp = self.front
            while(temp != self.rear):
                count += 1
                temp = temp.next
            if(temp == self.rear):
                count += 1
        return count

    def display(self):
        if (self.front is None):
            print("\nQueue is Underflow !")
        else:
            temp = self.front
            while(temp is not None):
                print(f"{temp.data}->", end=" ")
                temp = temp.next


if __name__ == '__main__':
    Q = Queue()
    while True:
        print("\n********* Menu *********")
        print("1. enqueue ")
        print("2. dequeue ")
        print("3. size ")
        print("4. display ")
        print("5. front element ")
        print("6. rear element ")
        print("7. Exit ")
        choice = int(input("\nEnter the choice : "))
        if(choice == 1):
            data = int(input("\nEnter the data to enqueue : "))
            Q.enqueue(data)
        elif(choice == 2):
            Q.dequeue()
        elif(choice == 3):
            length = Q.size()
            print(f"\nThe length of Queue is : {length}")
        elif(choice == 4):
            Q.display()
        elif(choice == 5):
            Q.frontElement()
        elif(choice == 6):
            Q.rearElement()
        elif(choice == 7):
            break
        else:
            print("Invalid Choice !!")

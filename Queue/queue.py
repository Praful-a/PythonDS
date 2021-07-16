class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.rear = self.front = -1
        self.arr = list() * capacity
        self.size = 0

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def length(self):
        return self.size

    def frontElement(self):
        if (self.isEmpty()):
            print("Queue is Empty")
        else:
            print(f"\nThe front element is : {self.arr[self.front]}")

    def rearElement(self):
        if (self.isEmpty()):
            print("\nQueue is Underflow !")
        else:
            print(f"The rear element is : {self.arr[self.rear]}")

    def enqueue(self, data):
        if (self.isFull()):
            print("\nQueue is Overflow !")
        else:
            self.rear = self.rear + 1 % self.capacity
            self.arr.append(data)
            if(self.front == -1):
                self.front = self.rear
            self.size += 1

    def dequeue(self):
        if (self.isEmpty()):
            print("Queue is Underflow !")
        print(f"{self.arr[self.front]} is dequeued from queue")
        if(self.front == self.rear):
            self.front = self.rear = -1
            self.size = 0
        else:
            self.front = (self.front + 1) % self.capacity
            self.size -= 1

    def display(self):
        if (self.isEmpty()):
            print('\nQueue is Underflow !')
        else:
            for i in range(self.front, self.rear+1):
                print(f"{self.arr[i]}", end=" ")


if __name__ == '__main__':
    que = Queue(5)
    while True:
        print("\n********** Menu **********")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Size")
        print("5. Front element")
        print("6. Rear element")
        print("7. Exit")
        choice = int(input("\nEnter the choice : "))
        if (choice == 1):
            data = int(input("Enter the data : "))
            que.enqueue(data)
        if (choice == 2):
            que.dequeue()
        elif(choice == 3):
            que.display()
        elif(choice == 4):
            res = que.length()
            print(f"The size of queue is : {res}")
        elif(choice == 5):
            que.frontElement()
        elif(choice == 6):
            que.rearElement()
        elif (choice == 7):
            break
        else:
            print("Invalid Choice")

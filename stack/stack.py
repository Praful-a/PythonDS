top = -1
MAX = 5
stack = []

def isFull():
    return top == MAX - 1

def isEmtpy():
    return top == -1

def push(data):
    global top
    if(isFull()):
        print("\n Stack Overflow \n")
    else:
        top += 1
        stack.append(data)
        print(" Inserted Successfully ")

def pop():
    global top
    if(isEmtpy()):
        print("\n Stack Underflow \n")
    else:
        print("\n The removed element is : ", stack[top])
        top -= 1
        print(" Removed Successfully ")

def peek():
    if(isEmtpy()):
        print("\n Stack Underflow \n")
    else:
        print(" Top Element is : ", stack[top])

def display():
    if(isEmtpy()):
        print("\n Stack is Empty ")
    else:
        print("\n The stack contains : ")
        print("   ", end="")
        for cur in range(top, -1, -1):
            print(stack[cur], end=" ")
        print("\n Executed Successfully !!\n")

if __name__ == '__main__':
    while(True):
        print("\n ******** Menu ********")
        print(" 1. Insert an element in stack ")
        print(" 2. Pop an elment from stack ")
        print(' 3. Display ')
        print(" 4. Peek ")
        print(" 5. Exit ")
        choice = int(input("\n Enter the choice : "))
        if (choice == 1):
            data = int(input("\n Enter the data : "))
            push(data)
        elif (choice == 2):
            pop()
        elif (choice == 3):
            display()
        elif (choice == 4):
            peek();
        elif (choice == 5):
            print("\n !! Bye Bye !!\n")
            break
        else:
            print("\n Invalid Choice !!")


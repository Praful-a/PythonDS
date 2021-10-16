class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None;

	def push(self, data):
		newNode = Node(data)
		newNode.next = self.head
		self.head = newNode

	def deleteList(self):
		current = self.head
		while current:
			prev = current.next
			current = None
			current = prev
	
	def display(self):
		if(self.head == None):
			print("\n .. List is empty ..")
		else:
			while(self.head != None):
				print("  " + "{}".format(self.head.data), end=" ")
				self.head = self.head.next


if __name__ == '__main__':
	lst = LinkedList()
	lst.push(1)
	lst.push(2)
	lst.push(10)
	print("\n .. List Constains : ", end="")
	lst.display()
	print("\n .. Deleting the list ..")
	lst.deleteList()
	print(" .. Linked list deleted ..")
	lst.display()
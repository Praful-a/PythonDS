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
			del current.data
			current = prev


if __name__ == '__main__':
	lst = LinkedList()
	lst.push(1)
	lst.push(2)
	lst.push(10)
	print("Deleting the list")
	lst.deleteList()
	print("Linked list deleted")

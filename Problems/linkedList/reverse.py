class Node:
	def __init__(self, data):
		self.data = data
		self.next = None 

class LinkedList:
	def __init__(self):
		self.head = None 

	def push(self, data):
		newNode = Node(data)
		if self.head is None:
			self.head = newNode
		else:
			newNode.next = self.head 
			self.head = newNode

	def reverse(self):
		if self.head is None:
			print("List is empty !!")
			return 
		else:
			prev = None 
			curr = self.head 
			while curr is not None:
				next = curr.next 
				curr.next = prev 
				prev = curr 
				curr = next 
		self.head = prev 

	def printList(self):
		if self.head is None:
			print("List is empty !!")
			return  
		else:
			temp = self.head
			while temp is not None:
				print(temp.data, end=" ")
				temp = temp.next 


sll = LinkedList()
sll.push(10)
sll.push(2)
sll.push(23)
sll.printList()
sll.reverse()
print()
sll.printList()
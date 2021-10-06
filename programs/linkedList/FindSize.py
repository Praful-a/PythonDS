class Node:
	def __init__(self, data):
		self.data = data 
		self.next = None 

class SingleLinkedList:
	def __init__(self):
		self.head = None  

	def insert(self, data):
		newNode = Node(data)
		if self.head is None:
			self.head = newNode 
		else:
			temp = self.head 
			while temp.next is not None:
				temp = temp.next 
			temp.next = newNode 

	def display(self):
		temp = self.head 
		if temp is None:
			print("List is Empty !!")
		else:
			while temp is not None:
				print(f"{temp.data}", end=" ")
				temp = temp.next 

	# Iterative way to get size of list 
	def size(self):
		count = 0 
		temp = self.head 
		if temp is None:
			return 0 
		else: 
			while temp is not None:
				count += 1 
				temp = temp.next 
		return count 

	# Recursive way to get size of list
	def getSize(self, node):
		if not node:
			return 0 
		else:
			return 1 + self.getSize(node.next)

	def getCount(self):
		return self.getSize(self.head)

if __name__ == '__main__':
	sl = SingleLinkedList()
	sl.insert(10) 
	sl.insert(20)
	sl.insert(30)
	sl.display() 
	print(f"\nThe size of the list is : {sl.size()}")
	print(f"Elements in the list are : {sl.getCount()}")
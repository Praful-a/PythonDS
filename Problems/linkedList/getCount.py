class Node:
	def __init__(self, data):
		self.data = data 
		self.next = None 

class LinkedList:
	def __init__(self):
		self.head = None 

	def append(self, data):
		newNode = Node(data)
		if self.head is None:
			self.head = newNode 
		else:
			newNode.next = self.head 
			self.head = newNode 

	def size(self):
		if self.head is None:
			return 0 
		else:
			count = 0 
			temp = self.head 
			while temp is not None:
				count += 1 
				temp = temp.next 
		return count  

	def getCountRec(self, node):
		if (not node):
			return 0
		else:
			return 1 + self.getCountRec(node.next) 

	def getCount(self):
		return self.getCountRec(self.head)

	def display(self):
		if self.head is None:
			print('list is empty !!')
		else:
			temp = self.head 
			while temp is not None:
				print(temp.data, end=" ")
				temp = temp.next 


if __name__ == '__main__':
	ll = LinkedList()
	ll.append(10)
	ll.append(20)
	ll.display()
	print(f"\nThe length of list is : {ll.size()}")
	print(f"\nThe length of list is : {ll.getCount()}")
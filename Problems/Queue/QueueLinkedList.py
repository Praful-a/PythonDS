class Node:
	def __init__(self, data):
		self.data = data 
		self.next = None 

class Queue:
	def __init__(self):
		self.front = self.rear = None 

	def isEmpty(self):
		self.front == None 

	def enqueue(self, item):
		temp = Node(item)
		if self.front == None:
			self.front = self.rear = temp 
		else:
			self.rear.next = temp 
			self.rear = temp 

	def dequeue(self):
		if self.isEmpty():
			print("Queue is Underflow")
			return 
		temp = self.front
		print(f"{temp.data} is dequeued !!") 
		self.front = temp.next

		if self.front is None:
			self.rear = None 

	def display(self):
		if self.isEmpty():
			print("Queue is Underflow !!")
		temp = self.front 
		while temp is not None:
			print(temp.data, end = " ")
			temp = temp.next 

if __name__ == '__main__':
	Q = Queue()
	Q.enqueue(10)
	Q.enqueue(20)
	Q.dequeue()
	Q.display()



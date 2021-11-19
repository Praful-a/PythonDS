class Queue:
	def __init__(self, capacity):
		self.capacity = capacity
		self.front = -1
		self.rear = -1 
		self.arr = [None] * capacity
		self.size = 0 

	def isFull(self):
		return self.rear == self.capacity - 1

	def isEmpty(self):
		return self.size == 0 

	def enqueue(self, item):
		if self.isFull():
			print("The queue is Overflow !!")
			return 
		self.rear = (self.rear + 1) % self.capacity
		self.arr[self.rear] = item  
		print(f"{item} enqueued in Queue")
		if (self.front == -1):
			self.front = self.rear 
		self.size += 1

	def dequeue(self):
		if self.isEmpty():
			print("The queue is Underflow !!")
			return   
		print(f"{self.arr[self.front]} is dequeued from Queue")
		self.front = (self.front + 1) % self.capacity
		self.size -= 1

	def display(self):
		if self.isEmpty():
			print("the queue is Underflow !!")
			return  

		for cur in range(self.front, self.rear + 1):
			print(self.arr[cur], end= " ")

Q = Queue(5)
Q.enqueue(10)
Q.enqueue(12)
Q.enqueue(15)
Q.enqueue(15)
Q.enqueue(15)
Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.display()
class Stack:
	def __init__(self, capacity):
		self.capacity = capacity
		self.top = -1
		self.arr = list() * self.capacity

	def isFull(self):
		return self.top == self.capacity - 1

	def isEmpty(self):
		return self.top == -1 

	def push(self, s):
		if not self.isFull():
			self.top += 1
			self.arr.append(s)
		else:
			return "Stack is full !!"

	def pop(self):
		if not self.isEmpty():
			self.top -= 1
			return self.arr.pop()

	def reverse(self, st):
		rev = ""
		for i in st:
			self.push(i)

		while not self.isEmpty():
			rev += self.pop()
		return rev 

if __name__ == '__main__':
	st = "GeeksQuiz"
	obj = Stack(len(st))
	print(obj.reverse(st))
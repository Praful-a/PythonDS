class Evaluate:
	def __init__(self, capacity):
		self.capacity = capacity
		self.top = -1
		self.arr = list() * self.capacity

	def isFull(self):
		return self.top == self.capacity - 1

	def isEmpty(self):
		return self.top == -1 

	def push(self, e):
		if not self.isFull():
			self.top += 1
			self.arr.append(e)
		else:
			return "Stack is full !!"

	def pop(self):
		if not self.isEmpty():
			self.top -= 1 
			return self.arr.pop()
		else:
			return "Stack is empty !!"

	def evaluatePostfix(self, exp):
		for i in exp:
			if i.isdigit():
				self.push(i)
			else:
				val1 = int(self.pop())
				val2 = int(self.pop())
				switcher = {'+':val2 + val1, '-':val2 - val1, '*':val2 * val1,
							'/': val2 // val1, '^': val2 ** val1}
				self.push(switcher.get(i))
		return int(self.pop())


if __name__ == '__main__':
	exp = "231*+9-"
	# second input 
	# exp2 = '100 200 + 2 / 5 * 7 +'
	obj = Evaluate(len(exp))
	print(obj.evaluatePostfix(exp))
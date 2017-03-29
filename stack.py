class Stack(object):
	def __init__(self):
		self.data = []

	def push(self, x):
		self.data.append(x)

	def pop(self):
		if(self.isEmpty()):
			return
		return self.data.pop()

	def top(self):
		return len(self.data)

	def showStack(self):
		print(self.data)

	def isEmpty(self):
		if(len(self.data) == 0):
			return True
		return False

stack = Stack()
stack.push(3)
stack.push(4)
stack.push(5)
stack.showStack()
stack.pop()
stack.pop()
stack.showStack()
stack.push(6)
stack.showStack()
stack.pop()
stack.showStack()
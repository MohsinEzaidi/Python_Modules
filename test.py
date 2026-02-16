from abc import ABC, abstractmethod
class A(ABC):
	@abstractmethod
	def hello():
		print('Hello')

class B(A):
	def hello():
		print('Hello b')
	pass

a=A()
b = B()
print(b)
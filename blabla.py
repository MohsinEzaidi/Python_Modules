from enum import Enum
from inspect import getmembers, isfunction

class Test():
	def hello():
		pass
	def bye():
		pass

print(getmembers(Test, predicate=isfunction))

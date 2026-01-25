class ErrorS(Exception):
    def __init__(self, msg: str = 'hahahahahahahaha'):
        super().__init__(msg)

try:
    raise ValueError(['what', 1, 0.9, {'j': 55}])
except Exception as e:
    print(e.__class__.__name__)
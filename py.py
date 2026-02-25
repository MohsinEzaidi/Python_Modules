import test
try:
    print(test.__version__)
except AttributeError as e:
    print(e)
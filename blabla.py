import requests
import pandas
import matplotlib.pyplot as plt

my_request = requests.get('http://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000&count=5')
data = my_request.json()

data_frame = pandas.DataFrame(data, columns=['value'])
print(data_frame['value'])
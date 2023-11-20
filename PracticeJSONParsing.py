import json

from urllib.request import urlopen
import openurl

with openurl("http://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

# with open('file.py', 'w') as f:

data = json.loads(source)
print(data)

for item in data['']['']:
    name = item['']['']['name']
# json.dumps(tempfile, f)

# with open('file.py', 'w') as f:

# with urlopen("url") as response:
#     source = response.read()


# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }



# output = json.dumps(x)

# new_op = json.loads(output)
# #print(new_op)

# for k, v in new_op['cars']:
#     for c in k:
#         print(c)


#print(output)



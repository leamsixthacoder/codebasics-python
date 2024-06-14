# book = {}
# book['tom'] = {
#     'name': 'tom',
#     'address': '1 red street, NY',
#     'phone' : 8952855
# }
# book['bob'] = {
#     'name': 'bob',
#     'address': '1 green street, NY',
#     'phone' : 8952866
# }

# import json
# s = json.dumps(book)

# with open("C://Users//Leamsi//Documents//investing//Python//codebasics//book.txt", "w") as f:
#     f.write(s)

f = open("C://Users//Leamsi//Documents//investing//Python//codebasics//book.txt", "r")
s = f.read()

import json 
book = json.loads(s)
for person in book: 
    print(book[person])
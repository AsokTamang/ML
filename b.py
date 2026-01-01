import json

data = {'tom': {
    'name': 'tom',
    'age': 18,
    'phone': 45612313},
    'james': {
        'name': 'james',
        'age': 22,
        'phone': 123456
    }}

with open(r'C:\Users\ashok\OneDrive\Desktop\change.txt', 'w') as f: #here we are writing in the file with w and here r means the string is raw string
    (f.write(json.dumps(data)))


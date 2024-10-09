from datetime import datetime

import requests

start_time = datetime.now()
end_time = datetime.now()
print(end_time - start_time)

start_time = datetime.now()
requests.get('https://jsonplaceholder.typicode.com/posts')
end_time = datetime.now()
print(end_time - start_time)
start_time = datetime.now()
requests.get('https://jsonplaceholder.typicode.com/posts/1')
end_time = datetime.now()
print(end_time - start_time)

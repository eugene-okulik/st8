import requests


def get_all():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    # print(response.text)
    data = response.json()
    print(data)
    print(data[0])
    print(data[0]['title'])


def get_one():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/42')
    data = response.json()
    print(data['title'])


def create_publication():
    payload = {
        'title': 'foo',
        "body": "bar",
        "userId": 1
    }
    headers = {"Content-Type": 'application/json'}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=payload,
        headers=headers
    )
    print(response.json())


def update_with_put():
    payload = {
        'title': 'fooUPD',
        "body": "barUPD",
        "userId": 1
    }
    headers = {"Content-Type": 'application/json'}
    response = requests.put(
        'https://jsonplaceholder.typicode.com/posts/42',
        json=payload,
        headers=headers
    )
    print(response.json())


def update_with_patch():
    payload = {
        'title': 'fooUPD'
    }
    headers = {"Content-Type": 'application/json'}
    response = requests.patch(
        'https://jsonplaceholder.typicode.com/posts/42',
        json=payload,
        headers=headers
    )
    print(response.json())


def delete_publication():
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/42')
    print(response.status_code)

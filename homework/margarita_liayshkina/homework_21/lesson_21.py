import requests


def create_object():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post("https://api.restful-api.dev/objects", json=payload)
    if response.status_code == 200:
        object_id = response.json()["id"]
        print(f"Object created {object_id}!")
        return object_id
    else:
        print(f"Failed to create object:{response.status_code}")


def receiving_object_by_id(object_id):
    request_value = "https://api.restful-api.dev/objects?id={}".format(object_id)
    response = requests.get(request_value)
    print(response)


def update_subject_with_put():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2030,
            "price": 3000,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {"Content-Type": 'application/json'}
    response = requests.put(
        f"https://api.restful-api.dev/objects/{object_id}",
        json=payload,
        headers=headers
    )
    print(response.json())


def update_subject_with_patch():
    payload = {
        "name": "Apple MacBook Pro 20",
        "data": {
            "year": 2025,
        }
    }
    headers = {"Content-Type": 'application/json'}
    response = requests.patch(
        f"https://api.restful-api.dev/objects/{object_id}",
        json=payload,
        headers=headers
    )
    print(response.json())


def delete_subject():
    response = requests.delete(f"https://api.restful-api.dev/objects/{object_id}")
    if response.status_code == 200:
        print(f"Object with ID {object_id} deleted")
    else:
        print(f"Object with ID {object_id} not found")


object_id = create_object()
receiving_object_by_id(object_id)
update_subject_with_put()
update_subject_with_patch()
delete_subject()

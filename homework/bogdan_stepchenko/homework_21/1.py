import requests


class APIClient:

    def __init__(self, url):
        self.url = url
        self.headers = {"Content-Type": "application/json"}

    def create_object(self, name: str, year: int, price: int, cpu_model: str):
        payload = {
            "name": name,
            "data": {
                "year": year,
                "price": price,
                "CPU model": cpu_model
            }
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        if response.status_code == 200:
            print(f'Object was successfully created With id == {response.json()["id"]}')
            return response.json()['id']
        else:
            print("Failed to create object: ", response.status_code, response.text)
            return None

    def get_exact_object(self, object_id):
        response = requests.get(f'{self.url}/{object_id}')
        if response.status_code == 200:
            data = response.json()
            print(f'Object with id: {object_id} details: {data}')
        else:
            print(f'Failed to get info about object with id: {object_id}. '
                  f'{response.status_code}, {response.text}')

    def update_object_with_patch(self, object_id, name):
        payload = {"name": name}
        response = requests.patch(f'{self.url}/{object_id}',
                                  json=payload, headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            print(f'Object with id: {object_id} was updated. Details: {data}')
        else:
            print(f'Failed to update object with id: {object_id}. '
                  f'{response.status_code}, {response.text}')

    def update_object_with_put(self, object_id, name, year, price, cpu_model):
        payload = {
            "name": name,
            "data": {"year": year, "price": price, "CPU model": cpu_model}
        }
        response = requests.put(f'{self.url}/{object_id}',
                                json=payload, headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            print(f'Object with id: {object_id} was updated. Details: {data}')
        else:
            print(f'Failed to update object with id: {object_id}. '
                  f'{response.status_code}, {response.text}')

    def delete_object(self, object_id):
        response = requests.delete(f'{self.url}/{object_id}')
        if response.status_code == 200:
            data = response.json()
            print(f'Object with id: {object_id} was successfully deleted. Details: {data}')
        else:
            print(f'Failed to delete object with id: {object_id}. '
                  f'{response.status_code}, {response.text}')


if __name__ == '__main__':
    client = APIClient('https://api.restful-api.dev/objects')

    new_object = client.create_object('iPhone16', 2024, 5000, 'iCore 16')

    if new_object:
        client.get_exact_object(new_object)
        client.update_object_with_patch(new_object, 'iPhone 16 Pro')
        client.update_object_with_put(new_object, 'iPhone 16 Pro Max', 2025, 7000, 'iCore 16 Pro Max')
        client.delete_object(new_object)

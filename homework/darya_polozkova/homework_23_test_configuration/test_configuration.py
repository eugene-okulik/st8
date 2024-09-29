import pytest
import requests
from pydantic import BaseModel, Field, ValidationError


@pytest.mark.smoke
def test_get_object_by_id(set_up, start_end):
    response = requests.get(f'http://167.172.172.115:52353/object/{set_up}')
    data = response.json()
    name = data['name']
    print(f'Your newly created object is {name}')


@pytest.mark.critical
@pytest.mark.parametrize(
    'name', [
        'Param-pam Pro 16', '$&*%!#%@', '    '
    ]
    , ids=['letters', 'symbols', 'spaces']
)
def test_update_object_with_put(set_up, start_end, name):
    payload = {
        "name": name,
        "data": {
            "year": 2024,
            "price": 2000,
            "CPU model": "Put Intel Core i9",
            "Hard disk size": "100 TB"
        }
    }
    headers = {"Content-Type": 'application/json'}
    response = requests.put(
        f'http://167.172.172.115:52353/object/{set_up}',
        json=payload,
        headers=headers
    )
    data = response.json()
    assert response.status_code == 200
    assert data['name'] == payload['name']
    print(f'Updated result: {data}')


def test_update_object_with_patch(set_up, start_end):
    payload = {
        "name": "Update Unittest MacBook Pro 16",
    }
    headers = {"Content-Type": 'application/json'}
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{set_up}',
        json=payload,
        headers=headers
    )
    print(f'Your updated object data: {response.json()}')


class ObjData(BaseModel):
    year: int
    price: int
    CPU_model: str = Field(alias='CPU model')


class ObjectWithData(BaseModel):
    name: str
    data: ObjData


@pytest.mark.smoke
def test_independent_create_an_object():
    payload = {
        "name": " Real Unittest MacBook Pro 16",
        "data": {
            "year": 2050,
            "price": 3000,
            "CPU model": "M1",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post(
        'http://167.172.172.115:52353/object', json=payload
    )
    object_id = response.json()['id']
    ObjectWithData(**response.json())
    print(f"{object_id} is created")
    return object_id


class DeleteResponse(BaseModel):
    success: bool


def test_independent_delete_an_object():
    object_id = test_independent_create_an_object()
    response = requests.delete(f'http://167.172.172.115:52353/object/{object_id}')
    print(f'Object is deleted with ID {object_id}')
    try:
        validated_response = DeleteResponse(**{'success': response})
        assert validated_response.success is True, f'Object with id {object_id} successfully deleted'
    except ValidationError as exc:
        print(repr(exc.errors()[0]['type']))

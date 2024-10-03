from api_tests_bstepchenko.data.randomizer import get_random_int, get_random_str

HEADERS = {"Content-Type": "application/json"}
BASE_URL = "http://167.172.172.115:52353/object"
PAYLOAD_FOR_OBJECT = {
    "name": get_random_str(),
    "data": {
        "year": get_random_int(),
        "price": get_random_int(),
        "CPU model": get_random_str(),
    },
}

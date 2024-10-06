from api_tests_msorokin.data.helpers import FakeData, Generator


class ObjectApiJson:

    @staticmethod
    def create_object_request_body_generated_json():
        payload = {
            "name": FakeData.RANDOM_WORD(),
            "data": {
                "year": FakeData.RANDOM_DATE(),
                "price": FakeData.RANDOM_INT(),
                "cpu_model": f"{FakeData.RANDOM_WORD()} core",
                "hard_disk_size": f"{Generator.memory_size_generator()} {Generator.memory_type_generator()}"
            }
        }
        return payload

    @staticmethod
    def create_object_request_body_parametrized_json(name, year, price, cpu_model, disk):
        payload = {
            "name": name,
            "data": {
                "year": year,
                "price": price,
                "cpu_model": cpu_model,
                "hard_disk_size": disk
            }
        }
        return payload

    @staticmethod
    def partial_update_name_json(name):
        payload = {"name": name}
        return payload

class BaseApi:
    def __init__(self):
        self.payload = None
        self.response = None
        self.response_json = None

    def check_response_code_is_(self, code):
        assert self.response.status_code == code

    def check_updated_name(self):
        assert self.response_json['name'] == self.payload['name']

    def check_updated_year(self):
        assert self.response_json['data']['year'] == self.payload['data']['year']

    def check_updated_price(self):
        assert self.response_json['data']['price'] == self.payload['data']['price']

    def check_updated_cpu_model(self):
        assert self.response_json['data']['CPU model'] == self.payload['data']['CPU model']

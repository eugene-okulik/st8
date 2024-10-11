from abc import abstractmethod


class BaseApi:
    def __init__(self):
        self.payload = None
        self.response = None
        self.response_json = None

    def check_response_code_is_(self, code):
        assert self.response.status_code == code

    @abstractmethod
    def data(self):
        pass

    def response_json(self):
        return self.response.json()

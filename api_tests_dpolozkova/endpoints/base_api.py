from abc import abstractmethod

import allure
from requests import Response


class BaseApi:
    response: Response

    @allure.step("Check response status code")
    def check_response_code_is_(self, code):
        assert self.response.status_code == code

    # property привращает результат функции в переменную
    # проверят вычитку респонса
    @property
    def response_json(self):
        return self.response.json()

    @property
    @abstractmethod
    # означает что во всех подклассах должна быть реализванно
    def data(self):
        pass

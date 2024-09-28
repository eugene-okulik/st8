import parametrization
import pytest
import requests
from helpers import NegativeCases


class TestHomework23Negative:
    API_URL = "http://167.172.172.115:52353/object"

    # очень удобен для негативных тестов когда статус коды могут быть разные в зависимости от того что передали
    # Но и для обычных сойдет.
    @pytest.mark.critical
    @parametrization.Parametrization.parameters("year", "expected")
    @parametrization.Parametrization.case("TOO_HEAVY_INTEGER", NegativeCases.TOO_HEAVY_INTEGER, 500)
    @parametrization.Parametrization.case("NEGATIVE_NUMBER", NegativeCases.NEGATIVE_NUMBER, 400)
    @parametrization.Parametrization.case("SYMBOL_IN_STRING", NegativeCases.SYMBOL_IN_STRING, 400)
    @parametrization.Parametrization.case("space int string", NegativeCases.STRING_SPACE, 400)
    @parametrization.Parametrization.case("BOOL_FALSE", NegativeCases.BOOL_FALSE, 400)
    @parametrization.Parametrization.case("BOOL_TRUE", NegativeCases.BOOL_TRUE, 400)
    @parametrization.Parametrization.case("VERY_LONG_STRING", NegativeCases.VERY_LONG_STRING, 500)
    @parametrization.Parametrization.case("FLOAT in value", NegativeCases.FLOAT, 400)
    @parametrization.Parametrization.case("LIST in value", NegativeCases.LIST, 400)
    @parametrization.Parametrization.case("OBJECT in value", NegativeCases.OBJECT, 500)
    def test_update_object_year_negative(self, year, expected):
        payload = {
            "name": "test",
            "data": {
                "year": year,
                "price": 1999.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "2 TB"
            }
        }
        response = requests.put(f"{self.API_URL}/{74}", json=payload)
        assert response.status_code == expected, f"Ошибка при обновлении объекта (PUT): {response.status_code}"

import pytest
import random
import allure


@allure.feature('Simple cases')
@pytest.mark.simple
def test_demo1(greet, for_simple):
    print(for_simple)
    assert 1 == random.randint(1, 3)


@allure.feature('Simple cases')
@pytest.mark.simple
def test_demo2(greet, for_simple):
    assert 1 == 1

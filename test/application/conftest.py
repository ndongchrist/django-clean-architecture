import pytest

# declare fixtures here to test the create and list usecases
@pytest.fixture
def car_repository_mock():
    class CarRepositoryMock:
        def __init__(self):
            self.cars = []

        def create(self, car):
            self.cars.append(car)

        def list_all(self):
            return self.cars

    return CarRepositoryMock()
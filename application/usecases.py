from domain.models import Car

class CreateCarUseCase:
    def __init__(self, car_repository):
        self.car_repository = car_repository

    def execute(self, car_data):
        car = Car(**car_data)
        self.car_repository.create(car)
        
class ListCarUseCase:
    def __init__(self, car_repository):
        self.car_repository = car_repository

    def execute(self):
        return self.car_repository.list_all()
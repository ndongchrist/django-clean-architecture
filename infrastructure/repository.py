from domain.models import Car
from interface.models import CarModel

class CarRepository:
    def create(self, car: Car):
        car_model = CarModel(
            model=car.model,
            year=car.year,
            color=car.color,
            speed=car.speed
        )
        car_model.save()
        return car_model

    def list_all(self):
        cars = CarModel.objects.all()
        return [Car(model=car.model, year=car.year, color=car.color, speed=car.speed) for car in cars]
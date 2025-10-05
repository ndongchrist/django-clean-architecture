from django.shortcuts import render
from infrastructure.repository import CarRepository
from application.usecases import CreateCarUseCase, ListCarUseCase

# Create your views here.
def create_car(request):
    if request.method == 'POST':
        model = request.POST.get('model')
        year = int(request.POST.get('year'))
        color = request.POST.get('color')
        speed = float(request.POST.get('speed'))
        car_data = {
            'model': model,
            'year': year,
            'color': color,
            'speed': speed,
            'csrfmiddlewaretoken': request.POST.get('csrfmiddlewaretoken')
        }
        repository = CarRepository()
        use_case = CreateCarUseCase(repository)
        use_case.execute(car_data)
    return render(request, 'create_car.html')

def list_cars(request):
    repository = CarRepository()
    use_case = ListCarUseCase(repository)
    cars = use_case.execute()
    return render(request, 'list_cars.html', {'cars': cars})

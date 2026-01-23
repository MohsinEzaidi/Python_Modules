class GardenError(Exception):
    counter = 1
    pass

class PlantError(GardenError):
    counter = 1
    pass

class WaterError(GardenError):
    counter = 1
    pass


class Garden:
    
    class Plant:
        def __init__(self, name: str, is_wilting: bool) -> None:
            self.name = name
            self.is_wilting = is_wilting

        def test_plant(self) -> None:
            if self.is_wilting:
                raise PlantError(f'Caught PlantError: The {self.name} plant is wilting!')
            else:
                print(f'The {self.name} is NOT wilting, No PlantError')


    class WaterTank:
        def __init__(self, liters: int) -> None:
            self.liters = liters

        def test_water_tank(self):
            if self.liters < 1:
                raise WaterError('Caught WaterError: Not enough water in the tank!')
            else:
                print(f'The water tank has enaugh water ({self.liters}L), No WaterError')


    def water_plant(plant: Plant, water_tank: WaterTank) -> None:
        if water_tank.liters < 1 and plant.is_wilting:
            raise GardenError(f'Caught a garden error: The {plant.name} plant is wilting!\n'
                              'Caught a garden error: Not enough water in the tank!')
        else:
            plant.test_plant()
            water_tank.test_water_tank()
            water_tank.liters -= 1
            print(f'{plant.name.capitalize()} been watered, No GardenError')


def main() -> None:
    print('=== Custom Garden Errors Demo ===')
    tomato = Garden.Plant('tomato', True)
    water_tank = Garden.WaterTank(-10)
    try:
        try:
            print('\nTesting PlantError...')
            tomato.test_plant()
        except GardenError as e:
            print(e)

        try:
            print('\nTesting WaterError...')
            water_tank.test_water_tank()
        except GardenError as e:
            print(e)

        try:
            print('\nTesting catching all garden errors...')
            Garden.water_plant(tomato, water_tank)
        except GardenError as e:
            print(e)
    except Exception as e:
        print(f'Caught an error "{e.__class__.__name__}"!!')
    print('\nAll custom error types work correctly!')


if __name__ == '__main__':
    main()

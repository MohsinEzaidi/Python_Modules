class GardenError(Exception):
    """Base exception for all garden related errors."""
    def __init__(self, msg: str = 'Caught GardenError') -> None:
        """Create a GardenError message"""
        super().__init__(msg)


class PlantError(GardenError):
    """Raised when a plant related problem occurs."""
    def __init__(self, msg: str = 'Caught PlantError') -> None:
        """Create a PlantError message"""
        super().__init__(msg)


class WaterError(GardenError):
    """Raised when a water related problem occurs."""
    def __init__(self, msg: str = 'Caught WaterError') -> None:
        """Create a WaterError message"""
        super().__init__(msg)


class Garden:
    """Represents a garden containing plants and water resources."""
    class Plant:
        """Represents a plant in the garden."""
        def __init__(self, name: str, is_wilting: bool) -> None:
            """Initialize a plant with its name and wilting state."""
            self.name = name
            self.is_wilting = is_wilting

        def test_plant(self) -> None:
            """Check if the plant is wilting and raise PlantError if needed."""
            if self.is_wilting:
                raise PlantError('Caught PlantError: The'
                                 f'{self.name} plant is wilting!')
            else:
                print(f'The {self.name} is NOT wilting, No PlantError')

    class WaterTank:
        """Represents a water tank in the garden."""
        def __init__(self, liters: int) -> None:
            """Initialize the water tank with a given amount of water."""
            self.liters = liters

        def test_water_tank(self):
            """Check if the water tank has enough water."""
            if self.liters < 1:
                raise WaterError('Caught WaterError: Not'
                                 'enough water in the tank!')
            else:
                print('The water tank has enaugh water '
                      f'({self.liters}L), No WaterError')


def water_plant(plant: Garden.Plant, water_tank: Garden.WaterTank) -> None:
    """Water a plant or raise a GardenError if conditions are not met."""
    if water_tank.liters < 1 and plant.is_wilting:
        raise GardenError(f'Caught a garden error: The {plant.name} plant',
                          'is wilting!\nCaught a garden error: Not',
                          'enough water in the tank!')
    else:
        plant.test_plant()
        water_tank.test_water_tank()
        water_tank.liters -= 1
        print(f'{plant.name.capitalize()} been watered, No GardenError')


if __name__ == '__main__':
    print('=== Custom Garden Errors Demo ===')
    tomato = Garden.Plant('tomato', True)
    water_tank = Garden.WaterTank(-10)
    try:
        try:
            print('\nTesting PlantError...')
            tomato.test_plant()
        except PlantError as e:
            print(e)

        try:
            print('\nTesting WaterError...')
            water_tank.test_water_tank()
        except WaterError as e:
            print(e)

        try:
            print('\nTesting catching all garden errors...')
            Garden.water_plant(tomato, water_tank)
        except GardenError as e:
            print(e)
    except Exception as e:
        print(f'Caught an error "{e.__class__.__name__}"!!')
    print('\nAll custom error types work correctly!')

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water_level: int, sunlight_hours: int) -> None:
        self._name = name
        self._water_level = water_level
        self._sunlight_hours = sunlight_hours

    def get_name(self) -> str:
        return self._name

    def get_water_level(self) -> int:
        return self._water_level

    def set_water_level(self, new_water_level: int) -> None:
        self._water_level = new_water_level

    def get_sunlight_hours(self) -> int:
        return self._sunlight_hours


class GardeMannager:
    def __init__(self, name: str, water_tank: int) -> None:
        self.name = name
        self._water_tank = water_tank
        self._plants_list = []

    def get_plants_list(self) -> list[Plant]:
        return self._plants_list

    def get_water_tank(self) -> int:
        return self._water_tank
    
    def set_water_tank(self, new_water_tank) -> None:
        self._water_tank = new_water_tank

    def add_plant(self, new_plant: Plant) -> None:
        if new_plant.get_name() == '':
            raise PlantError('Error adding plant: Plant name cannot be empty!')
        else:
            self.get_plants_list().append(new_plant)
            print(f'Added {new_plant.get_name()} successfully')

    def water_plants(self) -> None:
        print('Opening watering system')
        total_plants = self.get_plants_list().__len__()
        if total_plants == 0:
            raise GardenError('Error: There are no plants in the garden')
        if total_plants > self.get_water_tank():
            raise GardenError('Caught GardenError: Not enough water in tank')
        for plant in self.get_plants_list():
            print(f'Watering {plant.get_name()} - success')
            plant.set_water_level(plant.get_water_level() + 1)

    def check_plants_health(self) -> None:
        if self.get_plants_list().__len__() == 0:
            raise GardenError('Error: There are no plants in the garden')
        for plant in self.get_plants_list():
            if plant.get_water_level() > 10:
                raise GardenError(f'Error checking {plant.get_name()}: Water level {plant.get_water_level()} is too high (max 10)')
            if plant.get_water_level() < 1:
                raise GardenError(f'Error checking {plant.get_name()}: Water level {plant.get_water_level()} is too low (min 1)')
            if plant.get_sunlight_hours() > 12:
                raise GardenError(f'Error checking {plant.get_name()}: Sunlight hours {plant.get_sunlight_hours()} is too high (min 12)')
            if plant.get_sunlight_hours() < 2:
                raise GardenError(f'Error checking {plant.get_name()}: Sunlight hours {plant.get_sunlight_hours()} is too low (min 2)')
            print(f'{plant.get_name()}: healthy (water: {plant.get_water_level()}, sun: {plant.get_sunlight_hours()})')


def test_garden_management() -> None:
    garden = GardeMannager('my garden', 10)
    print('\nAdding plants to garden...')
    try:
        garden.add_plant(Plant('tomato', 4, 4))
        garden.add_plant(Plant('lettuce', 4, 4))
        garden.add_plant(Plant('', 4, 4))
    except GardenError as e:
        print(e)
    try:
        print('\nWatering plants...')
        garden.water_plants()
    except GardenError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")
    try:
        print('\nChecking plant health...')
        garden.check_plants_health()
    except GardenError as e:
        print(e)
    try:
        print('\nTesting error recovery...')
        garden.set_water_tank(0)
        garden.water_plants()
    except GardenError as e:
        print(e)
    print('System recovered and continuing...')

def main() -> None:
    print('=== Garden Management System ===')
    try:
        test_garden_management()
    except Exception as e:
        print(f'\nCaught {e.__class__.__name__}')
    print('\nGarden management system test complete!')

if __name__ == '__main__':
    main()
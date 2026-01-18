class GardenManager:
    """
    A class to manage multiple gardners and there garden
    and show information about plants in that garden.
    """
    total_managers = 0
    managers = []

    def __init__(self, name: str) -> None:
        """
        Make a new Garden Manager and create an empty garden for them.
        """
        self.name = name
        self.garden = []
        self.managers.append(self.name)
        self.initial_heights = []
        self.plant_added = 0
        GardenManager.total_managers += 1

    class GardenStats:
        """
        A nested class to help manging the garden.
        """
        total = 0

        def calculate_total_growth(initial_heights: list, garden: list) -> int:
            """
            Find out how much all plants grew in total.
            """
            i = 0
            total = GardenManager.GardenStats.total
            for plant in garden:
                total += (plant.height - initial_heights[i])
                i += 1
            return total
        calculate_total_growth = staticmethod(calculate_total_growth)

    def create_garden_network(cls, names_list: list):
        """
        Create a list of new garden managers at once.
        """
        return [cls(name) for name in names_list]

    create_garden_network = classmethod(create_garden_network)

    def help_all_plants(self, cm: int):
        """
        Increase the height of all plants by the cm:int amount.
        """
        print(f'\n{self.name} is helping all plants grow...')
        for plant in self.garden:
            plant.grow(cm)

    def add_plant(self, plant):
        """
        Add a new plant to the Garden Manger's garden.
        """
        self.garden.append(plant)
        self.plant_added += 1
        self.initial_heights.append(plant.height)
        print(f'Added {plant.name} to {self.name}\'s garden')

    def get_report(self):
        """
        Show a full report of what is inside the garden.
        """
        regular = 0
        flowering = 0
        prize_flowers = 0
        print()
        for plant in self.garden:
            if plant.__class__.__name__ == 'Plant':
                regular += 1
            if plant.__class__.__name__ == 'FloweringPlant':
                flowering += 1
            if plant.__class__.__name__ == 'PrizeFlower':
                prize_flowers += 1
            plant.get_info()
        print(f'\n=== {self.name}\'s Garden Report ===')
        print('Plants in garden:')
        for plant in self.garden:
            plant.get_info()
        print(f'\nPlants added: {self.plant_added}, Total growth: ',
              self.GardenStats.calculate_total_growth(self.initial_heights,
                                                      self.garden),
              'cm', sep='')
        print(f'Plant types: {regular} regular, {flowering} flowering,',
              f'{prize_flowers} prize flowers\n')

    def calculate_score(self) -> int:
        """
        Calculate the total points for the garden.
        """
        score = 0
        for plant in self.garden:
            if plant.__class__.__name__ == 'PrizeFlower':
                score += plant.points
            score += plant.height + 10
        return score

    def height_validation(self) -> None:
        """
        Check if all plants have a correct height (not negative).
        """
        for plant in self.garden:
            if plant.height < 0:
                return print('Height validation test: False')
        return print('Height validation test: True')

    def get_score(managers):
        """
        Show the points of all garden managers.
        """
        print("Garden scores - ", end='')
        first = True
        for manager in managers:
            if not first:
                print(", ", end='')
            print(f"{manager.name}: {manager.calculate_score()}", end='')
            first = False
        print()
    get_score = staticmethod(get_score)

    def get_gardens_managed():
        """
        Show how many gardens are being managed in total.
        """
        print(f'Total gardens managed: {GardenManager.total_managers}')
    get_gardens_managed = staticmethod(get_gardens_managed)


class Plant:
    """
    A class for a basic plant.
    """
    def __init__(self, name: str, height: int) -> None:
        """
        Set the name and height of the plant.
        """
        self.name = name
        self.height = height

    def grow(self, cm: int):
        """
        Add more height to the plant.
        """
        self.height += cm
        print(f'{self.name} grew {cm}cm')

    def get_info(self):
        """
        Show information about the plant.
        """
        print(f'- {self.name}: {self.height}cm')


class FloweringPlant(Plant):
    """
    A class for a flower plant
    """
    def __init__(self, name: str, height: int, color: str) -> None:
        """
        Set the flower with a plant info + color.
        """
        super().__init__(name, height)
        self.color = color

    def get_info(self):
        """
        Show plant info including the flower color.
        """
        print(f'- {self.name}: {self.height}cm, '
              f'{self.color} flowers (blooming)')


class PrizeFlower(FloweringPlant):
    """
    Set the prize flower with a flower info + points.
    """
    def __init__(self, name: str, height: int,
                 color: str, points: int) -> None:
        super().__init__(name, height, color)
        self.points = points

    def get_info(self):
        """
        Show flower info including the points.
        """
        print(f'- {self.name}: {self.height}cm, ',
              f'{self.color} flowers (blooming), Prize points: {self.points}')


def main() -> None:
    """
    The main part of the program to run the demo.
    """
    oak = Plant('Oak tree', 100)
    rose = FloweringPlant('Rose', 25, 'red')
    sunflower = PrizeFlower('Sunflower', 50, 'yellow', 10)
    managers = GardenManager.create_garden_network(['Alice', 'Bob'])
    alice = managers[0]

    print('=== Garden Management System Demo ===\n')
    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)
    alice.help_all_plants(1)
    alice.get_report()
    alice.height_validation()
    GardenManager.get_score(managers)
    GardenManager.get_gardens_managed()


if __name__ == '__main__':
    main()

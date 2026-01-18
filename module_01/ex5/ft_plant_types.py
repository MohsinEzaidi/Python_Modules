class Plant:
    """A class representing a plant in the garden."""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        """Prints common info about the plant."""
        print(self.name.capitalize(), f'{self.height}cm, {self.age} days')


class Flower(Plant):
    """A class representing a flower in the garden
    and inherits from class Plant."""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Inherits the attributes of the class Plant."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Display that the flower is blooming beautifully."""
        print(f'{self.name.capitalize()} is blooming beautifully!\n')

    def get_info(self):
        """Method to show info of a flower."""
        print(self.name.capitalize(), '(Flower):',
              f'{self.height}cm, {self.age} days,',
              f'{self.color} color')
        self.bloom()


class Tree(Plant):
    """A class representing a Tree in the garden
    and inherits from class Plant."""
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """Inherits the attributes of the class Plant."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Calculate and display the square meters of shade."""
        shade = 3.14 * ((self.trunk_diameter / 10)**2)
        print(f'{self.name.capitalize()} provides',
              f'{shade:.0f} square meters of shade\n')

    def get_info(self):
        """Method to show info of a tree"""
        print(self.name.capitalize(), '(Tree):',
              f'{self.height}cm, {self.age} days,',
              f'{self.trunk_diameter}cm diameter')
        self.produce_shade()


class Vegetable(Plant):
    """A class representing a Vegetable in the garden
    and inherits from class Plant."""
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """Inherits the attributes of the class Plant."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        """Method to show info of a vegetable."""
        print(self.name.capitalize(), '(Vegetable):',
              f'{self.height}cm, {self.age} days,',
              f'{self.harvest_season} harvest')
        print(f'{self.name.capitalize()}',
              f'is rich in vitamin {self.nutritional_value}\n')


def main() -> None:
    """Function to show diferent types of plants."""
    rose = Flower('rose', 25, 30, 'red')
    oak = Tree('oak', 500, 1825, 50)
    tomato = Vegetable('Tomato', 80, 90, 'summer', 'C')
    tulip = Flower('tulip', 40, 20, 'yellow')
    pine = Tree('pine', 800, 3000, 70)
    carrot = Vegetable('Carrot', 30, 60, 'winter', 'A')
    print('=== Garden Plant Types ===\n')
    rose.get_info()
    tulip.get_info()
    oak.get_info()
    pine.get_info()
    tomato.get_info()
    carrot.get_info()


if __name__ == '__main__':
    main()

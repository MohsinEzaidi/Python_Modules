class Plant:
    """A class representing a plant in the garden."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes the plant attributes."""
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm: int) -> None:
        """Increases the height of the plants by the value u provide."""
        self.height += cm

    def age(self) -> None:
        """Increases the plant's age by one."""
        self.age += 1

    def get_info(self) -> None:
        """Prints the plant details in an organized way."""
        print(f'{self.name.capitalize()}: {self.height}cm, {self.age} day old')


def main():
    plant = Plant('rose', 25, 30)
    old_height = plant.height
    print('=== Day 1 ===')
    plant.get_info()
    for i in range(1, 7):
        Plant.age(plant)
        plant.grow(1)
    print(f'=== Day {i + 1} ===')
    plant.get_info()
    print(f'Growth this week: +{plant.height - old_height}cm')


if __name__ == '__main__':
    main()

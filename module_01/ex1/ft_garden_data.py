class Plant:
    """A class representing a plant in the garden."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes the plant attributes."""
        self.name = name
        self.height = height
        self.age = age

    def print_plant(self):
        """Prints the plant details in an organized way."""
        print(f'{self.name.capitalize()}: {self.height}cm, {self.age} day old')


def main():
    plant1 = Plant('Rose', 25, 30)
    plant2 = Plant('Sunflower', 80, 45)
    plant3 = Plant('Cactus', 15, 120)
    print('=== Garden Plant Registry ===')
    plant1.print_plant()
    plant2.print_plant()
    plant3.print_plant()


if __name__ == '__main__':
    main()

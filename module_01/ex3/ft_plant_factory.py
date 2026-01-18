class Plant:
    """A class representing a plant in the garden."""
    """Initialize the plants counter."""
    counter = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes the plant attributes."""
        self.name = name
        self.height = height
        self.age = age
        """Increases the counter by 1 each time we create a new object."""
        Plant.counter += 1

    def created_msg(self) -> None:
        """Prints the plant details in an organized way."""
        print(f'Created: {self.name} ({self.height}cm, {self.age} days)')


def main() -> None:
    print('=== Plant Factory Output ===')
    plant1 = Plant('Rose', 25, 30)
    plant2 = Plant('Oak', 200, 365)
    plant3 = Plant('Cactus', 5, 90)
    plant4 = Plant('Sunflower', 80, 45)
    plant5 = Plant('Fern', 25, 30)
    plants = [plant1, plant2, plant3, plant4, plant5]
    for i in range(Plant.counter):
        plants[i].created_msg()
    print(f'\nTotal plants created: {Plant.counter}')


if __name__ == '__main__':
    main()

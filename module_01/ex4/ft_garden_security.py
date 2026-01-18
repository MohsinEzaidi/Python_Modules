class SecurePlant:
    """A class representing a plant in the garden."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes the plant attributes."""
        self.name = name
        """These attribute considered a private attributes."""
        self._height = height
        self._age = age

    def get_height(self) -> int:
        """Access the private attribute _height and return its value."""
        return self._height

    def set_height(self, new_height: int) -> None:
        """Prints an error msg if height given is negative."""
        """Change the value of the height if the new_height is positive."""
        if new_height < 0:
            print('Invalid operation attempted: ', end='')
            print(f'height {new_height}cm [REJECTED]')
            print('Security: Negative height rejected')
        else:
            self._height = new_height
            print(f'Height updated: {new_height}cm [OK]')

    def get_age(self) -> None:
        """Access the private attribute _age and return its value."""
        return self._age

    def set_age(self, new_age: int) -> None:
        """Prints an error msg if age given is negative."""
        """Change the value of the age if the new_age is positive."""
        if new_age < 0:
            print('Invalid operation attempted: age', end='')
            print(f'{new_age} days [REJECTED]')
            print('Security: Negative age rejected')
        else:
            self._age = new_age
            print(f'age updated: {new_age} days [OK]')


def main() -> None:
    plant1 = SecurePlant('Rose', 23, 50)
    print('=== Garden Security System ===')
    print(f'Plant created: {plant1.name}')
    plant1.set_height(25)
    plant1.set_age(30)
    print()
    plant1.set_height(-9)
    print()
    print(f'Current plant: {plant1.name} ', end='')
    print(f'({plant1.get_height()}cm, {plant1.get_age()} days)')


if __name__ == '__main__':
    main()

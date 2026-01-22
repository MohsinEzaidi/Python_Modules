def ft_garden_intro() -> None:
    """Displays information about a plant in the garden."""
    name = "Rose"
    height = 25
    age = 30
    print('=== Welcome to My Garden ===')
    print(f'Plant: {name}\nHeight: {height}cm\nAge: {age} days', end='\n\n')
    print('=== End of Program ===')


if __name__ == "__main__":
    ft_garden_intro()

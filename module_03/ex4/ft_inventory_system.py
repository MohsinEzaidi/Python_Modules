# $> python3 ft_inventory_system.py sword:1 potion:5 shield:2 armor:3 helmet:1
# === Inventory System Analysis ===
# Total items in inventory: 12
# Unique item types: 5

# === Current Inventory ===
# potion: 5 units (41.7%)
# armor: 3 units (25.0%)
# shield: 2 units (16.7%)
# sword: 1 unit (8.3%)
# helmet: 1 unit (8.3%)

# === Inventory Statistics ===
# Most abundant: potion (5 units)
# Least abundant: sword (1 unit)

# === Item Categories ===
# Moderate: {'potion': 5}
# Scarce: {'sword': 1, 'shield': 2, 'armor': 3, 'helmet': 1}

# === Management Suggestions ===
# Restock needed: ['sword', 'helmet']

# === Dictionary Properties Demo ===
# Dictionary keys: ['sword', 'potion', 'shield', 'armor', 'helmet']
# Dictionary values: [1, 5, 2, 3, 1]
# Sample lookup - 'sword' in inventory: True

from sys import argv as av

def parsing_dictionary() -> dict:
    ac = len(av)
    if ac < 1:
        raise Exception('Parsing Error: no arguments were previded')
    enventory = dict()
    for a in av[1:]:
        enventory_item = a.split(':')
        if len(enventory_item) != 2:
            raise Exception(f'Parsing Error: Invalid argument your argument should look like this "key:value"')
        if int(enventory_item[1]) < 0:
            raise Exception('Parsing Error: quantity cannot be a negative value')
        if enventory_item[0].strip() == '':
            raise Exception('Parsing Error: key name cannot me empty string')
        enventory[enventory_item[0]] = int(enventory_item[1])
    return enventory


def total_items(enventory: dict) -> int:
    total = 0
    for quantity in enventory.values():
        total += quantity
    return total


def calculate_percentage(enventory: dict, key: str) -> float:
    total = total_items(enventory)
    item_quantity = enventory.get(key)
    return (item_quantity/total) * 100


def least_abundant_item(enventory: dict) -> dict:
    least_abundant_item = ""
    min_quantity = float('inf')
    for item, quantity in enventory.items():
        if quantity < min_quantity:
            min_quantity = quantity
            least_abundant_item = item
    return {least_abundant_item: min_quantity}


def most_abundant_item(enventory: dict) -> dict:
    most_abundant_item = ""
    max_quantity = -1
    for item, quantity in enventory.items():
        if quantity > max_quantity:
            max_quantity = quantity
            most_abundant_item = item
    return {most_abundant_item: max_quantity}


def get_item_categories(enventory: dict) -> dict:
    categories = {"Moderate": {}, "Scarce": {}}
    for item, quantity in enventory.items():
        if quantity >= 5:
            categories["Moderate"][item] = quantity
        else:
            categories["Scarce"][item] = quantity
    return categories


def management_suggestions(enventory: dict) -> list:
    suggestions = []
    for item, quantity in enventory.items():
        if quantity < 2:
            suggestions.append(item)
    return suggestions


def properties_demo(sample: str, enventory: dict) -> None:
    keys = [*enventory.keys()]
    values = [*enventory.values()]
    print(f'Dictionary keys: {keys}')
    print(f'Dictionary values: {values}')
    print(f'Sample lookup - \'{sample}\' in inventory: {sample in enventory}')


def main() -> None:
    enventory = parsing_dictionary()
    print('=== Inventory System Analysis ===')
    print(f'Total items in inventory: {total_items(enventory)}')
    print(f'Unique item types: {len(enventory)}')

    print('\n=== Current Inventory ===')
    for item, quantity in enventory.items():
        print(f'{item}: {quantity} units ({calculate_percentage(enventory, item):.1f}%)')

    print('\n=== Inventory Statistics ===')
    most_abundant = most_abundant_item(enventory)
    least_abundant = least_abundant_item(enventory)
    (most_key, most_value), = most_abundant.items()
    (least_key, least_value), = least_abundant.items()
    print(f'Most abundant: {most_key} ({most_value} units)')
    print(f'Least abundant: {least_key} ({least_value} units)')

    print(f'\n=== Item Categories ===')
    categories = get_item_categories(enventory)
    for item, value in categories.items():
        print(f'{item}: {value}')

    print('\n=== Management Suggestions ===')
    suggestions = management_suggestions(enventory)
    print(f'Restock needed: {suggestions}')

    print('\n=== Dictionary Properties Demo ===')
    properties_demo('sword', enventory)



if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)

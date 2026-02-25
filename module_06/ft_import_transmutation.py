print('\n=== Import Transmutation Mastery ===')

print('\nMethod 1 - Full module import:')
import alchemy.elements
try:
    print(f'alchemy.elements.create_fire(): {alchemy.elements.create_fire()}')
except Exception:
    print('Exception occurred, but program continues')

print('\nMethod 2 - Specific function import:')
from alchemy.elements import create_water
try:
    print(f'create_water(): {create_water()}')
except Exception:
    print('Exception occurred, but program continues')

print('\nMethod 3 - Aliased import:')
from alchemy.potions import healing_potion as heal
try:
    print(f'heal(): {heal()}')
except Exception:
    print('Exception occurred, but program continues')

print('\nMethod 4 - Multiple imports:')
from alchemy.elements import create_fire, create_earth
from alchemy.potions import strength_potion
try:
    print(f'create_earth(): {create_earth()}')
    print(f'create_fire(): {create_fire()}')
    print(f'strength_potion(): {strength_potion()}')
except Exception:
    print('Exception occurred, but program continues')

print('\nAll import transmutation methods mastered!')

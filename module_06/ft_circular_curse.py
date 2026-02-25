import alchemy.grimoire as grimoire

print('\n=== Circular Curse Breaking ===')

print('\nTesting ingredient validation:')
print(f'validate_ingredients("fire air"): {grimoire.validate_ingredients("fire air")}')
print(f'validate_ingredients("dragon scales"): {grimoire.validate_ingredients("dragon scales")}')

print('\nTesting spell recording with validation:')
print(f'record_spell("Fireball", "fire air"): {grimoire.record_spell("Fireball", "fire air")}')
print(f'record_spell("Dark Magic", "shadow"): {grimoire.record_spell("Dark Magic", "shadow")}')
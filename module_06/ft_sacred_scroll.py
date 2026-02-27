import alchemy

print('\n=== Sacred Scroll Mastery ===')

print('\nTesting direct module access:')

try:
    print(f'alchemy.elements.create_fire(): {alchemy.elements.create_fire()}')
except Exception:
    print('Exception occurred, but program continues')

try:
    print('alchemy.elements.create_water()'
          f': {alchemy.elements.create_water()}')
except Exception:
    print('Exception occurred, but program continues')

try:
    print('alchemy.elements.create_earth()'
          f': {alchemy.elements.create_earth()}')
except Exception:
    print('Exception occurred, but program continues')

try:
    print(f'alchemy.elements.create_air(): {alchemy.elements.create_air()}')
except Exception:
    print('Exception occurred, but program continues')


print('\nTesting package-level access (controlled by __init__.py):')

try:
    print(f'alchemy.create_fire(): {alchemy.create_fire()}')
except AttributeError:
    print('alchemy.create_fire(): AttributeError - not exposed')
except Exception:
    print('Exception occurred, but program continues')

try:
    print(f'alchemy.create_water(): {alchemy.create_water()}')
except AttributeError:
    print('alchemy.create_water(): AttributeError - not exposed')
except Exception:
    print('Exception occurred, but program continues')

try:
    print(f'alchemy.create_earth(): {alchemy.create_earth()}')
except AttributeError:
    print('alchemy.create_earth(): AttributeError - not exposed')
except Exception:
    print('Exception occurred, but program continues')

try:
    print(f'alchemy.create_air(): {alchemy.create_air()}')
except AttributeError:
    print('alchemy.create_air(): AttributeError - not exposed')
except Exception:
    print('Exception occurred, but program continues')

print('\nPackage metadata:')

try:
    print(f'Version: {alchemy.__version__}')
except AttributeError as e:
    print(e)
except Exception:
    print('Exception occurred, but program continues')

try:
    print(f'Author: {alchemy.__author__}')
except AttributeError as e:
    print(e)
except Exception:
    print('Exception occurred, but program continues')

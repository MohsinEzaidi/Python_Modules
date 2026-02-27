try:
    from .py import cast_spell
    from .test import validate_spell
    cast_spell
    validate_spell
except ImportError as e:
    print(e)
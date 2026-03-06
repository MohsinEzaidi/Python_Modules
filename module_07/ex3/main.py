print('\n=== DataDeck Game Engine ===')
try:
    from .GameEngine import GameEngine
    from .FantasyCardFactory import FantasyCardFactory
    from .AggressiveStrategy import AggressiveStrategy

    print('\nConfiguring Fantasy Card Game...')
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    game = GameEngine()
    game.configure_engine(factory, strategy)

    print(f'Factory: {game.get_factory().__class__.__name__}')
    print(f'Strategy: {game.get_strategy().__class__.__name__}')
    print(f'Available types: {game.get_factory().get_supported_types()}')

    print('\nSimulating aggressive turn...')
    turn_details = game.simulate_turn()
    hand_list = [
        f"{name} ({cost})"
        for name, cost in turn_details["hand_details"].items()
    ]
    print(f'Hand: {hand_list}')

    print('\nTurn execution:')
    print(f'Strategy: {game.get_strategy().get_strategy_name()}')
    battlefield = game.get_factory().create_themed_deck(1)["cards"]
    strategy = game.get_strategy()
    actions = strategy.execute_turn(turn_details["hand"], battlefield)
    print(f'Actions: {actions}')

    print('\nGame Report:')
    print(game.get_engine_status())
    print('Abstract Factory + Strategy Pattern: Maximum flexibility achieved!')
except (ImportError, AttributeError):
    print(
        'All exercises must be executed from the repository root '
        'using: python3 -m exN.main (where N is the exercise number).\n'
        'Example: python3 -m ex0.main')
except Exception as e:
    print(e)

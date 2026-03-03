from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy

print('\n=== DataDeck Game Engine ===')

print('\nConfiguring Fantasy Card Game...')
try:
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    game = GameEngine()
    game.configure_engine(factory, strategy)

    print(f'Factory: {game.get_factory().__class__.__name__}')
    print(f'Strategy: {game.get_strategy().__class__.__name__}')
    print(f'Available types: {game.get_factory().get_supported_types()}')

    print('\nSimulating aggressive turn...')
    turn_details = game.simulate_turn()
    print(f'Hand: {[f"{name} ({cost})" for name, cost in turn_details["hand_details"].items()]}')

    print('\nTurn execution:')
    print(f'Strategy: {game.get_strategy().get_strategy_name()}')
    print(f'Actions: {game.get_strategy().execute_turn(turn_details["hand"], game.get_factory().create_themed_deck(1)["cards"])}')

    print('\nGame Report:')
    print(game.get_engine_status())
except Exception as e:
    print(e)

print('Abstract Factory + Strategy Pattern: Maximum flexibility achieved!')
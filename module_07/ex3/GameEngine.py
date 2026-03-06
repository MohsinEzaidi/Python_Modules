from ex0.Card import Card
from .CardFactory import CardFactory
from .GameStrategy import GameStrategy
from typing import List, Optional


class GameEngine:

    def __init__(self):
        self._factory: Optional[CardFactory] = None
        self._strategy: Optional[GameStrategy] = None
        self._turn: int = 0
        self._total_damage: int = 0
        self._cards_created: int = 0

    def get_factory(self) -> CardFactory:
        return self._factory

    def get_strategy(self) -> GameStrategy:
        return self._strategy

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        if not (factory or strategy):
            raise ValueError(
                'Couldn\'t configure engine, factory and strategy should'
                ' be of the corrected type as specific in the type hints')
        self._factory = factory
        self._strategy = strategy

    def simulate_turn(self) -> dict:
        hand: List[Card] = self._factory.create_themed_deck(3)
        self._cards_created = len(hand['cards'])
        self._turn += 1
        exce_res = self._strategy.execute_turn(hand['cards'], [])
        self._total_damage = exce_res['damage_dealt']
        return {
            'hand': hand['cards'],
            'hand_details': {c.get_name(): c.get_cost() for c in hand['cards']}
        }

    def get_engine_status(self) -> dict:
        strategy_name: str = self._strategy.get_strategy_name()
        return {
            'turns_simulated': self._turn,
            'strategy_used': strategy_name if self._strategy else 'None',
            'total_damage': self._total_damage,
            'cards_created': self._cards_created
        }

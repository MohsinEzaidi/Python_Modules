from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self._name = name
        self._cost = cost
        self._rarity = rarity

    def get_name(self) -> str:
        return self._name

    def get_cost(self) -> int:
        return self._cost

    def get_rarity(self) -> str:
        return self._rarity

    def set_name(self, name: str) -> None:
        self._name = name

    def set_cost(self, cost: int) -> None:
        self._cost = cost

    def set_rarity(self, rarity: str) -> None:
        self._rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            "name": self._name,
            "cost": self._cost,
            "rarity": self._rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        if available_mana >= self._cost:
            return True
        return False

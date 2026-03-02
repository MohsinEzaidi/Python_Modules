from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self._durability = durability
        self._effect = effect

    def get_durability(self) -> int:
        return self._durability

    def get_effect(self) -> str:
        return self._effect

    def set_durability(self, new_durability: int) -> None:
        self._durability = new_durability

    def set_effect(self, new_effect: str) -> None:
        self._effect = new_effect

    def play(self, game_state: dict) -> dict:
        if game_state['mana'] < self._cost:
            raise ValueError(f'You don\'t have enough mana to play "{self._name}"')

        game_state['mana'] -= self._cost
        return {
            'card_played': self.get_name(),
            'mana_used': self.get_cost(),
            'effect': self._effect
        }

def activate_ability(self) -> dict:
    if self._durability <= 0:
        return {"status": "destroyed", "message": "Artifact is broken!"}

    self._durability -= 1
    return {
        "status": "active",
        "effect": self._effect,
        "remaining_durability": self._durability
    }

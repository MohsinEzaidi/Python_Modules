from ex0 import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int) -> None:
        if attack < 0 or health < 0:
            raise ValueError("Attack and health must be non-negative integers.")
        super().__init__(name, cost, rarity)
        self._attack = attack
        self._health = health

    def get_attack(self) -> int:
        return self._attack

    def get_health(self) -> int:
        return self._health

    def set_attack(self, attack: int) -> None:
        if attack < 0:
            raise ValueError("Attack must be a non-negative integer.")
        self._attack = attack

    def set_health(self, health: int) -> None:
        if health < 0:
            raise ValueError("Health must be a non-negative integer.")
        self._health = health

    def play(self, game_state: dict) -> dict:
        
        return {
            'card_played': self.get_name(),
            'mana_used': self.get_cost(),
            'effect': 'Creature summoned to battlefield'
        }

    def attack_target(self, target) -> dict:
        pass

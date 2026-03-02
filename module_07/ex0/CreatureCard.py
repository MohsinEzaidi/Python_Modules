from ex0.Card import Card


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
            self._attack = 0
        self._attack = attack

    def set_health(self, health: int) -> None:
        if health < 0:
            self._health = 0
        self._health = health

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({'type': 'Creature', 'attack': self._attack, 'health': self._health})
        return info

    def play(self, game_state: dict) -> dict:
        if game_state['mana'] < self._cost:
            raise ValueError(f'You don\'t have enough mana to play "{self._name}"')
        game_state['mana'] -= self._cost
        return {
            'card_played': self.get_name(),
            'mana_used': self.get_cost(),
            'effect': 'Creature summoned to battlefield'
        }

    def attack_target(self, target) -> dict:
        if self._attack >= target._health:
            target._health = 0
        else:
            target._health -= self._attack
        return {'attacker': self._name, 'target': target._name, 'damage_dealt': self._attack, 'combat_resolved': target._health == 0}

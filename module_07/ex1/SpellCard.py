from ex0 import Card, CreatureCard


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self._effect_type = effect_type

    def get_effect_type(self) -> str:
        return self._effect_type

    def set_effect_type(self, new_effect_type: str) -> None:
        self._effect_type = new_effect_type

    def play(self, game_state: dict) -> dict:
        if game_state['mana'] < self._cost:
            raise Exception(f'You don\'t have enough mana to play "{self._name}"')
        game_state['mana'] -= self._cost
        game_state['cards_played'].append(self)
        game_state['mana_used'] += self._cost

        result = {'card_played': self.get_name(),'mana_used': self.get_cost()}
        if self._effect_type == 'heal':
            result['effect'] = 'Healing target by 3'
        if self._effect_type == 'buff':
            result['effect'] = 'Buffing target by 3 attacks'
        if self._effect_type == 'damage':
            result['effect'] = 'Deal 3 damage to target'
        if self._effect_type == 'debuff':
            result['effect'] = 'Debuffing target by 3 attacks'

        return result
    def resolve_effect(self, targets: list) -> dict:
        for target in targets:
            if not isinstance(target, CreatureCard):
                raise Exception('All targets should be creatures')
        for target in targets:
            if self._effect_type == 'heal':
                target.set_health(target.get_health() + 3)
            if self._effect_type == 'buff':
                target.set_attack(target.get_attack() + 3)
            if self._effect_type == 'damage':
                target.set_health(target.get_health() - 3)
            if self._effect_type == 'debuff':
                target.set_attack(target.get_attack() - 3)
        return {
            "effect_applied": self._effect_type,
            "target_count": len(targets),
            "details": f"Applied {self._effect_type} to {len(targets)} creatures"
        }

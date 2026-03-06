from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from enum import Enum
from typing import Dict, Union


class SpellEffects(Enum):
    HEAL = 'heal'
    BUFF = 'buff'
    DAMAGE = 'damage'
    DEBUFF = 'debuff'


class SpellCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        if effect_type not in [e.value for e in SpellEffects]:
            raise ValueError(
                f'The effect_type "{effect_type}" Not valid')
        self._effect_type = effect_type

    def get_effect_type(self) -> str:
        return self._effect_type

    def set_effect_type(self, new_effect_type: str) -> None:
        self._effect_type = new_effect_type

    def play(self, game_state: dict) -> dict:
        if game_state['mana'] < self._cost:
            raise Exception(
                f'You don\'t have enough mana to play "{self._name}"')
        game_state['mana'] -= self._cost
        game_state['cards_played'].append(self)
        game_state['mana_used'] += self._cost

        result: Dict[str, Union[str, int]] = {
            'card_played': self.get_name(),
            'mana_used': self.get_cost()}
        if self._effect_type == SpellEffects.HEAL.value:
            result['effect'] = 'Healing target by 3'
        elif self._effect_type == SpellEffects.BUFF.value:
            result['effect'] = 'Buffing target by 3 attacks'
        elif self._effect_type == SpellEffects.DAMAGE.value:
            result['effect'] = 'Deal 3 damage to target'
        elif self._effect_type == SpellEffects.DEBUFF.value:
            result['effect'] = 'Debuffing target by 3 attacks'
        else:
            result['effect'] = 'No effect'
        return result

    def resolve_effect(self, targets: list) -> dict:
        for target in targets:
            if not isinstance(target, CreatureCard):
                raise Exception('All targets should be creatures')
        for target in targets:
            if self._effect_type == SpellEffects.HEAL.value:
                target.set_health(target.get_health() + 3)
            if self._effect_type == SpellEffects.BUFF.value:
                target.set_attack(target.get_attack() + 3)
            if self._effect_type == SpellEffects.DAMAGE.value:
                target.set_health(target.get_health() - 3)
            if self._effect_type == SpellEffects.DEBUFF.value:
                target.set_attack(target.get_attack() - 3)
        result: Dict[str, Union[str, int]] = {
            "effect_applied": self._effect_type,
            "target_count": len(targets),
            "details": f"Applied {self._effect_type} "
                       f"to {len(targets)} creatures"
        }
        return result

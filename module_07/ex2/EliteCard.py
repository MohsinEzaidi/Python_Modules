from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int, armor: int, mana_power: int) -> None:
        if attack < 0 or health < 0:
            raise ValueError("Attack and health must be non-negative integers.")
        super().__init__(name, cost, rarity)
        self._attack = attack
        self._health = health
        self._armor = armor if armor > 0 else 0
        self._mana_power = mana_power if mana_power > 0 else 0

    def get_attack(self) -> int:
        return self._attack

    def get_health(self) -> int:
        return self._health

    def get_armor(self) -> int:
        return self._armor

    def get_mana_power(self) -> int:
        return self._mana_power

    def set_attack(self, attack: int) -> None:
        if attack < 0:
            self._attack = 0
        self._attack = attack

    def set_health(self, health: int) -> None:
        if health < 0:
            self._health = 0
        self._health = health

    def set_armor(self, new_armor: int) -> None:
        if new_armor < 0 :
            self._armor = 0
            return
        self._armor = new_armor

    def set_mana_power(self, new_mana_power: int) -> None:
        if new_mana_power < 0 :
            self._mana_power = 0
            return
        self._mana_power = new_mana_power

    def play(self, game_state: dict) -> dict:
        if game_state['mana'] < self._cost:
            raise ValueError(f'You don\'t have enough mana to play "{self._name}"')
        game_state['mana'] -= self._cost
        game_state['cards_played'].append(self)
        game_state['mana_used'] += self._cost
        return {
            'card_played': self.get_name(),
            'mana_used': self.get_cost(),
            'effect': 'Elite Card summoned to battlefield'
        }

    def attack(self, target) -> dict:
        if self._attack >= target._health:
            target._health = 0
        else:
            self.set_health(target._health - self._attack)
        return {
            'attacker': self._name,
            'target': target._name,
            'damage': self._attack,
            'combat_type': 'melee'}

    def defend(self, incoming_damage: int) -> dict:
        result = {
            'defender': self._name,
            'damage_taken': 0,
            'damage_blocked': 0,
            'still_alive': True
        }
        if incoming_damage > self._armor:
            result['damage_taken'] = incoming_damage - self._armor
            result['damage_blocked'] = self._armor
        else:
            result['damage_taken'] = 0
            result['damage_blocked'] = incoming_damage
        self.set_armor(self._armor - result['damage_blocked'])
        self.set_health(self._health - result['damage_taken'])
        result['still_alive'] = self._health > 0
        return result

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return{
            'caster': self._name,
            'spell': spell_name,
            'targets': [t.get_name() for t in targets],
            'mana_used': 2
        }

    def channel_mana(self, amount: int) -> dict:
        if amount < 0:
            amount = 0
        return {
            'channeled': amount,
            'total_mana': self._mana_power + amount
        }

    def get_magic_stats(self) -> dict:
        return{
            'magical power': 'mana_power',
            'amount': self._mana_power
        }

    def get_combat_stats(self) -> dict:
        return{
            'health': self._health,
            'attack': self._attack,
            'armor': self._armor
        }
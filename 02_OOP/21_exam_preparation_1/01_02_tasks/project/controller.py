from typing import List

from project.supply.supply import Supply
from project.supply.food import Food
from project.supply.drink import Drink
from project.player import Player


class Controller:
    VALID_TYPES = [
        "Food",
        "Drink"
    ]

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *args) -> str:
        result = []
        for player in args:
            if player not in self.players:
                result.append(player.name)
                self.players.append(player)

        return f"Successfully added: {', '.join(result)}"

    def add_supply(self, *args):
        [self.supplies.append(s) for s in args]

    def sustain(self, player_name: str, sustenance_type: str):
        try:
            player = next(filter(lambda p: p.name == player_name, self.players))
        except StopIteration:
            return

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        if sustenance_type not in Controller.VALID_TYPES:
            return

        supplies_of_type = None

        for i in range(len(self.supplies) - 1, -1, -1):
            supply = self.supplies[i]

            if supply.__class__.__name__ == sustenance_type:
                supplies_of_type = self.supplies.pop(i)
                break

        if not supplies_of_type:
            if sustenance_type == "Food":
                raise Exception("There are no food supplies left!")
            else:
                raise Exception("There are no drink supplies left!")

        # Sustain the player and remove the supply
        # Ensure the player's stamina does not exceed 100
        player.stamina = min(player.stamina + supplies_of_type.energy, 100)

        return f"{player_name} sustained successfully with {supplies_of_type.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = next(filter(lambda p: p.name == first_player_name, self.players))
        second_player = next(filter(lambda p: p.name == second_player_name, self.players))

        if [first_player.stamina, second_player.stamina] == [0, 0]:
            return f"Player {first_player.name} does not have enough stamina.\n" \
                   f"Player {second_player.name} does not have enough stamina."

        elif first_player.stamina == 0:
            return f"Player {first_player.name} does not have enough stamina."

        elif second_player.stamina == 0:
            return f"Player {second_player.name} does not have enough stamina."

        if first_player.stamina < second_player.stamina:
            attacker, defender = first_player, second_player
        else:
            attacker, defender = second_player, first_player

        attack_value_att = attacker.stamina / 2

        # Reduce the defender's stamina
        defender.stamina = max(defender.stamina - attack_value_att, 0)

        if defender.stamina == 0:
            return f"Winner: {attacker.name}"

        attack_value_def = defender.stamina / 2

        # Reduce the attacker's stamina
        attacker.stamina = max(attacker.stamina - attack_value_def, 0)

        if attacker.stamina == 0:
            return f"Winner: {defender.name}"

        # Determine the winner based on remaining stamina
        winner = attacker if attacker.stamina > defender.stamina else defender

        return f"Winner: {winner.name}"

    def next_day(self) -> None:
        for player in self.players:
            reduce_stamina_with = player.age * 2
            player.stamina = max(player.stamina - reduce_stamina_with, 0)

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        return "\n".join(
            [str(p) for p in self.players]
            +
            [s.details() for s in self.supplies]
        )

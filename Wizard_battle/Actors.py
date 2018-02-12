import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level

    def attack(self, creature):
        print(creature.name)
        creature_roll = creature.get_defensive_roll()  # Call method on
        # instance(creature)
        player_roll = self.get_defensive_roll()  # call method on player
        # instance

        print('wizard rolls {}'.format(player_roll))
        print('{} rolls {}'.format(creature.name, creature_roll))

        if player_roll > creature_roll:
            print('Wizard won')
            return creature
        else:
            print('{} won'.format(creature.name))


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breath_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breath_fire = breath_fire

# Override method for dragon
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breath_fire else 1  # If else cond in one line
        return base_roll * fire_modifier * 1 / self.scaliness

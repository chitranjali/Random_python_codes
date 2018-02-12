from Actors import Creature, Dragon
import random


def main():
    play_game()


def play_game():
    creatures = [Creature('Toad', 3),
                 Creature('Bat', 10),
                 Creature('Tiger', 25),
                 Dragon('dragon', 50, 20, True),
                 Creature('Evil wizard', 75)]

    player = Creature('wizard', 60)

    while True:
        user_choice = input('Do you wanna [a]ttack or [r]un away, [l]ook around?')
        if user_choice == 'a':
            print('ok')
            opponent = random.choice(creatures)
            lost = player.attack(opponent)
            if lost:
                creatures.remove(lost)
        elif user_choice == 'r':
            continue
        elif user_choice == 'l':
            for c in creatures:
                print('* A level {} {}'.format(c.level, c.name))
        else:
            print('OK, exiting game... bye!')
            break

        if not creatures:
            print('No more creatures left! You Won!!')
            break


if __name__ == '__main__':
    main()

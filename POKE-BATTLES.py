"""                     Welcome to the turn-based terminal game,
                        ------------- POKE-BATTLES -------------

You will be able to select a pokemon, each with a variety of moves and stats,
and take them into battle!
But BEWARE! A ghostly prescence haunts this game..."""

import random

# list of pokemon with their respective stats and moves
pokemon_list = [{'Name': 'Pikachu', 'HP': 70, 'Type': 'Electric', 'Speed': 90,
                 'Moves': {'Thunder Shock': {'Type': 'Electric', 'Power': 40},
                           'Quick Attack': {'Type': 'Normal', 'Power': 40}}},

                {'Name': 'Charmander', 'HP': 70, 'Type': 'Fire', 'Speed': 65,
                 'Moves': {'Ember': {'Type': 'Fire', 'Power': 40},
                           'Slash': {'Type': 'Normal', 'Power': 70}}},

                {'Name': 'Bulbasaur', 'HP': 80, 'Type': 'Grass', 'Speed': 45,
                 'Moves': {'Vine Whip': {'Type': 'Grass', 'Power': 35},
                           'Tackle': {'Type': 'Normal', 'Power': 35},
                           'Razor Leaf': {'Type': 'Grass', 'Power': 55}}},


                {'Name': 'Squirtle', 'HP': 70, 'Type': 'Water', 'Speed': 43,
                 'Moves': {'Water Gun': {'Type': 'Water', 'Power': 40},
                           'Tackle': {'Type': 'Normal', 'Power': 35}}},

                {'Name': 'Gengar', 'HP': 130, 'Type': 'Ghost', 'Speed': 110,
                 'Moves': {'Lick': {'Type': 'Ghost', 'Power': 20},
                           'Dream Eater': {'Type': 'Psychic', 'Power': 100}}}]

trained_pokemon = pokemon_list.copy()

# variable tracks whether user has beaten Gengar
beat_gengar = False

# function for which prompts user to select a character


def pokemon_selection(pokemon_list):
    print(">>> Choose one of the following pokemon to battle with: \n")
    for pokemon in pokemon_list:
        if pokemon.get('Name') == 'Gengar' and beat_gengar == False:
            break
        else:
            print(f"    >{pokemon.get('Name')}\n")

    selection = input(">>>Who do you choose?\n  >")
    selection = selection.title()

    for pokemon in pokemon_list:
        if selection in pokemon.values():
            return pokemon

# random opponent selection


def opponent_selection(pokemon_list):
    return random.choice(pokemon_list)

# displays a pokemon's stats without showing their moveset


def pokemon_stats(pokemon):
    for key in pokemon:
        print(f"    >{key}: {pokemon.get(key)}")
        if key == 'Speed':
            print("\n")
            break

# prompts user to select a move


def move_selection(moves):
    print(">>> Make your move!")
    for move in moves:
        print(f"    >{move}: {moves.get(move)}")

    selection = input("Pick a move to attack with: ")
    selection = selection.title()

    for move in moves:
        if selection in moves:

            return move, (moves.get(move)).get('Power')

# random opponent move selection


def opponent_move(moves):
    move = random.choice(list(moves.keys()))
    return move, (moves.get(move)).get('Power')

# decide which player goes first, the quicker of the two will start
# if speeds are equal, the user will always start


def who_goes_first(your_speed, opponent_speed):
    if your_speed > opponent_speed:
        first_mover = True
    elif your_speed == opponent_speed:
        first_mover == True
    else:
        first_mover = False
    return first_mover

# calculates updated HP based on the attack


def attack(pokemon, opponent, move, damage):
    attacker = pokemon.get('Name')
    defender = opponent.get('Name')
    health = opponent.get('HP')
    adjusted_damage = damage
    super_effective = False
    if opponent['Type'] == 'Fire':
        if pokemon['Moves'][move]['Type'] == 'Water':
            adjusted_damage = damage * 1.4
            super_effective = True
    if opponent['Type'] == 'Grass':
        if pokemon['Moves'][move]['Type'] == 'Fire':
            adjusted_damage = damage * 1.4
            super_effective = True
    if opponent['Type'] == 'Water':
        if pokemon['Moves'][move]['Type'] == 'Grass':
            adjusted_damage = damage * 1.4
            super_effective = True
    adjusted_damage = round(adjusted_damage)
    new_health = health - adjusted_damage
    print(f">>> {attacker} used {move}!")
    if super_effective == True:
        print(f"{move} was super effective!")
    print(f">>> {move} dealt {adjusted_damage} damage.")
    print(f">>> {defender} has {new_health}HP remaining...")
    opponent['HP'] = new_health

# increases pokemon's health after each battle


def pokemon_training(user_pokemon, trained_pokemon):
    for pokemon in trained_pokemon:
        if user_pokemon.get('Name') == pokemon.get('Name'):
            pokemon['HP'] = pokemon['HP'] + 5
            print(
                f"{user_pokemon.get('Name')} has become stronger! It now has {pokemon['HP']}HP.")

# battle function where players take turns attacking until one player loses all their


def battle():
    if who_goes_first(user_pokemon.get('Speed'), opponent_pokemon.get('Speed')) == True:
        your_move, damage_dealt = move_selection(user_pokemon.get('Moves'))
        print("\n")
        attack(user_pokemon, opponent_pokemon, your_move, damage_dealt)
        print("\n")

        while user_pokemon['HP'] > 0 or opponent_pokemon['HP'] > 0:
            if user_pokemon['HP'] <= 0 or opponent_pokemon['HP'] <= 0:
                break

            their_move, damage_taken = opponent_move(
                opponent_pokemon.get('Moves'))
            print("\n")
            attack(opponent_pokemon, user_pokemon, their_move, damage_taken)
            print("\n")

            your_move, damage_dealt = move_selection(user_pokemon.get('Moves'))
            print("\n")
            attack(user_pokemon, opponent_pokemon, your_move, damage_dealt)
            print("\n")

    else:
        their_move, damage_taken = opponent_move(opponent_pokemon.get('Moves'))
        print("\n")
        attack(opponent_pokemon, user_pokemon, their_move, damage_taken)
        print("\n")

        while user_pokemon['HP'] > 0 or opponent_pokemon['HP'] > 0:
            if user_pokemon['HP'] <= 0 or opponent_pokemon['HP'] <= 0:
                break

            your_move, damage_dealt = move_selection(user_pokemon.get('Moves'))
            print("\n")
            attack(user_pokemon, opponent_pokemon, your_move, damage_dealt)
            print("\n")

            their_move, damage_taken = opponent_move(
                opponent_pokemon.get('Moves'))
            print("\n")
            attack(opponent_pokemon, user_pokemon, their_move, damage_taken)
            print("\n")

    if user_pokemon['HP'] <= 0:
        print("You LOST :( Better luck next time...")

    elif opponent_pokemon['HP'] <= 0:
        print("Congratulations! You are the WINNER :)")
        if opponent_pokemon['Name'] == 'Gengar':
            beat_gengar == True

    pokemon_training(user_pokemon, trained_pokemon)


user_pokemon = dict(pokemon_selection(pokemon_list))

# user prompted until a pokemon from the list is chosen
while user_pokemon == None:
    user_pokemon = dict(pokemon_selection(pokemon_list))

opponent_pokemon = dict(opponent_selection(pokemon_list))
print("\n>>> Your pokemon:")
pokemon_stats(user_pokemon)
print("\n>>> Your opponent:")
pokemon_stats(opponent_pokemon)

battle()

# ask for a rematch
rematch = input(">>> Would you like to play again?\n    >Y\n    >N\n    >")
# let user play as many games as they like until they decide otherwise
while rematch.upper() == 'Y':
    user_pokemon = dict(pokemon_selection(trained_pokemon))

    while user_pokemon == None:
        user_pokemon = dict(pokemon_selection(trained_pokemon))

    opponent_pokemon = dict(opponent_selection(pokemon_list))
    print("\n>>> Your pokemon:")
    pokemon_stats(user_pokemon)
    print("\n>>> Your opponent:")
    pokemon_stats(opponent_pokemon)

    battle()
    rematch = input(">>> Would you like to play again?\n    >Y\n    >N\n    >")

    if rematch.upper() == 'N':
        print("Thanks for playing- see you again soon!")
        break

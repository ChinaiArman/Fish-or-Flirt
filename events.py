"""
Arman Chinai | A01317650
Lex Wong | A01322278

A python module containing the event functions for Fish or Flirt.
"""


from random import randint
from time import sleep
import dialogue
import ascii_art as asc


WATER_TILE = "\U0001F30A"
LAND_TILE = "\U0001F3D6"
BOAT_TILE = "\U000026F5"
ISLAND_TILE = "\U0001F334"
PLAYER_TILE = "\U0001F3A3"
SKULL_TILE = "\U0001F480"
LEVIATHAN_TILE = "\U00002757"
FISHABLE_ITEMS = {0: "Stick", 1: "Stick", 2: "Stick", 3: "Stick", 4: "Stick", 5: "Boot", 6: "Boot",
                  7: "Boot", 8: "Boot", 9: "Fishie", 10: "Fishie", 11: "Fishie", 12: "Pufferfishie", 13: "Penguin",
                  14: "Shark", 15: "none", 16: "none", 17: "none", 18: "none", 19: "none", 20: "POSEIDON'S TRIDENT"}


def fishing_game(character: dict) -> None:
    """
    Play the Fishing Game and have a random chance to catch an item. Caught items are added to players inventory.

    :param character: A dictionary with key-value pairs representing the player and their basic information.
    :precondition: character exists and has the key-value pairs 'luck' and 'charisma' containing integers and
    'inventory' containing a list of game items the player has acquired.
    :postcondition: Will run the fishing game, giving players a random chance to catch an item from FISHABLE_ITEMS.
    :postcondition: If the objected returned from FISHABLE_ITEMS is not 'none' the item will be added to their
    inventory and success dialogue will be displayed in the console.
    :postcondition: If the item caught is 'POSEIDON'S TRIDENT', the item will be added to the inventory, special
    dialogue will display in the console, and the character's 'luck' and 'charisma' will be increased by a multiple of
    1.2.
    :postcondition: If the item caught is 'none', no item will be added and fail dialogue will be displayed in the
    console.
    :return: None
    """
    print(asc.fishing_rod)
    print(dialogue.start_fish[randint(0, len(dialogue.start_fish) - 1)])
    dialogue.loading(randint(2, 7))
    fished_item = FISHABLE_ITEMS[randint(0, len(FISHABLE_ITEMS) - 1)]
    if fished_item != "none":
        print(asc.bucket)
        if fished_item == "POSEIDON'S TRIDENT":
            for i in range(3):
                print("...\n\n")
                sleep(1)
            print(asc.fishing_ascii[fished_item])
            dialogue.slow_print(dialogue.acquired_trident)
            del FISHABLE_ITEMS[20]
            character["luck"] *= 1.2
            character["charisma"] *= 1.2
        else:
            sleep(1)
            print(asc.fishing_ascii[fished_item])
            print(f"You fished a {fished_item}! It has been added to your inventory.")
            print("Your luck and charisma have been greatly increased")
        character["inventory"] += [fished_item]
        character["luck"] += 1
    else:
        print(asc.sadness)
        dialogue.slow_print(dialogue.fishing_game_fail[randint(0, len(dialogue.fishing_game_fail) - 1)])
    sleep(2)
    return


def leviathan_event(board: dict, character: dict, event_dialogue: dict) -> None:
    """
    Play the Leviathan Event Challenge; the final boss for Fish or Flirt.

    :param board: A dictionary with key-value pairs representing tiles on the game board.
    :param character: A dictionary with key-value pairs representing the player and their basic information.
    :param event_dialogue: A dictionary containing the dialogue for the challenge.
    :precondition: board has keys of tuples, representing x and y coordinates, and values representing the location
    stored at that position.
    :precondition: character exists and has the key-value pairs 'x-coordinate', 'y-coordinate', 'charisma', 'luck', and
    'xp' containing integers, and 'inventory' containing a list of game items.
    :precondition: event_dialogue is the Leviathan dictionary constant from the dialogue module containing strings with
    storylines for the event.
    :return: None
    """
    leviathan_charisma = 100
    leviathan_difficulty = 100
    position = (character['x-coordinate'], character['y-coordinate'])
    print(event_dialogue["ascii_encounter"])
    dialogue.slow_print(event_dialogue["encounter"])
    flirting = True
    while flirting:
        player_options = ["Fish and Flirt"]
        for key, player_options in enumerate(player_options, 1):
            print(f"{key}.\t{player_options}")
        selection = input("\nAnswer Here:\t")

        if selection == "1":
            dialogue.slow_print(event_dialogue["fish_and_flirt"])
            if character["charisma"] > randint(0, leviathan_charisma) and character["luck"] > \
                    randint(0, leviathan_difficulty):
                print(event_dialogue["success"])
                dialogue.slow_print(event_dialogue["defeated"])
                character["inventory"] += [event_dialogue["entity"], event_dialogue["reward"]]
                flirting = False
            else:
                print(event_dialogue["fail"])
                print(event_dialogue["action_failed"])
        else:
            print(event_dialogue["invalid_flirt"])
    board[position] = WATER_TILE
    board[(1, 8)] = LEVIATHAN_TILE
    character["xp"] += 1
    return


def pirate_event(board: dict, character: dict, event_dialogue: dict) -> None:
    """
    Play the Pirate Event Challenge; the first boss in Fish or Flirt.

    :param board: A dictionary with key-value pairs representing tiles on the game board.
    :param character: A dictionary with key-value pairs representing the player and their basic information.
    :param event_dialogue: A dictionary containing the dialogue for the challenge.
    :precondition: board has keys of tuples, representing x and y coordinates, and values representing the location
    stored at that position.
    :precondition: character exists and has the key-value pairs 'x-coordinate', 'y-coordinate', 'charisma', and 'xp'
    containing integers, and 'inventory' containing a list of game items.
    :precondition: event_dialogue is the Pirate dictionary constant from the dialogue module containing strings with
    storylines for the event.
    :return: None
    """
    pirate_charisma = 100
    position = (character['x-coordinate'], character['y-coordinate'])
    dialogue.slow_print(event_dialogue["encounter"])
    print(event_dialogue["start_flirt"])

    flirting = True
    while flirting:
        player_options = ["Seduce"]
        for key, player_options in enumerate(player_options, 1):
            print(f"{key}.\t{player_options}")
        selection = input("\nAnswer Here:\t")

        if selection == "1":
            dialogue.slow_print(event_dialogue["seduction"][randint(0, len(event_dialogue["seduction"]) - 1)])
            if character["charisma"] > randint(0, pirate_charisma):
                print(event_dialogue["blush"])
                print(event_dialogue["success"])
                character["charisma"] += 5
                character["luck"] += 5
                character["inventory"] += [event_dialogue["entity"]]
                flirting = False
            else:
                print(event_dialogue["skulls"])
                print(event_dialogue["fail"])
        else:
            print(event_dialogue["run_away"])
            print(event_dialogue["flee"][randint(0, len(event_dialogue["flee"]) - 1)])

    board[position] = ISLAND_TILE
    board[(1, 8)] = LEVIATHAN_TILE
    character["xp"] += 1
    return


def boat_event(board: dict, character: dict, event_dialogue: dict) -> None:
    """
    Play the Boat Event Challenge.

    :param board: A dictionary with key-value pairs representing tiles on the game board.
    :param character: A dictionary with key-value pairs representing the player and their basic information.
    :param event_dialogue: A dictionary containing the dialogue for the challenge.
    :precondition: board has keys of tuples, representing x and y coordinates, and values representing the location
    stored at that position.
    :precondition: character exists and has the key-value pairs 'x-coordinate', 'y-coordinate', and 'xp'
    containing integers, and 'inventory' containing a list of game items.
    :precondition: event_dialogue is the Boat dictionary constant from the dialogue module containing strings with
    storylines for the event.
    :return: None
    """
    position = (character['x-coordinate'], character['y-coordinate'])
    print(event_dialogue["ascii_encounter"])
    dialogue.slow_print(event_dialogue["encounter"])
    dialogue.slow_print(event_dialogue["acquisition"])
    board[position] = WATER_TILE
    character["xp"] += 1
    character["inventory"] += [event_dialogue["entity"]]
    return


def land_event(_, character: dict, event_dialogue: dict) -> None:
    """
    Play the Land Event Challenge. Fight against a Crab or a Fisherman, depending on the entity in event_dialogue.

    :param _: Not important to the function
    :param character: A dictionary with key-value pairs representing the player and their basic information.
    :param event_dialogue: A dictionary containing the dialogue for the challenge. Determines which enemy the player is
    fighting against.
    :precondition: character exists and has the key-value pairs 'x-coordinate', 'y-coordinate', and 'charisma'
    containing integers, and 'inventory' containing a list of game items.
    :precondition: event_dialogue is either then Crab or Fisherman dictionary constant from the dialogue module
    containing strings with storylines for the event.
    :return: None
    """
    entity_charisma = randint(80, 100)
    print(event_dialogue["ascii_encounter"])
    print(event_dialogue["encounter"][(randint(0, len(event_dialogue["encounter"]) - 1))])
    print(event_dialogue["start_flirt"])

    flirting = True
    while flirting:
        player_options = ("Flirt", "Flirt Harder")
        for key, player_options in enumerate(player_options, 1):
            print(f"{key}.\t{player_options}")
        selection = input("\nAnswer Here:\t")

        if selection == "1":
            dialogue.slow_print(event_dialogue["flirt_dialogue"][randint(0, len(event_dialogue["flirt_dialogue"]) - 1)])
            valid_selection = True
        elif selection == "2":
            dialogue.slow_print(event_dialogue["flirt_harder_dialogue"][randint(
                0, len(event_dialogue["flirt_harder_dialogue"]) - 1)])
            valid_selection = True
        else:
            print(event_dialogue["invalid_flirt"])
            valid_selection = False

        if valid_selection:
            if character["charisma"] > randint(0, entity_charisma):
                print(event_dialogue["ascii_blushing"])
                print(event_dialogue["success_dialogue"])
                character["charisma"] += character["charisma"] < 80
                character["inventory"] += [event_dialogue["entity"]]
                flirting = False
            else:
                print(event_dialogue["ascii_fail"])
                print(event_dialogue["fail_dialogue"])
    return


def water_event(_, character: dict, event_dialogue: dict) -> None:
    """
    Play the Land Event Challenge. Fight against a Mermaid or a Whale, depending on the entity in event_dialogue.

    :param _: Not important to the function
    :param character: A dictionary with key-value pairs representing the player and their basic information.
    :param event_dialogue: A dictionary containing the dialogue for the challenge. Determines which enemy the player is
    fighting against.
    :precondition: character exists and has the key-value pairs 'x-coordinate', 'y-coordinate', 'charisma', and 'luck'
    containing integers, and 'inventory' containing a list of game items.
    :precondition: event_dialogue is either then Mermaid or Whale dictionary constant from the dialogue module
    containing strings with storylines for the event.
    :return: None
    """
    entity_charisma = randint(80, 100)
    entity_difficulty = randint(80, 100)
    print(event_dialogue["ascii_encounter"])
    print(event_dialogue["encounter"][(randint(0, len(event_dialogue["encounter"]) - 1))])

    attempting = True
    while attempting:
        player_options = ("Fish", "Flirt")
        for key, player_options in enumerate(player_options, 1):
            print(f"{key}.\t{player_options}")
        selection = input("\nAnswer Here:\t")

        if selection == "1":
            print(event_dialogue["fishing_rod"])
            dialogue.slow_print(event_dialogue["start_fish"][randint(0, len(event_dialogue["start_fish"]) - 1)])
            if character["luck"] > randint(0, entity_difficulty):
                print(event_dialogue["ascii_bucket"])
                print(event_dialogue["fishing_success_dialogue"])
                character["luck"] += character["luck"] < 80
                character["inventory"] += [event_dialogue["entity"]]
                attempting = False
            else:
                print(event_dialogue["ascii_fishing_fail"])
                print(event_dialogue["fishing_fail_dialogue"])
        elif selection == "2":
            print(event_dialogue["start_flirt"])
            dialogue.slow_print(event_dialogue["flirt_dialogue"][randint(0, len(event_dialogue["flirt_dialogue"]) - 1)])
            if character["charisma"] > randint(0, entity_charisma):
                print(event_dialogue["ascii_blushing"])
                print(event_dialogue["flirt_success"])
                character["charisma"] += character["charisma"] < 80
                character["inventory"] += [event_dialogue["entity"]]
                attempting = False
            else:
                print(event_dialogue["ascii_fail"])
                print(event_dialogue["flirt_fail"])
        else:
            print(event_dialogue["invalid_flirt"])
    return


def main():
    """
    Drive the program.
    """
    pass


if __name__ == "__main__":
    main()

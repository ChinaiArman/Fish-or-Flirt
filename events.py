from random import randint
# from time import sleep
import dialogue
import ascii_art as asc
# import sys


def leviathan_event(board, character, event_dialogue):
    water_tile = "\U0001F30A"
    leviathan_tile = "\U00002757"
    position = (character['x-coordinate'], character['y-coordinate'])
    print(asc.leviathan)
    dialogue.slow_print(dialogue.encounter_leviathan)
    # Mechanics here

    # story here

    board[position] = water_tile
    board[(1, 8)] = leviathan_tile
    character["xp"] += 1
    return


def pirate_event(board, character, event_dialogue):
    island_tile = "\U0001F334"
    leviathan_tile = "\U00002757"
    pirate_charisma = 100
    position = (character['x-coordinate'], character['y-coordinate'])
    dialogue.slow_print(event_dialogue["encounter"])
    print(event_dialogue["start_flirt"])

    flirting = True
    while flirting:
        player_options = ("Seduce", "Flee")
        for key, player_options in enumerate(player_options, 1):
            print(f"{key}.\t{player_options}")
        selection = input("\nAnswer Here:\t")

        if selection == "1":
            dialogue.slow_print(event_dialogue["seduction"][randint(0, len(event_dialogue["seduction"]) - 1)])
            if character["charisma"] > randint(0, pirate_charisma):
                # Pirate Blush
                # Success Art
                print(event_dialogue["success"])
                character["charisma"] += 5
                character["luck"] += 5
                character["inventory"] += [event_dialogue["entity"]]
                flirting = False
            else:
                # Fail Art
                print(event_dialogue["fail"])
        elif selection == "2":
            print("No fleeing, only flirting")
        else:
            # Confused Art
            print(event_dialogue["flee"][randint(0, len(event_dialogue["flee"]) - 1)])

    board[position] = island_tile
    board[(1, 8)] = leviathan_tile
    character["xp"] += 1
    return


def boat_event(board, character, event_dialogue):
    water_tile = "\U0001F30A"
    position = (character['x-coordinate'], character['y-coordinate'])
    print(event_dialogue["ascii_encounter"])
    dialogue.slow_print(event_dialogue["encounter"])
    dialogue.slow_print(event_dialogue["acquisition"])
    board[position] = water_tile
    character["xp"] += 1
    character["inventory"] += [event_dialogue["entity"]]
    return


def land_event(_, character, event_dialogue):
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


# MERMAID_DIALOGUE = {
#     "entity": "Mermaid",
#     "ascii_encounter": asc.mermaid,
#     "encounter": dialogue.random_encounter_mermaid,
#     "fishing_rod": asc.fishing_rod,
#     "start_fish": dialogue.start_fish,
#     "ascii_bucket": asc.bucket,
#     "fishing_success_dialogue": dialogue.fish_mermaid_success,
#     "ascii_fishing_fail": asc.fishing_fail,
#     "fishing_fail_dialogue": dialogue.fish_mermaid_fail,
#     "start_flirt": dialogue.start_flirt,
#     "flirt_dialogue": dialogue.flirt_dialogue,
#     "ascii_blushing": asc.blushing,
#     "flirt_success": dialogue.flirt_success_mermaid,
#     "ascii_fail": asc.flirt_fail,
#     "flirt_fail": dialogue.flirt_fail_mermaid,
#     "invalid_flirt": dialogue.invalid_flirt
# }
def water_event(_, character, event_dialogue):
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

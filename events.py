from random import randint
# from time import sleep
import dialogue
import ascii_art as asc
# import sys


def leviathan_event(board, character):
    water_tile = "\U0001F30A"
    leviathan_tile = "\U00002757"
    position = (character['x-coordinate'], character['y-coordinate'])
    print(asc.leviathan)
    dialogue.slow_print(dialogue.encounter_leviathan)
    # story here

    # Mechanics here

    # story here

    board[position] = water_tile
    board[(1, 8)] = leviathan_tile
    character["xp"] += 1
    return


def pirate_event(board, character):
    island_tile = "\U0001F334"
    leviathan_tile = "\U00002757"
    position = (character['x-coordinate'], character['y-coordinate'])
    dialogue.slow_print(dialogue.encounter_pirate)
    print(dialogue.start_flirt)

    # Mechanics here

    board[position] = island_tile
    board[(1, 8)] = leviathan_tile
    character["xp"] += 1
    return


def boat_event(board, character):
    water_tile = "\U0001F30A"
    position = (character['x-coordinate'], character['y-coordinate'])
    print(asc.boat)
    dialogue.slow_print(dialogue.encounter_boat)
    dialogue.slow_print(dialogue.acquired_boat)
    board[position] = water_tile
    character["xp"] += 1
    return


def fisherman_event(_, character):
    fisherman_charisma = randint(80, 100)
    print(asc.fisherman)
    print(dialogue.random_encounter_fisherman[(randint(0, len(dialogue.random_encounter_fisherman) - 1))])
    print(dialogue.start_flirt)

    flirting = True
    while flirting:
        player_options = ("Flirt", "Flirt Harder")
        for key, player_options in enumerate(player_options, 1):
            print(f"{key}.\t{player_options}")
        selection = input("\nAnswer Here:\t")

        if selection == "1":
            dialogue.slow_print(dialogue.flirt_dialogue[randint(0, len(dialogue.flirt_dialogue) - 1)])
            valid_selection = True
        elif selection == "2":
            dialogue.slow_print(dialogue.flirt_harder_dialogue[randint(0, len(dialogue.flirt_harder_dialogue) - 1)])
            valid_selection = True
        else:
            print(dialogue.invalid_flirt)
            valid_selection = False

        if valid_selection:
            if character["charisma"] > randint(0, fisherman_charisma):
                print(asc.blushing)
                print(dialogue.flirt_success_fisherman)
                character += character["charisma"] < 80
                character["inventory"] += ["Fisherman"]
                flirting = False
            else:
                print(asc.flirt_fail)
                print(dialogue.flirt_fail_fisherman)
    return


def crab_event(_, character):
    crab_charisma = randint(80, 100)
    print(asc.crab)
    print(dialogue.random_encounter_crab[(randint(0, len(dialogue.random_encounter_crab) - 1))])
    print(dialogue.start_flirt)

    flirting = True
    while flirting:
        player_options = ("Flirt", "Flirt Harder")
        for key, player_options in enumerate(player_options, 1):
            print(f"{key}.\t{player_options}")
        selection = input("\nAnswer Here:\t")

        if selection == "1":
            dialogue.slow_print(dialogue.flirt_dialogue[randint(0, len(dialogue.flirt_dialogue) - 1)])
            valid_selection = True
        elif selection == "2":
            dialogue.slow_print(dialogue.flirt_harder_dialogue[randint(0, len(dialogue.flirt_harder_dialogue) - 1)])
            valid_selection = True
        else:
            print(dialogue.invalid_flirt)
            valid_selection = False

        if valid_selection:
            if character["charisma"] > randint(0, crab_charisma):
                print(asc.blushing)
                print(dialogue.flirt_success_crab)
                character += character["charisma"] < 80
                character["inventory"] += ["Crab"]
                flirting = False
            else:
                print(asc.flirt_fail)
                print(dialogue.flirt_fail_crab)
    return


def whale_event(_, character):
    whale_charisma = randint(80, 100)
    whale_difficulty = randint(80, 100)
    print(asc.whale)
    print(dialogue.random_encounter_whale[(randint(0, len(dialogue.random_encounter_whale) - 1))])

    attempting = True
    while attempting:
        player_options = ("Fish", "Flirt")
        for key, player_options in enumerate(player_options, 1):
            print(f"{key}.\t{player_options}")
        selection = input("\nAnswer Here:\t")

        if selection == "1":
            print(asc.fishing_rod)
            dialogue.slow_print(dialogue.start_fish[randint(0, len(dialogue.start_fish) - 1)])
            if character["luck"] > randint(0, whale_difficulty):
                print(asc.bucket)
                print(dialogue.fish_whale_success)
                character += character["luck"] < 80
                character["inventory"] += ["Whale"]
                attempting = False
            else:
                print(asc.fishing_fail)
                print(dialogue.fish_whale_fail)
        elif selection == "2":
            print(dialogue.start_flirt)
            dialogue.slow_print(dialogue.flirt_dialogue[randint(0, len(dialogue.flirt_dialogue) - 1)])
            if character["charisma"] > randint(0, whale_charisma):
                print(asc.blushing)
                print(dialogue.flirt_success_whale)
                character += character["charisma"] < 80
                character["inventory"] += ["Whale"]
                attempting = False
            else:
                print(asc.flirt_fail)
                print(dialogue.flirt_fail_whale)
        else:
            print(dialogue.invalid_flirt)
    return


def mermaid_event(_, character):
    mermaid_charisma = randint(80, 100)
    mermaid_difficulty = randint(80, 100)
    print(asc.mermaid)
    print(dialogue.random_encounter_mermaid[(randint(0, len(dialogue.random_encounter_mermaid) - 1))])

    attempting = True
    while attempting:
        player_options = ("Fish", "Flirt")
        for key, player_options in enumerate(player_options, 1):
            print(f"{key}.\t{player_options}")
        selection = input("\nAnswer Here:\t")

        if selection == "1":
            print(asc.fishing_rod)
            dialogue.slow_print(dialogue.start_fish[randint(0, len(dialogue.start_fish) - 1)])
            if character["luck"] > randint(0, mermaid_difficulty):
                print(asc.bucket)
                print(dialogue.fish_mermaid_success)
                character += character["luck"] < 80
                character["inventory"] += ["Mermaid"]
                attempting = False
            else:
                print(asc.fishing_fail)
                print(dialogue.fish_mermaid_fail)
        elif selection == "2":
            print(dialogue.start_flirt)
            dialogue.slow_print(dialogue.flirt_harder_dialogue[randint(0, len(dialogue.flirt_harder_dialogue) - 1)])
            if character["charisma"] > randint(0, mermaid_charisma):
                print(asc.blushing)
                print(dialogue.flirt_success_mermaid)
                character += character["charisma"] < 80
                character["inventory"] += ["Mermaid"]
                attempting = False
            else:
                print(asc.flirt_fail)
                print(dialogue.flirt_fail_mermaid)
        else:
            print(dialogue.invalid_flirt)
    return

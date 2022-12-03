"""
Arman Chinai | A01317650
Lex Wong | A01322278

A python module containing the engine for Fish or Flirt
"""


from random import randint
from time import sleep
from itertools import starmap
import dialogue
import events
import ascii_art as asc
from pandas import DataFrame


WATER_TILE = "\U0001F30A"
LAND_TILE = "\U0001F3D6"
BOAT_TILE = "\U000026F5"
ISLAND_TILE = "\U0001F334"
PLAYER_TILE = "\U0001F3A3"
SKULL_TILE = "\U0001F480"
LEVIATHAN_TILE = "\U00002757"
SCORING_SHEET = {"Mama's Fishing Rod": 1, "Stick": 0, "Boot": 0, "Fishie": 3, "Pufferfishie": 5, "Penguin": 10,
                 "Shark": 20, "POSEIDON'S TRIDENT": 1000, "Sail Boat": 100, "Pirate": 100, "Leviathan": 500, "Crab": 50,
                 "Fisherman": 50, "Mermaid": 50, "Whale": 50, "An Unspoken Level of Rod-ly-ness": 250}


def scoring(item: str, count: int) -> (str, int, int):
    """
    Return a tuple containing the item, the quantity, and the number of points generated from the item using
    SCORING_SHEET.

    :param item: A string containing the name of a game object.
    :param count: An integer representing the amount of times player collected item throughout the game.
    :precondition: item is a string representing an object in the game.
    :precondition: count is an integer representing the number of times the game object appears in the player's
    inventory.
    :postcondition: Will return a tuple containing the item, the number of times the item appears in the player's
    inventory, and an integer representing the amount of points the item generated for the player.
    :return: A tuple containing a string and two integers.

    >>> scoring('Shark', 3)
    ('Shark', 3, 60)
    >>> scoring('Stick', 50)
    ('Stick', 50, 0)
    >>> scoring('banana', 15)
    ('banana', 15, 0)
    """
    try:
        return item, count, SCORING_SHEET[item] * count
    except KeyError:
        return item, count, 0


def remove_non_legendary_items(item: str) -> bool:
    """
    Filter out the non-legendary items from a list of inventory items.

    :param item: An string containing the name of an object from the game.
    :precondition: item must be a string containing the name of an object from the game.
    :postcondition: Will return True if the item is a legendary item, else False.
    :return: A boolean value.
    """
    legendary_items = ("POSEIDON'S TRIDENT", "An Unspoken Level of Rod-ly-ness", "Leviathan")
    return item in legendary_items


def scoreboard(character):
    inventory = character["inventory"]
    totals = [(item, character["inventory"].count(item)) for item in set(inventory)]
    score = list(starmap(scoring, totals))
    total_score = sum([element[2] for element in score])
    row_headers = [element[0] for element in score]
    column_headers = ["Quantity", "Points"]
    data = [[element[1], element[2]] for element in score]
    legendary_items = filter(remove_non_legendary_items, inventory)
    print(DataFrame(data, row_headers, column_headers))
    dialogue.slow_print(dialogue.tallying_message)
    dialogue.slow_print(dialogue.final_legendary_item_display)
    dialogue.loading(3)
    for key, item in enumerate(legendary_items, 1):
        print(f"{key}.\t{item}")
    dialogue.slow_print(dialogue.transition_to_point_total)
    dialogue.loading(3)
    print(asc.cake)
    print(f"\t\t\t\t\t\t\tTotal Points:\t\t{total_score}")
    dialogue.slow_print(dialogue.final_point_total_display)


def end_game(character: dict) -> None:
    """
    End the game for the player.

    :param character: A dictionary with key-value pairs representing the player and their basic information.
    :precondition: character must have the key-value pair 'inventory', containing a list representing the players
    inventory.
    :postcondition: Will print the final dialogue into the console,
    :postcondition: Will call the scoreboard function to show the player's final score.
    :return: None
    """
    print(asc.win)
    sleep(0.5)
    dialogue.slow_print(dialogue.congratulations_pt1)
    sleep(0.5)
    print(asc.title)
    dialogue.slow_print(dialogue.congratulations_pt2)
    dialogue.loading(3)
    scoreboard(character)
    dialogue.slow_print(dialogue.end_of_game_shenanigans)
    return


def check_if_goal_attained(character: dict) -> bool:
    """
    Return if the win condition for the game has been met.

    :param character: A dictionary with key-value pairs representing the player and their basic information.
    :precondition: character must have the key-value pair 'inventory', containing a list representing the players
    inventory.
    :postcondition: Will return True if 'Leviathan' is in 'inventory', else False.
    :return: A boolean value representing whether the end condition has been met.

    >>> doctest_character = {'inventory': []}
    >>> check_if_goal_attained(doctest_character)
    False
    >>> doctest_character = {'inventory': ['Leviathan']}
    >>> check_if_goal_attained(doctest_character)
    True
    """
    sleep(1)
    return "Leviathan" in character["inventory"]


def execute_glow_up_protocol(character: dict) -> None:
    """
    Level up the character.

    :param character: A dictionary with key-value pairs representing the player and their basic information.
    :precondition: character exists and has the key-value pairs 'xp', 'rod level', 'luck', and 'charisma' containing
    integers.
    :postcondition: Will increase 'rod level' to match the value of 'xp'.
    :postcondition: Will increase 'luck' and 'charisma' by 2.
    :postcondition: Will print dialogue.level_up, current charisma, and current luck into the console.
    :return: None

    >>> doctest_character = {'xp': 1, 'rod level': 0, 'charisma': 0, 'luck': 0}
    >>> execute_glow_up_protocol(doctest_character)
    You levelled up! Your rod is now stronger.
    Current Charisma: 2 (level cap: 80)
    Current Luck: 2 (level cap: 80)
    >>> doctest_character['xp'] == doctest_character['rod level'] and doctest_character['charisma'] == 2 and \
    doctest_character['luck'] == 2
    True
    >>> second_doctest_character = {'xp': 2, 'rod level': 0, 'charisma': 17, 'luck': 36}
    >>> execute_glow_up_protocol(second_doctest_character)
    You levelled up! Your rod is now stronger.
    Current Charisma: 19 (level cap: 80)
    Current Luck: 38 (level cap: 80)
    >>> second_doctest_character['xp'] == second_doctest_character['rod level'] \
    and second_doctest_character['charisma'] == 19 and second_doctest_character['luck'] == 38
    True
    """
    character["rod level"] = character["xp"]
    character["luck"] += 2
    character["charisma"] += 2
    print(dialogue.level_up)
    print(f"Current Charisma: {character['charisma']} (level cap: 80)")
    print(f"Current Luck: {character['luck']} (level cap: 80)")
    return


def character_has_leveled(character: dict) -> bool:
    """
    Check if the character has leveled up.

    :param character: A dictionary with key-value pairs representing the player and their basic information.
    :precondition: character exists and has the key-value pairs 'xp' and 'rod level' containing integers.
    :postcondition: Will return True if the character's xp has surpassed the rod level.
    :return: A boolean indicating whether the character has leveled up.

    >>> doctest_character = {'xp': 0, 'rod level': 0}
    >>> character_has_leveled(doctest_character)
    False
    >>> doctest_character = {'xp': 1, 'rod level': 0}
    >>> character_has_leveled(doctest_character)
    True
    """
    return character["xp"] > character["rod level"]


def check_for_challenges(board: dict, character: dict) -> tuple:
    """
    Check if a challenge is happening on a given tile.

    :param board: A dictionary with key-value pairs representing tiles on the game board.
    :param character: A dictionary with key-value pairs representing the player and their basic information.
    :precondition: board has keys of tuples, representing x and y coordinates, and values representing the location
    stored at that position.
    :precondition: character exists and has the key-value pairs 'x-coordinate' and 'y-coordinate' containing integers
    within the range 0 and the game boards rows and columns.
    :postcondition: Will return a tuple containing a boolean value representing whether there is a challenge for the
    user, the name of a function corresponding to the challenge on that tile (or None if no challenge), and a dictionary
    containing the dialogue for the challenge (or None if no challenge).
    :postcondition: If there is no event, function will print a no encounter message from the dialogue module.
    :return: A tuple containing a boolean value, the name of an event function and the dialogue corresponding to the
    event function.
    """
    chance = randint(0, 100)
    position = (character['x-coordinate'], character['y-coordinate'])
    if board[position] == BOAT_TILE:
        return True, events.boat_event, dialogue.BOAT_DIALOGUE
    elif board[position] == SKULL_TILE:
        return True, events.pirate_event, dialogue.PIRATE_DIALOGUE
    elif board[position] == LEVIATHAN_TILE:
        return True, events.leviathan_event, dialogue.LEVIATHAN_DIALOGUE
    elif board[position] == LAND_TILE and chance < 18:
        return True, events.land_event, dialogue.CRAB_DIALOGUE
    elif board[position] == LAND_TILE and 36 > chance >= 18:
        return True, events.land_event, dialogue.FISHERMAN_DIALOGUE
    elif board[position] == WATER_TILE and chance < 18:
        return True, events.water_event, dialogue.MERMAID_DIALOGUE
    elif board[position] == WATER_TILE and 36 > chance >= 18:
        return True, events.water_event, dialogue.WHALE_DIALOGUE
    elif board[position] == LAND_TILE:
        print(dialogue.no_encounter_land[randint(0, len(dialogue.no_encounter_land) - 1)])
        return False, None, None
    elif board[position] == WATER_TILE:
        print(dialogue.no_encounter_sea[randint(0, len(dialogue.no_encounter_sea) - 1)])
        return False, None, None
    else:
        return False, None, None


def move_character(character: dict, move: (int, int)) -> None:
    """
    Move the character on the board to match the coordinates in move.

    :param character: A dictionary with key-value pairs representing the player and their basic information.
    :param move: A tuple representing the x and y coordinates the player wishes to move to OR the string
    'fishing'.
    :precondition: character exists and has the key-value pairs 'x-coordinate' and 'y-coordinate' containing integers
    within the range 0 and the game boards rows and columns.
    :precondition: move must be a tuple representing the x and y coordinates the player wishes to move to OR the
    string 'fishing'.
    :postcondition: Will call fishing_game from the event module if move is equal to 'fishing'
    :postcondition: Will change the x-coordinate in the character dictionary to the first value in move, and the
    y-coordinate in the character dictionary to the second value in move.
    :return: None

    >>> doctest_character = {'x-coordinate': 0, 'y-coordinate': 0}
    >>> doctest_move = 'fishing'
    >>> move_character(doctest_character, doctest_move)
    >>> doctest_character['x-coordinate'], doctest_character['y-coordinate'] == doctest_move
    True
    >>> doctest_move = (1, 0)
    >>> move_character(doctest_character, doctest_move)
    >>> doctest_character['x-coordinate'], doctest_character['y-coordinate'] == doctest_move
    True
    >>> doctest_move = (0, 1)
    >>> move_character(doctest_character, doctest_move)
    >>> doctest_character['x-coordinate'], doctest_character['y-coordinate'] == doctest_move
    True
    """
    if move == "fishing":
        events.fishing_game(character)
        return
    else:
        x_direction, y_direction = move
        character["x-coordinate"] = x_direction
        character["y-coordinate"] = y_direction
        return


def describe_invalid_move(board: dict, character: dict, move) -> str:
    """
    Return a random message from a list of messages in the dialogue module describing to the player the invalid move
    they attempted.

    :param board: A dictionary with key-value pairs representing tiles on the game board.
    :param character: A dictionary with key-value pairs representing the player and their basic information.
    :param move: A tuple representing the x and y coordinates the player wishes to move to OR the string
    'fishing'.
    :precondition: board has keys of tuples, representing x and y coordinates, and values representing the location
    stored at that position.
    :precondition: character exists and has the key-value pairs 'x-coordinate' and 'y-coordinate' containing integers
    within the range 0 and the game boards rows and columns.
    :precondition: move must be a tuple representing the x and y coordinates the player wishes to move to OR the
    string 'fishing'.
    :postcondition: Will return a random string from the dialogue module containing a message describing the invalid
    movement.
    :return: A random string.
    """
    position = (character['x-coordinate'], character['y-coordinate'])
    if move == "fishing":
        return dialogue.invalid_fish[randint(0, len(dialogue.invalid_fish) - 1)]
    if board[position] == WATER_TILE:
        return dialogue.invalid_move_water[randint(0, len(dialogue.invalid_move_water) - 1)]
    elif board[position] == LAND_TILE:
        return dialogue.invalid_move_land[randint(0, len(dialogue.invalid_move_land) - 1)]
    elif board[position] == ISLAND_TILE:
        return dialogue.invalid_move_island[randint(0, len(dialogue.invalid_move_island) - 1)]


def validate_move(board: dict, character: dict, direction, rows: int, columns: int) -> tuple:
    """
    Validate the user's move coming from get_user_choice, and returns a tuple containing their updated position on the
    board. If the move is invalid, the function also returns False, else True.

    :param board: A dictionary with key-value pairs representing tiles on the game board.
    :param character: A dictionary with key-value pairs representing the player and their basic information.
    :param direction: A tuple representing the x and y coordinates the player wishes to move to OR the string
    'fishing' and a boolean to prompt the fishing game OR the boolean False.
    :param rows: An integer representing the number of rows in the game board.
    :param columns: An integer representing the number of columns in the game board.
    :precondition: board has keys of tuples, representing x and y coordinates, and values representing the location
    stored at that position.
    :precondition: character exists and has the key-value pairs 'x-coordinate' and 'y-coordinate' containing integers
    within the range 0 and the game boards rows and columns AND a key-value pair 'rod level' which contains the player
    level.
    :precondition: direction must be a tuple representing the x and y coordinates the player wishes to move to OR the
    string 'fishing' and a boolean to prompt the fishing game OR the boolean False.
    :precondition: rows equals to the number of rows represented in board.
    :precondition: columns equals to the number of columns represented in board.
    :postcondition: If direction is False, the function will return the characters current coordinates and the boolean
    False, as a tuple.
    :postcondition: If direction is equal to 'fishing', the function will return the string 'fishing' and a boolean
    representing whether it is possible to play the fishing game from this tile.
    :postcondition: If direction is a tuple of integers, the function will return a tuple representing the coordinates
    to move the player to, and a boolean representing whether the user's desired move was valid.
    :return: A tuple containing integers representing coordinates to move the character to, or the string 'fishing',
    AND a boolean representing whether the move was valid.

    >>> doctest_board = {(0, 0): LAND_TILE, (0, 1): LAND_TILE, (1, 0): WATER_TILE, (1, 1): LAND_TILE}
    >>> doctest_character = {'x-coordinate': 0, 'y-coordinate': 0, 'rod level': 0}
    >>> doctest_direction = 'fishing'
    >>> validate_move(doctest_board, doctest_character, doctest_direction, 2, 2)
    ('fishing', True)
    >>> doctest_direction = (0, 1)
    >>> validate_move(doctest_board, doctest_character, doctest_direction, 2, 2)
    ((0, 1), True)
    >>> doctest_direction = False
    >>> validate_move(doctest_board, doctest_character, doctest_direction, 2, 2)
    ((0, 0), False)
    """
    if not direction:
        return (character["x-coordinate"], character["y-coordinate"]), False
    if direction == "fishing":
        x_coordinate = character["x-coordinate"]
        y_coordinate = character["y-coordinate"]
        counter = 0
        try:
            counter += board[x_coordinate - 1, y_coordinate] == WATER_TILE
        except KeyError:
            pass
        try:
            counter += board[x_coordinate + 1, y_coordinate] == WATER_TILE
        except KeyError:
            pass
        try:
            counter += board[x_coordinate, y_coordinate - 1] == WATER_TILE
        except KeyError:
            pass
        try:
            counter += board[x_coordinate, y_coordinate + 1] == WATER_TILE
        except KeyError:
            pass
        return "fishing", counter > 0
    x_direction, y_direction = direction
    if x_direction > columns - 1 or x_direction < 0:
        return (character["x-coordinate"], character["y-coordinate"]), False
    elif y_direction > rows - 1 or y_direction < 0:
        return (character["x-coordinate"], character["y-coordinate"]), False
    elif board[direction] == WATER_TILE and character["rod level"] == 0:
        return (character["x-coordinate"], character["y-coordinate"]), False
    else:
        return direction, True


def get_user_choice(character: dict):
    """
    Ask the user to select one of the enumerated options in the console, and log their selection. Users respond with the
    enumerated number corresponding to their desired selection, else the function returns False. Responding with an
    enumerated option causes the function to return a value representing their selection.

    :param character: A dictionary with key-value pairs representing the player and their basic information.
    :precondition: character exists and has the key-value pairs 'x-coordinate' and 'y-coordinate' containing integers
    within the range 0 and the game boards rows and columns.
    :postcondition: Will enumerate the available options and print them into the console.
    :postcondition: If the user selects one of the available options (by typing the corresponding number into the
    console), the function will return value(s) that match the user's decision.
    :postcondition: If the user selects the options 1 through 4 inclusive, the function will return the coordinates of
    the tile the user wishes to move their character to.
    :postcondition: If the user selects option 5, the function will return "fishing", to prompt the game function to run
    the fishing game.
    :postcondition: If the user selects option 6, function will print 'Thanks for playing', then the call stack will be
    terminated and the game will end.
    :postcondition: If the user does not enter a valid option from the enumerated list, the function will return False.
    :return: A tuple of integers representing coordinates, a string, None, or False, depending on the user input.
    """
    print("Possible Actions")
    directions = ("north", "south", "east", "west", "fish", "quit")
    for key, direction in enumerate(directions, 1):
        print(f"{key}.\t{direction}")
    direction = input("\nAnswer Here:\t")
    if direction == "1":
        return character["x-coordinate"] - 1, character["y-coordinate"]
    elif direction == "2":
        return character["x-coordinate"] + 1, character["y-coordinate"]
    elif direction == "3":
        return character["x-coordinate"], character["y-coordinate"] + 1
    elif direction == "4":
        return character["x-coordinate"], character["y-coordinate"] - 1
    elif direction == "5":
        return "fishing"
    elif direction == "6":
        print("Thanks for playing")
        quit()
    else:
        return False


def describe_current_location(board: dict, character: dict, columns: int) -> None:
    """
    Describe the current state of the game board, as well as the players location on the game board in a visually
    pleasing manner (10 x 10 grid of Unicode characters).

    :param board: A dictionary with key-value pairs representing tiles on the game board.
    :param character: A dictionary with key-value pairs representing the player and their basic information.
    :param columns: An integer representing the number of columns in the game board.
    :precondition: board has keys of tuples, representing x and y coordinates, and values representing the location
    stored at that position.
    :precondition: character exists and has the key-value pairs 'x-coordinate' and 'y-coordinate' containing integers
    within the range 0 and the game boards rows and columns.
    :precondition: columns equals to the number of columns represented in board.
    :postcondition: Will print in the console a beautified description of board, in the form of a 10 x 10 grid of icons
    (represented with Unicode characters).
    :return: None
    """
    position = (character['x-coordinate'], character['y-coordinate'])
    tile = board[position]
    if board[position] == WATER_TILE:
        board[position] = BOAT_TILE
    if board[position] == LAND_TILE or board[position] == ISLAND_TILE:
        board[position] = PLAYER_TILE
    counter = 1
    for icon in board.values():
        if counter % columns == 0:
            print(icon[0])
        else:
            print(icon[0], end="")
        counter += 1
    board[position] = tile
    return


def make_character(columns: int) -> dict:
    """
    Create a character dictionary to store player information while the game function is running.

    :param columns: An integer representing the number of columns on the game board.
    :precondition: columns is the same integer value as the number of columns on the game board.
    :precondition: User must enter required input value to complete function.
    :postcondition: Will create a character dictionary containing key-value pairs necessary for the game to function.
    Dictionary will contain a key-value pair called name, which contains a user inputted value representing their
    character's name.
    :return: A dictionary representing the player for the duration of the game.
    """
    dialogue.slow_print(dialogue.get_name)
    name = input("Answer Here:\t\t")
    character = {
        "name": name,
        "x-coordinate": columns - 1,
        "y-coordinate": 0,
        "luck": 40,
        "charisma": 40,
        "rod level": 0,
        "xp": 0,
        "inventory": ["Mama's Fishing Rod"]
    }
    return character


def make_board(rows: int, columns: int) -> dict:
    """
    Create a dictionary representing a game board of a variable row and column size. Coordinates on the board are
    represented in tuples with tiles represented using unicode characters.

    :param rows: An integer representing the number of rows in the game board.
    :param columns: An integer representing the number of columns in the game board.
    :precondition: rows, columns must be integers greater than or equal to 10.
    :postcondition: Will create a dictionary representing a game board, with row rows and column columns.
    :return: A dictionary.
    """
    board = {}
    for row in range(rows):
        for column in range(columns):
            board[row, column] = WATER_TILE
    for column in range(columns):
        board[9, column] = LAND_TILE
    for column in range(columns):
        if column > 1:
            board[8, column] = LAND_TILE
    for column in range(columns):
        if column > 5:
            board[7, column] = LAND_TILE
    for column in range(columns):
        if column > 8:
            board[6, column] = LAND_TILE
    island_tiles = [(1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (2, 2), (2, 1), (4, 2)]
    for tile in island_tiles:
        board[tile] = ISLAND_TILE
    board[(6, 9)] = BOAT_TILE
    board[(2, 2)] = SKULL_TILE
    return board


def game() -> None:
    """
    The game's main engine. This function operates all the logic for the game, and all helper functions branch off from
    here.

    :postcondition: Will run the Fish or Flirt game to completion.
    :return: None.
    """
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    print(asc.title)
    dialogue.slow_print(dialogue.welcome_message)
    dialogue.slow_print(dialogue.choose_class)
    for key, class_option in enumerate(dialogue.class_options, 1):
        print(f"{key}.\t{class_option}")
    _ = input("Answer Here:\t\t")
    dialogue.slow_print(dialogue.after_class_input)
    dialogue.slow_print(dialogue.story_1)
    character = make_character(columns)
    achieved_goal = False
    while not achieved_goal:
        describe_current_location(board, character, columns)
        direction = get_user_choice(character)
        move, valid_move = validate_move(board, character, direction, rows, columns)
        if valid_move:
            move_character(character, move)
            there_is_a_challenge, challenge, event_dialogue = check_for_challenges(board, character)
            if there_is_a_challenge:
                challenge(board, character, event_dialogue)
                if character_has_leveled(character):
                    execute_glow_up_protocol(character)
            achieved_goal = check_if_goal_attained(character)
        else:
            print(describe_invalid_move(board, character, move))
    end_game(character)
    return


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()

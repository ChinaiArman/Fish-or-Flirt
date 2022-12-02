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


WATER_TILE = "\U0001F30A"
LAND_TILE = "\U0001F3D6"
BOAT_TILE = "\U000026F5"
ISLAND_TILE = "\U0001F334"
PLAYER_TILE = "\U0001F3A3"
SKULL_TILE = "\U0001F480"
LEVIATHAN_TILE = "\U00002757"


def scoring(item, count):
    if item == "banana":
        return item, count, count * 5
    elif item == "johnson":
        return item, count, count * 17
    else:
        return item, count, count * 0


def end_game(character):
    print(asc.win)
    print("[LEX] END GAME DIALOGUE")
    inventory = character["inventory"]
    totals = [(item, character["inventory"].count(item)) for item in set(inventory)]
    score = list(starmap(scoring, totals))
    total_score = sum([element[2] for element in score])
    print("[ARMAN] NEEDS TO BE BEAUTIFIED")
    for item in score:
        print(f"{item[1]}x {item[0]}:\t\t\t{item[2]}\n")
    print(f"Total Score:\t\t{total_score}")


def check_if_goal_attained(character):
    sleep(1)
    return "Leviathan" in character["inventory"]


def execute_glow_up_protocol(character):
    character["rod level"] = character["xp"]
    character["luck"] += 2
    character["charisma"] += 2
    print(dialogue.level_up)


def character_has_leveled(character):
    return character["xp"] > character["rod level"]


def check_for_challenges(board, character):
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


def move_character(character, move):
    if move == "fishing":
        events.fishing_game(character)
        return
    else:
        x_direction, y_direction = move
        character["x-coordinate"] = x_direction
        character["y-coordinate"] = y_direction
        return


def describe_invalid_move(board, character, move):
    position = (character['x-coordinate'], character['y-coordinate'])
    if move == "fishing":
        return "[LEX] INVALID FISH MOVE"
    if board[position] == WATER_TILE:
        return dialogue.invalid_move_water[randint(0, len(dialogue.invalid_move_water) - 1)]
    elif board[position] == LAND_TILE:
        return dialogue.invalid_move_land[randint(0, len(dialogue.invalid_move_land) - 1)]
    elif board[position] == ISLAND_TILE:
        return dialogue.invalid_move_island[randint(0, len(dialogue.invalid_move_island) - 1)]


def validate_move(board, character, direction, rows, columns):
    if not direction:
        return (character["x-coordinate"], character["y-coordinate"]), False
    if direction == "fishing":
        try:
            x_coordinate = character["x-coordinate"]
            y_coordinate = character["y-coordinate"]
            return "fishing", board[x_coordinate - 1, y_coordinate] == WATER_TILE or \
                board[x_coordinate + 1, y_coordinate] == WATER_TILE or \
                board[x_coordinate, y_coordinate - 1] == WATER_TILE or \
                board[x_coordinate, y_coordinate + 1] == WATER_TILE
        except KeyError:
            return "fishing", False
    x_direction, y_direction = direction
    if x_direction > columns - 1 or x_direction < 0:
        return (character["x-coordinate"], character["y-coordinate"]), False
    elif y_direction > rows - 1 or y_direction < 0:
        return (character["x-coordinate"], character["y-coordinate"]), False
    elif board[direction] == WATER_TILE and character["rod level"] == 0:
        return (character["x-coordinate"], character["y-coordinate"]), False
    else:
        return direction, True


def get_user_choice(character):
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


def main():
    game()


if __name__ == "__main__":
    main()

"""
Arman Chinai | A01317650
Lex Wong | A01322278
"""


# import random


def leviathan_event(board, character):
    water_tile = "\U0001F30A"
    leviathan_tile = "\U00002757"
    position = (character['x-coordinate'], character['y-coordinate'])

    # story here

    board[position] = water_tile
    board[(1, 8)] = leviathan_tile
    character["xp"] += 1
    return


def pirate_event(board, character):
    island_tile = "\U0001F334"
    leviathan_tile = "\U00002757"
    position = (character['x-coordinate'], character['y-coordinate'])

    # story here

    board[position] = island_tile
    board[(1, 8)] = leviathan_tile
    character["xp"] += 1
    return


def boat_event(board, character):
    water_tile = "\U0001F30A"
    position = (character['x-coordinate'], character['y-coordinate'])

    # story here

    board[position] = water_tile
    character["xp"] += 1
    return


def random_land_event(character):
    pass


def random_water_event(character):
    pass


def check_if_goal_attained(character):
    if character["rod level"] == 3:
        return True
    else:
        return False


def execute_glow_up_protocol(character):
    character["rod level"] = character["xp"]
    print("LEVELUP")


def character_has_leveled(character):
    if character["xp"] > character["rod level"]:
        return True
    else:
        return False


def execute_challenge_protocol(character):
    character["rod level"] = character["xp"]


def check_for_challenges(board, character):
    boat_tile = "\U000026F5"
    pirate_tile = "\U0001F480"
    leviathan_tile = "\U00002757"
    position = (character['x-coordinate'], character['y-coordinate'])
    if board[position] == boat_tile:
        return True, boat_event
    elif board[position] == pirate_tile:
        return True, pirate_event
    elif board[position] == leviathan_tile:
        return True, leviathan_event
    else:
        return False, None


def move_character(character, move):
    x_direction, y_direction = move
    character["x-coordinate"] = x_direction
    character["y-coordinate"] = y_direction
    return


def validate_move(board, character, direction, rows, columns):
    water_tile = "\U0001F30A"
    x_direction, y_direction = direction
    if (character["x-coordinate"], character["y-coordinate"]) == direction:
        return (character["x-coordinate"], character["y-coordinate"]), False
    elif x_direction > columns - 1 or x_direction < 0:
        return (character["x-coordinate"], character["y-coordinate"]), False
    elif y_direction > rows - 1 or y_direction < 0:
        return (character["x-coordinate"], character["y-coordinate"]), False
    elif board[direction] == water_tile and character["rod level"] == 0:
        return (character["x-coordinate"], character["y-coordinate"]), False
    else:
        return direction, True


def get_user_choice(character):
    print("Pick a direction to travel")
    directions = ["north", "south", "east", "west"]
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
    else:
        return character["x-coordinate"], character["y-coordinate"]


def describe_current_location(board, character, columns):
    water_tile = "\U0001F30A"
    boat_icon = "\U000026F5"
    land_tile = "\U0001F3D6"
    island_tile = "\U0001F334"
    fisherman_icon = "\U0001F3A3"
    position = (character['x-coordinate'], character['y-coordinate'])
    tile = board[position]
    if board[position] == water_tile:
        board[position] = boat_icon
    if board[position] == land_tile or board[position] == island_tile:
        board[position] = fisherman_icon
    counter = 1
    for icon in board.values():
        if counter % columns == 0:
            print(icon[0])
        else:
            print(icon[0], end="")
        counter += 1
    board[position] = tile


def make_character():
    name = input("name?")
    character = {
        "name": name,
        "x-coordinate": 9,
        "y-coordinate": 0,
        "luck": 0,
        "charisma": 0,
        "rod level": 0,
        "xp": 0,
        "inventory": []
    }
    return character


def make_board(rows, columns):
    water_tile = "\U0001F30A"
    land_tile = "\U0001F3D6"
    boat_tile = "\U000026F5"
    island_tile = "\U0001F334"
    skull_tile = "\U0001F480"
    board = {}
    # WATER
    for row in range(rows):
        for column in range(columns):
            board[row, column] = water_tile
    # SAND
    for column in range(columns):
        board[9, column] = land_tile
    for column in range(columns):
        if column > 1:
            board[8, column] = land_tile
    for column in range(columns):
        if column > 5:
            board[7, column] = land_tile
    for column in range(columns):
        if column > 8:
            board[6, column] = land_tile
    # BOAT
    board[(6, 9)] = boat_tile
    board[(1, 3)] = island_tile
    board[(2, 3)] = island_tile
    board[(3, 3)] = island_tile
    board[(3, 2)] = island_tile
    board[(3, 1)] = island_tile
    board[(2, 2)] = island_tile
    board[(2, 1)] = island_tile
    board[(4, 2)] = island_tile
    board[(2, 2)] = skull_tile
    return board


def game():
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    character = make_character()
    achieved_goal = False
    while not achieved_goal:
        describe_current_location(board, character, columns)
        direction = get_user_choice(character)
        move, valid_move = validate_move(board, character, direction, rows, columns)
        if valid_move:
            move_character(character, move)
            there_is_a_challenge, challenge = check_for_challenges(board, character)
            if there_is_a_challenge:
                challenge(board, character)
                if character_has_leveled(character):
                    execute_glow_up_protocol(character)
            achieved_goal = check_if_goal_attained(character)
        else:
            print("Tell the user they can’t go in that direction")
    print("end of game shenanigans")


def main():
    game()


if __name__ == "__main__":
    main()

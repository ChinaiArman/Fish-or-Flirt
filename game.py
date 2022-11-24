"""
Arman Chinai | A01317650
Lex Wong | A01322278
"""


# import random


def boat_event(board, character):
    character["icon"] = "\U000026F5"
    position = (character['x-coordinate'], character['y-coordinate'])
    board[position] = "\U0001F3D6"



def random_land_event(character):
    pass


def random_water_event(character):
    pass


def check_if_goal_attained(board, character):
    return False


def execute_glow_up_protocol():
    pass


def character_has_leveled():
    return True


def execute_challenge_protocol(character):
    pass


def check_for_challenges(board, character):
    position = (character['x-coordinate'], character['y-coordinate'])
    if board[position] == "\U000026F5":
        return True, boat_event
    else:
        return False, None


def move_character(character, move):
    x_direction, y_direction = move
    character["x-coordinate"] = x_direction
    character["y-coordinate"] = y_direction
    return


def validate_move(board, character, direction, rows, columns):
    x_direction, y_direction = direction
    if (character["x-coordinate"], character["y-coordinate"]) == direction:
        return (character["x-coordinate"], character["y-coordinate"]), False
    elif x_direction > columns - 1 or x_direction < 0:
        return (character["x-coordinate"], character["y-coordinate"]), False
    elif y_direction > rows - 1 or y_direction < 0:
        return (character["x-coordinate"], character["y-coordinate"]), False
    elif board[direction] == "\U0001F30A" and character["rod level"] == 0:
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
    position = (character['x-coordinate'], character['y-coordinate'])
    tile = board[position]
    board[position] = character["icon"]
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
        "icon": "\U0001F9CD",
        "inventory": []
    }
    return character


def make_board(rows, columns):
    sea_tile = "\U0001F30A"
    land_tile = "\U0001F3D6"
    boat_tile = "\U000026F5"
    board = {}
    # WATER
    for row in range(rows):
        for column in range(columns):
            board[row, column] = sea_tile
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
            # describe_current_location(board, character, columns)
            there_is_a_challenge, challenge = check_for_challenges(board, character)
            if there_is_a_challenge:
                challenge(board, character)
                if character_has_leveled():
                    execute_glow_up_protocol()
            achieved_goal = check_if_goal_attained(board, character)
        else:
            print("Tell the user they can’t go in that direction")
    print("end of game shenanigans")


def main():
    game()


if __name__ == "__main__":
    main()

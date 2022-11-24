"""
Arman Chinai | A01317650
Lex Wong | A01322278
"""


def check_if_goal_attained(board, character):
    return False


def execute_glow_up_protocol():
    pass


def character_has_leveled():
    return True


def execute_challenge_protocol(character):
    pass


def check_for_challenges():
    return True


def move_character(character):
    pass


def validate_move(board, character, direction):
    if direction == "1" and character["x-coordinate"] != 0:
        character["x-coordinate"] -= 1
        return True
    elif direction == "2" and character["x-coordinate"] != 9:
        character["x-coordinate"] += 1
        return True
    elif direction == "3" and character["y-coordinate"] != 9:
        character["y-coordinate"] += 1
        return True
    elif direction == "4" and character["y-coordinate"] != 0:
        character["y-coordinate"] -= 1
        return True
    else:
        return False


def get_user_choice():
    print("Pick a direction to travel")
    directions = ["north", "south", "east", "west"]
    for key, direction in enumerate(directions, 1):
        print(f"{key}.\t{direction}\t\t", end="")
    return input("\nAnswer Here:\t")


def describe_current_location(board, character, columns):
    position = (character['x-coordinate'], character['y-coordinate'])
    tile = board[position]
    board[position] = "\U0001F606"
    counter = 1
    for icon in board.values():
        if counter % columns == 0:
            print(icon)
        else:
            print(icon, end="")
        counter += 1
    board[position] = tile


def make_character(name):
    character = {
        "name": name,
        "x-coordinate": 9,
        "y-coordinate": 0,
        "luck": 0,
        "charisma": 0,
        "rod level": 0,
        "inventory": []
    }
    return character


def make_board(rows, columns):
    board = {}
    for row in range(rows):
        for column in range(columns):
            board[row, column] = "\U0001F30A"
    return board


def game():
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    character = make_character("Player name")
    achieved_goal = False
    while not achieved_goal:
        describe_current_location(board, character, columns)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character)
            # describe_current_location(board, character, columns)
            there_is_a_challenge = check_for_challenges()
            if there_is_a_challenge:
                execute_challenge_protocol(character)
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

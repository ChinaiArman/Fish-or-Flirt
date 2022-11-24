"""
Arman Chinai | A01317650
Lex Wong | A01322278
"""


def check_if_goal_attained(board, character):
    return True


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
    return True


def get_user_choice():
    choice = 0
    return choice


def describe_current_location(board, character):
    pass


def make_character(name):
    character = {
        "name": name,
        "x-coordinate": 0,
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
            board[row, column] = "\U0001f600"
    return board


def game():
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    print(board)
    character = make_character("Player name")
    achieved_goal = False
    while not achieved_goal:
        describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character)
            describe_current_location(board, character)
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

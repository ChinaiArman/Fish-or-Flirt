# print("Pick a direction to travel")
# directions = ["north", "south", "east", "west"]
#
# for key, direction in enumerate(directions, 1):
#     print(f"{key}.\t{direction}\t\t", end="")


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

# import regex as re


# def get_lines() -> list[str]:
#     return open("./input.txt", "r").read().splitlines()

# def parse_game_string(game_string: str) -> tuple:
#     match = re.match(r"Game (\d+): (.+)", game_string)
#     game_id, cube_info = match.groups()

#     cubes = [cube.split() for cube in cube_info.split(";")]
#     cube_counts = {'red': 0, 'green': 0, 'blue': 0}

#     for cube in cubes:
#         color = cube[-1].rstrip(',')
#         cube_counts[color] += int(cube[0])

#     return int(game_id), cube_counts

# class PartOne:
#     @staticmethod
#     def find_answer() -> int:
#         valid_game_ids: list = []
#         lines = get_lines()

#         for line in lines:
#             game_id, cube_counts = parse_game_string(line)
#             if (
#                 cube_counts['red'] <= 12 and
#                 cube_counts['green'] <= 13 and
#                 cube_counts['blue'] <= 14 or
#                 cube_counts['red'] + cube_counts['green'] + cube_counts['blue'] == 39
#             ):
#                 valid_game_ids.append(game_id)

#         print(valid_game_ids)
#         return sum(valid_game_ids)


# if __name__ == "__main__":
#     print("Part one...")
#     part1_answer = PartOne.find_answer()
#     print(f"Value: {part1_answer}.")

import regex as re

def get_lines() -> list[str]:
    return open("./input.txt", "r").read().splitlines()

def parse_game_string(game_string: str) -> tuple:
    match = re.match(r"Game (\d+): (.+)", game_string)
    game_id, cube_info = match.groups()

    cubes = [cube.split() for cube in cube_info.replace(';', ',').split(',')]
    cube_counts = {'red': 0, 'green': 0, 'blue': 0}

    for cube in cubes:
        color = cube[-1].strip(',')
        cube_counts[color] = max(cube_counts[color], int(cube[0]))

    return int(game_id), cube_counts


class PartOne:
    @staticmethod
    def find_answer() -> int:
        valid_game_ids: list = []
        lines = get_lines()

        for line in lines:
            game_id, cube_counts = parse_game_string(line)
            if cube_counts['red'] <= 12 and \
               cube_counts['green'] <= 13 and \
               cube_counts['blue'] <= 14: valid_game_ids.append(game_id)

        return sum(valid_game_ids)
    
    def test(value: int) -> bool:
        if value != 2369: return False
        return True    


if __name__ == "__main__":
    print("Part one...")
    part1_answer = PartOne.find_answer()
    print(f"Value: {part1_answer} | Test {'passed' if PartOne.test(part1_answer) else 'failed, incorrect value'}.")

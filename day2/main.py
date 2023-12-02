import math


def do_part_1(CUBES_AVAILABLE, game):
    game_id, sub_games = parse_game(game)
    for sub_game in sub_games:
        cube_list = sub_game.split(',')
        for color_count_str in cube_list:
            color, count = get_color_count(color_count_str)
            if count > CUBES_AVAILABLE[color]:
                return 0
    return game_id


def do_part_2(game):
    min_count_map = {'red': 0, 'green': 0, 'blue': 0}
    _, sub_games = parse_game(game)
    for sub_game in sub_games:
        cube_list = sub_game.split(',')
        for color_count_str in cube_list:
            color, count = get_color_count(color_count_str)
            if min_count_map[color] < count:
                min_count_map[color] = count
    power = math.prod([val for val in min_count_map.values()])
    return power


def parse_game(game):
    game_id = int(game.split(':')[0].split()[1])
    sub_games = game.split(':')[1].split(';')
    return game_id, sub_games


def get_color_count(num_color_input):
    count = int(num_color_input.split()[0])
    color = num_color_input.split()[1]
    return color, count


if __name__ == "__main__":

    with open('input.txt') as f:
        games = f.readlines()

    CUBES_AVAILABLE = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    sum_1 = 0
    sum_2 = 0

    for game in games:
        # Part 1
        sum_1 += do_part_1(CUBES_AVAILABLE, game)
        # Part 2
        sum_2 += do_part_2(game)

    print(f'Part 1 answer: {sum_1}')
    print(f'Part 2 answer: {sum_2}')

test_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

def get_input():
    #return test_input
    return read_file()

def read_file():
    with open("input.txt") as f:
        data = f.read()
    return data

def serialize_input(input: str):
    games = {}
    for line in input.split('\n'):
        if len(line) == 0:
            continue
        idstr, datastr = line.split(':')
        id = int(idstr.split(' ')[-1])
        sets = []
        for set in datastr.split(';'):
            set_dict = {}
            for colorstr in set.split(','):
                qtystr, color = colorstr.strip().split(' ')
                qty = int(qtystr)
                existing_max = set_dict.get(color, None)
                if existing_max == None or existing_max < qty:
                    set_dict[color] = qty
            sets.append(set_dict)
        games[id] = sets
    return games

def get_game_validity(game, max_r:int, max_g:int, max_b:int):
    for set in game:
        cur_r = set.get("red",0)
        cur_g = set.get("green",0)
        cur_b = set.get("blue",0)
        if cur_r > max_r or cur_g > max_g or cur_b > max_b:
            return False
    return True

def compute_game_minimums(game):
    max_r = 0
    max_g = 0
    max_b = 0
    for set in game:
        max_r = max(max_r, set.get("red",0))
        max_g = max(max_g, set.get("green",0))
        max_b = max(max_b, set.get("blue",0))
    return max_r, max_g, max_b

def p1():
    input = get_input()
    games = serialize_input(input)
    valid_id_sum = 0
    for game_id in games:
        game_data = games.get(game_id)
        if get_game_validity(game_data, 12, 13, 14):
            valid_id_sum += game_id
    print(valid_id_sum)

def p2():
    input = get_input()
    games = serialize_input(input)
    game_power_sum = 0
    for game_id in games:
        game_data = games.get(game_id)
        r, g, b = compute_game_minimums(game_data)
        power = r * g * b
        game_power_sum += power
    print(game_power_sum)

if __name__ == "__main__":
    p2()

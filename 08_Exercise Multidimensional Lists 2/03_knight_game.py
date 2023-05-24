def check_possible_attacks(horse_pos):
    count_of_attacks = 0
    for row, col in attack_moves:
        attacked_position = (row + horse_pos[0], col + horse_pos[1])
        if check_valid_index(attacked_position):
            if matrix[attacked_position[0]][attacked_position[1]] == "K":
                count_of_attacks += 1
    return count_of_attacks


def check_valid_index(coord):
    if 0 <= coord[0] < rows and 0 <= coord[1] < rows:
        return True
    return False


def horse_to_remove(att_moves_by_horse):
    if len(set(att_moves_by_horse.values())) == 1:
        return next(iter(att_moves_by_horse.keys()))
    else:
        return max(att_moves_by_horse, key=att_moves_by_horse.get)


attack_moves = {
    (-2, -1), #UL
    (-2, 1),  #UR
    (2, -1),  #DL
    (2, 1),   #DR
    (-1, 2),  #RU
    (1, 2),   #RD
    (-1, -2), #LU
    (1, -2)   #LD
}

rows = int(input())

matrix = [[el for el in list(input())] for _ in range(rows)]

moves_required = 0

while True:
    attack_moves_by_horse = {}
    for row_index in range(rows):
        for col_index in range(rows):
            if matrix[row_index][col_index] == "K":
                horse_position = (row_index, col_index)
                attack_moves_by_horse[horse_position] = check_possible_attacks(horse_position)

    if not any(value > 0 for value in attack_moves_by_horse.values()):
        break

    horse_to_kill = horse_to_remove(attack_moves_by_horse)
    matrix[horse_to_kill[0]][horse_to_kill[1]] = "0"
    moves_required += 1

print(moves_required)

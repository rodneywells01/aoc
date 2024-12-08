from re import search


f = open("input.txt")

data = list()
for line in f:
    data.append(line.rstrip())


def is_valid(row_idx, col_idx):
    is_valid = not(row_idx < 0 or col_idx < 0 or row_idx >= len(data) or col_idx >= len(data[row_idx]))
    if not is_valid:
        print("Failed validation check")
        # print(f"{row_idx} vs {len(data)}")
        # print(f"{col_idx} vs {len(data[row_idx])}")
    return is_valid

def check_for_directionality(row_idx, col_idx, row_direction, col_direction, search_term="XMAS"):
    # Horizontal
    valid = True
    for x in range(len(search_term)):
        next_row_idx = row_idx + x * row_direction
        next_col_idx = col_idx + x * col_direction
        # print(data[next_row_idx][next_col_idx])
        # print(search_term[x])
        if not is_valid(next_row_idx, next_col_idx) or data[next_row_idx][next_col_idx] != search_term[x]:
            # print(f"{data[next_row_idx][next_col_idx]} vs {search_term[x]}")
            # print("not search term")
            valid=False
            break

    if valid:
        print(f"Found on {row_idx}, {col_idx}")
        return 1

    return 0

def check_for_cross_mas(row_idx, col_idx):
    cross_mas_tests = [
        check_for_directionality(row_idx-1, col_idx-1, 1, 1, search_term="MAS"), # Start top left
        check_for_directionality(row_idx+1, col_idx-1, -1, 1, search_term="MAS"), # Bottom left
        check_for_directionality(row_idx-1, col_idx+1, 1, -1, search_term="MAS"), # top right
        check_for_directionality(row_idx+1, col_idx+1, -1, -1, search_term="MAS"), # bottom right
    ]

    if sum(cross_mas_tests) == 2:
        print("Cross MAS founds")
        return 1

    return 0


def check_for_xmas(row_idx, col_idx):
    """
    XMAS can be forwards, backwards, up, down, diagonal
    """
    print(f"Checking {row_idx}, {col_idx}")
    xmas_tests = [
        check_for_directionality(row_idx, col_idx, 0, 1), # Forwards
        check_for_directionality(row_idx, col_idx, 0, -1), # Backwards
        check_for_directionality(row_idx, col_idx, 1, 0), # Down
        check_for_directionality(row_idx, col_idx, -1, 0), # Up

        check_for_directionality(row_idx, col_idx, -1, -1), # Up left
        check_for_directionality(row_idx, col_idx, -1, 1), # Up right
        check_for_directionality(row_idx, col_idx, 1, -1), # Down left
        check_for_directionality(row_idx, col_idx, 1, 1), # Down right
    ]

    print(xmas_tests)
    instances = sum(xmas_tests)
    print(f"Found {instances} instances")
    return instances


    # Horizontal
    valid = True
    for x in range(1,4):
        next_row_idx = row_idx
        next_col_idx = col_idx + x
        print(x)
        # print(data[next_row_idx][next_col_idx])
        # print(search_term[x])
        if not is_valid(next_row_idx, next_col_idx) or data[next_row_idx][next_col_idx] != search_term[x]:
            # print(f"{data[next_row_idx][next_col_idx]} vs {search_term[x]}")

            # print("not search term")
            valid=False
            break

    if valid:
        xmas_instances += 1
        print(f"Found on {row_idx}, {col_idx}")



    return xmas_instances


def part_one():
    total = 0
    for row_idx in range(len(data)):
        for col_idx in range(len(data[row_idx])):
            if data[row_idx][col_idx] == 'X':
                total += check_for_xmas(row_idx, col_idx)
    print(f"Part one: {total}")

def part_two():
    total = 0
    for row_idx in range(len(data)):
        for col_idx in range(len(data[row_idx])):
            if data[row_idx][col_idx] == 'A':
                total += check_for_cross_mas(row_idx, col_idx)
    print(f"Part two: {total}")


# part_one()
part_two()
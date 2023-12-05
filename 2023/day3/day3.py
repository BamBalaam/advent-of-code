from functools import reduce

def get_matrix_from_file_lines(lines):
    for i in range(len(lines)):
        lines[i] = [*lines[i].strip()]
    return lines

def get_neighbours(matrix, x, y):
    neighbours = []
    matrix_max_x = len(matrix)
    matrix_max_y = len(matrix[0])
    for k in (x-1, x, x+1):
        for l in (y-1, y, y+1):
            if (
                ( (x,y) != (k,l) )
                and ( 0 <=  k <= matrix_max_x-1 )
                and ( 0 <=  l <= matrix_max_y-1 )
            ):
                neighbours.append((matrix[k][l], k, l))

    return neighbours

def get_symbols(neighbours):
    neighbour_symbols = {}
    symbols_list = ['*', '/', '@', '&', '$', '=', '#', '-', '+', '%']
    for neighbour in neighbours:
        if neighbour[0] in symbols_list:
            symbol = neighbour[0]
            coordinates = (neighbour[1],neighbour[2])
            if coordinates not in neighbour_symbols.keys():
                neighbour_symbols[coordinates] = {
                    'type': symbol,
                    'count': 1
                }
            else:
                neighbour_symbols[coordinates]['count'] += 1
    neighbours_set = set(neighbours)
    return neighbour_symbols

def get_gear_ratios(gears):
    gear_ratios = []
    for gear, part_numbers in gears.items():
        gear_ratios.append(part_numbers[0] * part_numbers[1])
    return gear_ratios

def process_matrix(matrix):
    part_numbers = []
    possible_gears = {}

    for x in range(len(matrix)):
        part_number_str = ''
        part_number_neighbours = []

        for y in range(len(matrix[x])):
            if matrix[x][y].isdigit():
                # Found digit, gathering neighbours
                part_number_str += matrix[x][y]
                neighbours = get_neighbours(matrix, x, y)
                part_number_neighbours.extend(neighbours)
            if not matrix[x][y].isdigit() and part_number_str != '':
                # Found dot, number is done.
                # Getting symbols from neighbours and searching for part numbers and gears.
                symbols = get_symbols(part_number_neighbours)
                if symbols != {}:
                    # Found part number, adding to list
                    part_numbers.append(int(part_number_str))
                    # Check symbols for possible gears
                    for key, value in symbols.items():
                        if key not in possible_gears.keys():
                            possible_gears[key] = [int(part_number_str)]
                        else:
                            possible_gears[key].append(int(part_number_str))
                part_number_str = ''
                part_number_neighbours = []

            if y == len(matrix[x])-1:
                # In case we have a number right at the end...
                # Getting symbols from neighbours and searching for gears.
                symbols = get_symbols(part_number_neighbours)
                if part_number_str != '' and symbols != {}:
                    # Found part number, adding to list
                    part_numbers.append(int(part_number_str))
                    # Check symbols for possible gears
                    for key, value in symbols.items():
                        if key not in possible_gears.keys():
                            possible_gears[key] = [int(part_number_str)]
                        else:
                            possible_gears[key].append(int(part_number_str))

    gears = {}
    for key,value in possible_gears.items():
        if len(value) == 2:
            gears[key] = value
            
    return part_numbers, gears

with open("day3.txt", 'r') as file:
    lines = file.readlines()

matrix = get_matrix_from_file_lines(lines)
part_numbers, gears = process_matrix(matrix)
print("Sum of part numbers: " + str(reduce((lambda x, y: x + y), part_numbers)))
print("Sum of gear ratios: " + str(reduce((lambda x, y: x + y), get_gear_ratios(gears))))
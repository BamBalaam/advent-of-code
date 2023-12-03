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
                neighbours.append(matrix[k][l])

    return neighbours

def check_neighbours_contain_symbols(neighbours):
    symbols_set = set(['*', '/', '@', '&', '$', '=', '#', '-', '+', '%'])
    neighbours_set = set(neighbours)
    return len(symbols_set.intersection(neighbours_set))


def check_neighbours_contain_gear(neighbours):
    symbols_set = set(['*', '/', '@', '&', '$', '=', '#', '-', '+', '%'])
    neighbours_set = set(neighbours)
    return len(symbols_set.intersection(neighbours_set))


def get_part_numbers_from_matrix(matrix):
    part_numbers = []

    for x in range(len(matrix)):
        part_number_str = ''
        part_number_neighbours = []

        for y in range(len(matrix[x])):
            if matrix[x][y].isdigit():
                part_number_str += matrix[x][y]
                neighbours = get_neighbours(matrix, x, y)
                part_number_neighbours.extend(neighbours)
            if not matrix[x][y].isdigit() and part_number_str != '':
                if check_neighbours_contain_symbols(part_number_neighbours):
                    part_numbers.append(int(part_number_str))
                part_number_str = ''
                part_number_neighbours = []

            if y == len(matrix[x])-1:
                # in case we have a number right at the end...
                if part_number_str != '' and check_neighbours_contain_symbols(part_number_neighbours):
                    part_numbers.append(int(part_number_str))
            
    return(part_numbers)

with open("day3.txt", 'r') as file:
    lines = file.readlines()

matrix = get_matrix_from_file_lines(lines)
part_numbers = get_part_numbers_from_matrix(matrix)
print(reduce((lambda x, y: x + y), part_numbers))
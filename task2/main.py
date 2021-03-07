import argparse
import os.path

def is_matrix_square(matrix):
    if len(matrix) < 1:
        return True
    l = len(matrix[0])
    if l != len(matrix):
        return False
    for sub_list in matrix:
        if l != len(sub_list):
            return False
    return True

def load_matrix(path):
    if path == None:
        return None
    if not os.path.exists(path):
        return None
    matrix = list()
    file = open(path, 'r')
    for line in file:
        row = [int(num) for num in line.split()]
        matrix.append(row)
    return matrix


def is_matrix_right(matrix):
    if(len(matrix) < 1):
        return True
    indent = 0
    i = 0
    j = 1
    di = 0
    dj = 1
    comparsion_elem = matrix[0][0]
    flag_sign = None
    exit_count = len(matrix) * len(matrix[0])
    while(exit_count>1):
        if matrix[i][j] - comparsion_elem != 0:
            if flag_sign == None:
                flag_sign = matrix[i][j] - comparsion_elem
        if flag_sign != None:
            if flag_sign * (matrix[i][j] - comparsion_elem) < 0:
                return False

        comparsion_elem = matrix[i][j]
        if dj > 0 and j == len(matrix) - indent-1:
            dj = 0
            di = 1
        if di > 0 and i == len(matrix) - indent-1:
            di = 0
            dj = -1
        if dj < 0 and j == indent:
            dj = 0
            di = -1
        if di < 0 and i == indent+1:
            di = 0
            dj = 1
            indent +=1
        i+=di
        j+=dj
        exit_count-=1
    return True

def main():
    parser = argparse.ArgumentParser('specify the path to the matrix')
    parser.add_argument('--p')
    args = parser.parse_args()
    path = args.p
    if load_matrix(path) == None:
        path = 'matrix_data.txt'
    if load_matrix(path) == None:
        print('Error: Specify the path to the matrix or type matrix into file with name is \'matrix_data.txt\'')
        return
    matrix = load_matrix(path)
    if not is_matrix_square(matrix):
        print('Error: The matrix must be square!')
        return
    if is_matrix_right(matrix):
        print('Matrix elements form an ordered sequence.')
    else:
        print('Matrix elements do not form an ordered sequence.')

if __name__ == '__main__':
    main()
 

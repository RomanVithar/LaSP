import argparse
import re


def create_args():
    cmd_parser = argparse.ArgumentParser(
        description='use the --p for point out path to file,' +
        'use --w, that point out number of symbol into line'
    )
    cmd_parser.add_argument('--p')
    cmd_parser.add_argument('--w')
    cmd_parser.add_argument('--o')
    args = cmd_parser.parse_args()
    return args


def get_path(args):
    if args.p == None:
        print("The file is not existed, program use own file")
        return 'task4/files/data.txt'
    return args.p


def get_width(args):
    if args.w == None:
        return 70
    return int(args.w)

def get_path_out(args):
    if args.o == None:
        print("The file is not existed, program use own file")
        return 'task4/files/output.txt'
    return args.o   


def read_from_file(path):
    with open(path, 'r') as file:
        data = file.read()
    return data


def write_into_file(str, path):
    with open(path, 'w') as file:
        file.write(str)


def len_to_space_left(str, space_start):
    count = 1
    while str[space_start - count] != ' ':
        count += 1
    return count


def fill_spaces(str, width):
    space_count = width - len(str)
    list_word = str.split()
    quantity_words = len(list_word)
    if quantity_words <= 1:
        return str
    in_every = space_count // (quantity_words - 1)
    last_word = space_count % (quantity_words - 1)
    outcome = ''
    for i in range(quantity_words-1):
        if i == quantity_words - last_word-1:
            in_every += 1
        outcome += list_word[i]+' '
        for j in range(in_every):
            outcome += ' '
    outcome += list_word[quantity_words-1]
    return outcome


def align_string(str, width):
    outcome = '      '
    space_count = 0
    start_line = 0
    indent = 6
    for space in re.finditer(r'\s', str):
        if space.group(0) == '\n' and space.start()+indent-start_line <= width:
            outcome += str[start_line:space.start()] + '\n'
            outcome += '      '
            indent = 6
            start_line = space.start()+1
        if space.start()+indent-start_line > width:
            space_count = len_to_space_left(str, space.start())
            outcome += fill_spaces(str[start_line:space.start() -
                                       space_count], width-indent) + '\n'
            start_line = space.start() - space_count + 1
            indent = 0
    return outcome


def main():
    args = create_args()
    path_input = get_path(args)
    width = get_width(args)
    path_out = get_path_out(args) 
    str = read_from_file(path_input)
    str = align_string(str, width)
    write_into_file(str, path_out)


if __name__ == '__main__':
    main()

import argparse
import re
from Splitter import Splitter
from Formater import Formater


def create_args():
    cmd_parser = argparse.ArgumentParser(
        description='use the --p for point out path to input file,' +
        'use --w, that point out number of symbol into line' +
        'use --o, that point out path to out file'
    )
    cmd_parser.add_argument('--p')
    cmd_parser.add_argument('--o')
    cmd_parser.add_argument('--w')
    args = cmd_parser.parse_args()
    return args


def get_path(args):
    if args.p == None:
        print("The file is not existed!")
        return None
    return args.p


def get_width(args):
    if args.w == None:
        return 70
    return int(args.w)

def get_path_out(args):
    if args.o == None:
        print("The output file is not existed, program use own file")
        return 'output.txt'
    return args.o


def read_from_file(path):
    with open(path, 'r') as file:
        data = file.read()
    return data

def align_string(func):
    def inner(str, path, width):
        outcome = ''
        for line in Formater(str, width):
            outcome += line + '\n'
        func(outcome, path)
    return inner

@align_string
def write_into_file(str, path):
    with open(path, 'w') as file:
        file.write(str)

# без регулярки метод выше, если слово больше чем ширина строки иправить.
# сделать ошибку при попытке загрузки фала из неоткуда и вывод в консоль при неуказании пути к файлу вывода
# прикрутить сюда декоратор
# декоратор сделать для обёртки текста который надо выровнять, то есть для считывания из файла
# лучше использовать декаратор с помощью "@" но дополнительно лучше и по-нормальному сделать
# можно использовать итератор для перебора слов и для перебора отдельных строк которые надо вставить
# избавиться от условных операторов в fill_spaces если при выполнении остальных пунктов останется необходимость 

def main():
    args = create_args()
    path_input = get_path(args)
    width = get_width(args)
    path_out = get_path_out(args)
    str = read_from_file(path_input)
    write_into_file(str, path_out, width)

if __name__ == '__main__':
    main()
















































# старый алгоритм который не пилит слова когда остаётся одно слово на строке и оно не вмещается

#def len_to_space_left(str, space_start):
#    count = 1
#    while str[space_start - count] != ' ':
#        count += 1
#    return count
#
#
#def fill_spaces(str, width):
#    space_count = width - len(str)
#    list_word = str.split()
#    quantity_words = len(list_word)
#    if quantity_words <= 1:
#        return str
#    in_every = space_count // (quantity_words - 1)
#    last_word = space_count % (quantity_words - 1)
#    outcome = ''
#    for i in range(quantity_words-1):
#        if i == quantity_words - last_word-1:
#            in_every += 1
#        outcome += list_word[i]+' '
#        for j in range(in_every):
#            outcome += ' '
#    outcome += list_word[quantity_words-1]
#    return outcome
#
#
#def align_string(str, width):
#    outcome = ' '
#    indent = 6
#    if width < 6:
#        outcome *= width
#        indent = width
#    else:
#        outcome *= 6
#    space_count = 0
#    start_line = 0
#    for space in re.finditer(r'\s', str):
#        if space.group(0) == '\n' and space.start()+indent-start_line <= width:
#            outcome += str[start_line:space.start()] + '\n'
#            outcome += '      '
#            indent = 6
#            start_line = space.start()+1
#        if space.start()+indent-start_line > width:
#            #if quantity_words <= 1:
#            #    return str
#            space_count = len_to_space_left(str, space.start())
#            if len(str[start_line:space.start() - space_count]):
#                temp = str[start_line:space.start() - space_count]
#                while len(temp) > width:
#                    outcome += temp[0:width] + '\n'
#                    temp = temp[width:len(temp)]
#                else:
#
#            outcome += fill_spaces(str[start_line:space.start() -
#                                       space_count], width-indent) + '\n'
#            start_line = space.start() - space_count + 1
#            indent = 0
#    return outcome

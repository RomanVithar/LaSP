import argparse


def task(fun_for_decoration):
    def inner_decor_1(list_num):
        def inner_decor_2(list_num, firstIndex, b):
            return fun_for_decoration(list_num, firstIndex, b)
        new_list = list()
        main_first = 0
        max_count = 0
        main_b = 0
        for i in range(len(list_num)):
            for j in range(i+1, len(list_num)):
                temp = inner_decor_2(list_num, i, list_num[j]-list_num[i])
                if temp > max_count:
                    max_count = temp
                    main_first = i
                    main_b = list_num[j]-list_num[i]
        return printer(list_num, main_first, main_b)
    return inner_decor_1    

def progression_count(list_num, firstIndex, b):
    current = list_num[firstIndex]
    count = 0
    for i in range(firstIndex, len(list_num)):
        if(list_num[i] == current):
            count += 1
            current += b
    return count


def printer(list_num, firstIndex, b):
    new_list = list()
    current = list_num[firstIndex]
    for i in range(firstIndex, len(list_num)):
        if(list_num[i] == current):
            new_list.append(list_num[i])
            current += b
    return new_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A tutorial of argparse!')
    parser.add_argument("--input")
    args = parser.parse_args()
    path = args.input
    list10 = list()
    with open(path, 'r') as f:
        for eachLine in f:
            for x in eachLine.strip().strip('[]').split(","):
                list10.append(int(x))
    fun_decor = task(progression_count)
    print(fun_decor(list10))

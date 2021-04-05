if __name__ == '__main__':
    path = 'file.txt'
    text = ''
    file = open(path, 'r')
    for line in file:
        text += line
    list = text.split('.')
    for i in range(len(list)):
        list[i] +='.'
    print(list)
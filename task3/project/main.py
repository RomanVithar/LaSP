import argparse
from pathlib import Path
from Triangle import Triangle
from Point import Point
from tkinter import *

def load_from_file(path):
    triangles = list()
    file_data = open(path, 'r')
    for line in file_data:
        list_coordinates = line.rstrip('\n').split(',')
        triangle = Triangle(Point((int)(list_coordinates[0]), (int)(list_coordinates[1])),
                            Point((int)(list_coordinates[2]), (int)(
                                list_coordinates[3])),
                            Point((int)(list_coordinates[4]), (int)(list_coordinates[5])))
        triangles.append(triangle)
    return triangles


def group_triangles(triangles):
    map = list()
    map.append(list())
    map[0].append(triangles[0])
    for i in range(1, len(triangles)):
        is_push_in_map = False
        for j in range(len(map)):
            # print(triangles[i].is_similar(map[j][0]))
            if triangles[i].is_similar(map[j][0]):
                map[j].append(triangles[i])
                is_push_in_map = True
                break
        if not is_push_in_map:
            temp_list = list()
            temp_list.append(triangles[i])
            map.append(temp_list)
    return map

def draw(ax,ay,bx,by,cx,cy, canvas,color):
    canvas.create_line(ax*40,ay*40,bx*40,by*40, width=3, fill=color)
    canvas.create_line(bx*40,by*40,cx*40,cy*40, width=3, fill=color)
    canvas.create_line(ax*40,ay*40,cx*40,cy*40, width=3, fill=color)
   
def main():
    parser = argparse.ArgumentParser(
        description='use the --p[path] for point out path to file')
    parser.add_argument("--p")
    args = parser.parse_args()
    if(args.p == None):
        print("The file is not existed, program use own file")
        path = 'data.txt'
    else:
        path = args.p
    triangles = load_from_file(path)
    map = group_triangles(triangles)
    #rendering
    root = Tk()
    canvas = Canvas(root, width=900, height=500)

    colors = ['black', 'yellow', 'green', 'grey', 'pink','red','orange']
    for i in range(len(map)):
        print('Triangles group {} is :'.format(i))
        for j in range(len(map[i])):
            draw(map[i][j].p1.x, map[i][j].p1.y,map[i][j].p2.x, map[i][j].p2.y,map[i][j].p3.x, map[i][j].p3.y, canvas,colors[i])
            print(map[i][j])
        print('===================')

    canvas.pack()
    root.mainloop()


if __name__ == '__main__':
    main()

import math


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def get_angles(self):
        parties_list = list()
        a = math.sqrt((self.p1.x - self.p2.x)**2 + (self.p1.y - self.p2.y)**2)
        b = math.sqrt((self.p2.x - self.p3.x)**2 + (self.p2.y - self.p3.y)**2)
        c = math.sqrt((self.p3.x - self.p1.x)**2 + (self.p3.y - self.p1.y)**2)
        parties_list.append(a) 
        parties_list.append(b) 
        parties_list.append(c) 
        return parties_list 

    def is_similar(self, triangle):
        this_list = self.get_angles()
        that_list = triangle.get_angles()
        this_list.sort()
        that_list.sort()
        k = round(this_list[0]/that_list[0], 5)
        return k == round(this_list[1]/that_list[1], 5) and k == round(this_list[2]/that_list[2], 5)

    def __str__(self):
        return 'p1 -> {}, p2 -> {}, p3 -> {}'.format(self.p1, self.p2, self.p3)

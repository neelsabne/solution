# Solution for the 1st Problem..... That is whether the point in polygon or not ? 

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def is_within_polygon(polygon, point):
    A = []
    B = []
    C = []  
    for i in range(len(polygon)):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % len(polygon)]
        
        # calculate A, B and C
        a = -(p2.y - p1.y)
        b = p2.x - p1.x
        c = -(a * p1.x + b * p1.y)

        A.append(a)
        B.append(b)
        C.append(c)

    D = []
    for i in range(len(A)):
        d = A[i] * point.x + B[i] * point.y + C[i]
        D.append(d)

    t1 = all(d >= 0 for d in D)
    t2 = all(d <= 0 for d in D)
    return t1 or t2

if __name__ == '__main__':
    polygon = [Point(1, 0), Point(8, 3), Point(8, 8), Point(1, 5)]
    p1 = Point(3, 5)
    print(is_within_polygon(polygon, p1)) # returns True
    polygonn = [Point(-3,2),Point(-2,-0.8),Point(0,1.2),Point(2.2,0),Point(2,4.5)]
    p2 = Point(0, 0)
    print(is_within_polygon(polygonn, p2)) # returns False

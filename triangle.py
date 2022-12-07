from draw import *
from convex_hull import *

def det(a, b):
    return a[0] * b[1] - a[1] * b[0]
def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    div = det(xdiff, ydiff)
    if div==0:
        return -1
    
    d = (det(*line1), det(*line2))
    x = det(d, xdiff)/div
    y = det(d, ydiff)/div
    return x,y

n=int(input("n = "))
#n=100
S=generate_random_set(n)
#S = [(10,20),(20,10),(40,30),(50,10),(60,10),(70,40),(80,20),(90,30),(100,10)]
print(S)

CH = convex_hull(S)
print(CH)

def triangle_area(p1,p2,p3):
    return abs((p2[0]-p1[0])(p3[1]-p1[1])-
                             (p3[0]-p1[0])(p2[1]-p1[1]))/2


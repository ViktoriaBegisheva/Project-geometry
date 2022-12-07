import random
from draw import *

def generate_random_set(n):
    S=[]
    for i in range(n):
        S.append((random.randint(-200,200),random.randint(-200,200)))
    return S

def coliniar(p1,p2,p3):
    a=((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**(1/2)
    b=((p3[0]-p2[0])**2+(p3[1]-p2[1])**2)**(1/2)
    c=((p1[0]-p3[0])**2+(p1[1]-p3[1])**2)**(1/2)
    return a+b==c or c+b==a or a+c==b

def find_q(S):
    p1=S[0]
    p2=S[1]
    p=0
    for i in range(2,len(S)):
        p3=S[i]
        if not coliniar(p1,p2,p3):
            p=1
            break
    if not p:
        return False
    x_q=(p1[0]+p2[0]+p3[0])/3
    y_q=(p1[1]+p2[1]+p3[1])/3
    draw_p((x_q,y_q),text="q",color="blue")
    return (x_q,y_q)

def rotate(p1,p2,p3):
  return (p2[0]-p1[0])*(p3[1]-p2[1])-(p2[1]-p1[1])*(p3[0]-p2[0])

def sort_by_q_(S):
    
    if len(S)<=1:
        return S
    
    left = []
    center = []
    right = []
    p=S[0]
    dk=abs(q[0]-p[0])+abs(q[1]-p[1])
    for j in range(0,len(S)):
        
        dj=abs(q[0]-S[j][0])+abs(q[1]-S[j][1])
        x = rotate (q,p,S[j])
        if   x<0: left.append(S[j])
        elif x>0: right.append(S[j])
        else:
            if dj>dk: left.append(S[j])
            elif dj<dk: right.append(S[j])
            else: center.append(S[j])
    return (sort_by_q_(left)+center+sort_by_q_(right))

def convex_hull(S):
    
    set_speed(20)
    draw_points(S)
    
    n=len(S)
    
    # find q
    global q
    q=find_q(S)
    
    # check all points on one line
    if not q:
        return S
    
    # sort by polar algel ((0,0) -> q)
    K=sort_by_q_(S)
    draw_lines_qsort(K,q)
    
    # find start point (with min x coord)
    min_ind=0
    for i in range(len(K)):
        if K[i]<K[min_ind]:
            min_ind=i
    K=K[min_ind:]+K[:min_ind]
    CH=[K[0],K[0]]
    
    set_speed(5)
    for i in range(1,n+1):
        while (rotate(CH[-2],CH[-1],K[i%n])<0): 
            draw_line(CH[-1],CH[-2],color="white")
            del CH[-1]
        draw_line(CH[-1],K[i%n],color="red")
        CH.append(K[i%n])
    return CH


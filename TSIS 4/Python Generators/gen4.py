import math
def Squares(a, b):
    while a <= b:
            yield a*a
            a+=1
r = int(input())
j = int(input())
for i in Squares(r, j):
    print(i)

    
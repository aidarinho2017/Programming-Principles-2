def Gen(n):
    num = 0
    while num <= n:
        yield num
        num += 2
a = int(input())
for i in Gen(a):
    print(i)
    
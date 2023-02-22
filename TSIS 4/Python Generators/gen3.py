def Gen(n):
    num = 0
    while num <= n:
        num += 12
        yield num
        
a = int(input())
for i in Gen(a):
    print(i)
    
def gen(n):
    num = 1
    while num<=n:
        yield num**2
        num+=1
a = int(input())
for i in gen(a):
    print(i)

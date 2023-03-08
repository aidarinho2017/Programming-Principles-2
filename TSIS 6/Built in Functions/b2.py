def cnt(x):
    a = 0
    b = 0
    for i in x:
        if i.isupper():
            a+=1
        elif i.islower():
            b+=1
    return [a, b]
print(cnt("Hello QWorld"))
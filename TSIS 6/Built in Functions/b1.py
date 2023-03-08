def multiply(numbers):
    t = 1
    for i in numbers:
        t*=i
    return t
print(multiply([1, 2, 3, 4, 5, 6, 7, 8]))
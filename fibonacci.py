for i in range(50):
    if i == 0:
        print(0)
    elif i == 1:
        print(1)
    else:
        a, b = 0, 1
        for _ in range(2, i + 1):
            a, b = b, a + b
        print(b)
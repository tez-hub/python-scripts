# The triangles should appear twice

t = 2
for r in range(t):
    # Increasing triangle
    # n is the no of rows
    n = 5
    for i in range(n):
        # Increase the number of rows
        for j in range(i+1):
            print('*', end=' ')

        print()

    # Decreasing triangle
    # n is the no of rows
    n = 5
    for i in range(n):
        for j in range(i-1, n):
            print('*', end=' ')

        print()

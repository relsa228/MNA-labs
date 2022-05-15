def euler_method(function, n, h, x, y):
    for i in range(n):
        y += h * function(x, y)
        x += h
    return x, y

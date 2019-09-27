def sign(x):
    return (x > 0) - (x < 0)


def sum(m, n):
    sum = m
    for _ in range(abs(n)):
        sum += sign(n)
    return sum


def divide(m, n):

    assert n != 0

    s_m = sign(m)
    s_n = sign(n)

    m = abs(m)
    n = abs(n)

    result = 0

    while (m-n) > 0:
        result += 1
        m = m-n

    return s_m * s_n * result


def subtract(m, n):
    return sum(m, -n)


def multiply(m, n):
    result = 0

    for _ in range(abs(n)):
        result += abs(m)

    return sign(n) * sign(m) * result

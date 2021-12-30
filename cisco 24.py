''' Some simple functions: evaluating a triangle's area ,We can also evaluate a triangle's area. Heron's formula will be handy here:s = (a + b + c) / 2
A = the square root of s(s - a)(s - b)(s - c)
We're going use the exponentiation operator to find the square root - it may seem strange, but it works:
The square root of x = x to the power of 1/2 .This is the resulting code:'''
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)


print(area_of_triangle(1., 1., 2. ** .5))


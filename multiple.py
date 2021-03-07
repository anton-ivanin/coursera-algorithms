def multiple(m1, m2):
    str_m1 = str(m1)
    str_m2 = str(m2)
    n = max(len(str_m1), len(str_m2))
    if n > 1:
        a = m1 // pow(10, int(n / 2))
        b = m1 % pow(10, int(n / 2))
        c = m2 // pow(10, int(n / 2))
        d = m2 % pow(10, int(n / 2))
        return pow(10, int(n)) * multiple(a, c) + multiple(b, d) + pow(10, int(n / 2)) * (
                    multiple(a, d) + multiple(b, c))
    else:
        return m1 * m2


x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

print(multiple(x, y) == x * y)

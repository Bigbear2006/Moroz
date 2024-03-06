a = 7
b = 2
c = 8


def triangle_perimetr(_a=a, _b=b, _c=c):
    return _a + _b + _c


def triangle_area(_a=a, _b=b, _c=c):
    p = (_a + _b + _c) / 2
    return (p * (p - _a) * (p - _b) * (p - _c)) ** 0.5

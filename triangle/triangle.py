def validate(f):
    def wrapper(sides):
        a, b, c = sorted(sides)
        return 0 not in sides and a + b >= c and f(sides)

    return wrapper


@validate
def equilateral(sides):
    return len(set(sides)) == 1


@validate
def isosceles(sides):
    return len(set(sides)) in [1, 2]


@validate
def scalene(sides):
    return len(set(sides)) == 3

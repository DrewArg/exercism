def equilateral(sides):
    result = check_rules(sides)

    if not result:
        return False
    else:
        if sides[0] == sides[1] and sides[0] == sides[2]:
            return True
        else:
            return False


def isosceles(sides):
    result = check_rules(sides)

    if not result:
        return False
    else:
        if sides[0] == sides[1]:
            return True
        elif sides[0] == sides[2]:
            return True
        elif sides[1] == sides[2]:
            return True
        else:
            return False


def scalene(sides):
    result = check_rules(sides)

    if not result:
        return False
    else:
        if sides[0] == sides[1]:
            return False
        elif sides[1] == sides[2]:
            return False
        elif sides[0] == sides[2]:
            return False
        else:
            return True


def check_rules(sides):

    if len(sides) == 3:
        if sides[0] != 0 and sides[1] != 0 and sides[2] != 0:
            return inequality_check(sides)
        else:
            return False
    else:
        return False

def inequality_check(sides):
    bigger_side = max(sides)
  
    other_sides_sum = 0

    for x in range(0,len(sides)):
        if x !=  sides.index(bigger_side):
            other_sides_sum += sides[x]

    if other_sides_sum < bigger_side:
        return False
    else:
        return True

print(scalene([5,4,6]))
def is_armstrong_number(number):

    number = str(number)
    digits = len(number)

    result = 0

    for digit in number:
        result += int(digit) ** digits

    if result == int(number):
        return True
    else:
        return False 

print(is_armstrong_number(154))
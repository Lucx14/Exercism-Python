def is_armstrong_number(number):
    digits = [int(i) for i in str(number)]
    exp = len(digits)
    return sum(d ** exp for d in digits) == int(number)

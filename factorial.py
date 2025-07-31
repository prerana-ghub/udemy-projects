def calculate_factorial(number):
    if number < 0:
        return "Factorial not defined for negative numbers"
    if number == 0 or number == 1:
        return 1
    return number * calculate_factorial(number - 1)

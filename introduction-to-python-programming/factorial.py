def calculate_factorial(num):
    if num < 0:
        return "Factorial not defined for negative numbers"
    if num == 0 or num == 1:
        return 1
    return num * calculate_factorial(num - 1)

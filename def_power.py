def power(num1, num2):
    result = 1
    if num2 < 0:
        for x in range(-1 * num2):
            result = result * (1/num1)
    else:
        for x in range(0, num2):
            result = result * num1
    return result


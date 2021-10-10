def result(num):
    if num % 3 == 0:
        return "fizz"
    if num % 5 == 0:
        return "buzz"
    else:
        return str(num)

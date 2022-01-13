# Ryan Lugo: RJL 1/13/22

def sum_nums(num1,num2):

    value = num1
    numbers_to_add = []

    if num1 == num2:
        value = num1

    while True:
        if not num1 == value:
            if num2 + 1 > value:
                numbers_to_add.append(value)
                value += 1
                print(value)
            else:
                break
        else:
            numbers_to_add.append(value)
            value += 1

    value = 0

    for i,v in enumerate(numbers_to_add):
        value += v

    return value

print(sum_nums(2,5))
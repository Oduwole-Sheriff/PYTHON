def find_max():
    numbers = [10, 22, 1, 33, 7]
    total = numbers[0]

    for number in numbers:
        if number > total:
            total = number
    print(total)
print(find_max())

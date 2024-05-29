def fizzbuzz(value):
    if value % 3 == 0 and value % 5 == 0:
        return "fizzbuzz"
    elif value % 3 == 0:
        return "fizz"
    elif value % 5 == 0:
        return "buzz"
    else:
        return value


def main():
    for value in range(1, 101):
        print(fizzbuzz(value))


if __name__ == '__main__':
    main()

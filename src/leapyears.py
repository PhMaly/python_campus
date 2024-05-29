def leapyears(value):
    if value % 400 == 0:
        return "Are Leap years"
    elif value % 100 == 0 and value % 400 != 0:
        return "Not Leap years"
    elif value % 4 == 0 and value % 100 != 0:
        return "Are Leap years"
    elif value % 4 != 0:
        return "Not Leap years"


def main():
    value = int(input("Saisir une année :"))
    print(leapyears(value))


if __name__ == '__main__':
    main()

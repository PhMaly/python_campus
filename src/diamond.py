def create_diamond(letter):
    if letter == "B":
        return """\
 A
B B
 A"""

    if letter == "C":
        return """\
  A
 B B
C   C
 B B
  A"""


# def value_of(letter):
#     return (ord(letter) - (ord("A")) + 1)


def main():
    print(create_diamond("C"))


if __name__ == '__main__':
    main()

'''
Reverse a string using generator
'''


def main():
    str_in = get_str()
    for char in rev(str_in):
        print(char, end='')


def get_str():
    return input('Enter string to be reversed:').strip()


def rev(str_in):
    for i in range(len(str_in) - 1, -1, -1):
        yield str_in[i]


main()

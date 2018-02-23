'''
sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
'''

# ord() -- gives you the numeric value of the character in whatever encoding it's in,
# chr(c) --> to find character given ascii


def so(x):
    # Increase the priority by adding
    assci = ord(x)
    if assci > 64 and assci < 91:
        assci += 35
    elif assci > 47 and assci < 58:
        assci += 120
    return assci


s1 = input().strip()
s3 = sorted(s1, key=so)

# ~ to ''.join(s3)
print(*s3, sep='')

# same in one liners! 4 ways!
# print(*sorted(input(), key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')
#
# print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')
#
# order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
# print(*sorted(input(), key=order.index), sep='')
#
# import string
# print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')


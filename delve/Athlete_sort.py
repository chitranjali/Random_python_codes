'''
given a spreadsheet that contains a list of  athletes and their details
(such as age, height, weight and so on).You are required to sort the data based
on the th attribute and print the final resulting table
  '''

# sort() --> in place, sorted --> new list
athletes, attributes = map(int, input('Enter no of Athletes and '
                                      'attributes').split())

ath_att = []
# O(2n) --
for _ in range(athletes):  # athletes is gen obj
    att = [*map(int, input().split())]
    ath_att.append(att)

k = int(input().strip())

# lambda equivalent: lambda x:x[k]
# def k_ele(item):
# return item[k] --k?
sorted_list = sorted(ath_att, key=lambda x: x[k])

# print "\n".join(map(lambda x: " ".join(map(str, x)), sorted(lst,
# key = lambda x: x[k]))) # equivalent to below
for item in sorted_list:
    print(' '.join(map(str, item)))

#     for i in item:
#         print(i, end =' ')
#     print()

'''
Given a space separated list of integers,
If all the integers are positive, then you need to
check if any integer is a palindromic integer.
Print True if all the conditions of the problem statement
are satisfied. Otherwise, print False.
'''
no_of_ele = int(input().strip())
nums = input().strip().split()

pos = all([int(x) > 0 for x in nums])
pal = any([ x[:] == x[-1::-1] for x in nums])
print(pal and pos)


'''
 Fibonacci sequence upto n using generator
'''

def generate_fibonacci(n):
    i, j = 0, 1
    for _ in range(n):
        yield i+j
        i, j = j, i + j


n = input("How many fibonacci numbers you want?")
fi_obj = generate_fibonacci(int(n))  # Gen_object

for num in fi_obj:
    print('{},'.format(num), end =' ')

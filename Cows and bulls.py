import random
def gen_number():
    return random.randint(1000,9999)

def check_cows_and_bulls(guess,g_num):
    bulls,cows = 0,0
    if guess == g_num:
        print("you guessed it right!")
    else:
        for index, value  in enumerate(guess):
            if value in g_num:
                if value == g_num[index]:
                    cows = cows + 1
                else:
                    bulls = bulls + 1
        return bulls,cows

g_num = str(gen_number())
guess = ' '
att = 0
print(g_num)
while guess != g_num and guess != 'exit':
    guess = input("Enter your four digit number guess")
    att = att + 1
    print('bulls and cows are {}'.format(check_cows_and_bulls(guess,g_num)))
print(g_num)
print(att)

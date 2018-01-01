import random
def gen_number():
    return random.randint(1000,9999)

def check_cows_and_bulls(guess,g_num):
    bulls,cows,ind = 0,0,0
    if guess == g_num:
        print("you guessed it right!")
    else:
        for x in guess:
            if x in g_num:
                if x == g_num[ind]:
                    cows = cows + 1
                else:
                    bulls = bulls + 1
            ind = ind + 1
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

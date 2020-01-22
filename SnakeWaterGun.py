"""
This is Snake Water Gun game
There are three conditions:
i) if water and snake are together snake will drink all water
ii) if snake and Gun are together fun will kill the snake
iii) if gun and water are together gun will sink in water

Give input same as choice given in temp
"""
import random as rd

temp = ['Snake', 'Water', 'Gun']

a = rd.choice(temp)

print(temp)
inp = str(input("Choose one of above: "))

val = False

if inp == 'Snake' or inp == 'Gun' or inp == 'Water':
    val = True
else:
    print("You entered unexpected value")

while val:
    if inp == 'Snake' and a == 'Water':
        print("You Won : Snake drank the Water")
        break
    elif inp == 'Snake' and a == 'Gun':
        print("You Lose : Gun killed the Snake")
        break
    elif inp == 'Water' and a == 'snake':
        print("You Lose : Snake drank the Water")
        break
    elif inp =='Water' and a == 'Gun':
        print("You Won : Gun drowned in Water")
        break
    elif inp == 'Gun' and a =='Water':
        print("You Lose : Gun drowned in Water")
        break
    elif inp == 'Gun' and a =='Snake':
        print("You Won : Gun killed the Snake")
        break
    else:
        print("Draw")

print("System has choosen ", a)


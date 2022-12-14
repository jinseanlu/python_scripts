#carrot clogs gun. rabbit eats carrot. gun shoots rabbit

import random

choice = ['carrot', 'rabbit', 'gun']
x = random.randint(0,2)
y = random.randint(0,2)
outcomex = choice[x]
outcomey = choice[y]
print(outcomex)
print(outcomey)
if x == 0 and y == 2:
    print("carrot1 wins!")
   
if x == 2 and y == 1:
    print("gun1 wins!")
if x == 1 and y == 0:
    print("The rabbit1 eats a juicy carrot")
if y == 0 and x == 2:
    print("carrot2 wins!")
if y == 2 and x == 1:
    print("gun2 wins!")
if y == 1 and x == 0:
    print("The rabbit2 eats a even juicier carrot!")
if y == x:
    print("No one wins!")

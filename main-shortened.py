# We all have played snake, water gun game in our childhood. If you haven’t, google the
# rules of this game and write a python program capable of playing this game with the
# user.
'''
1 for snake
-1 for water 
0 for gun

'''
import random
print()
print()
print("## Snake , Water , Gun game.")
print("Hello everyone, Welcome to the game..")
print("Rules to consider")
print()
print("Snake drinks water  --> Snake wins.")
print("Gun sinks in water  --> Water wins.")
print("Gun shoots the snake--> Gun wins.")
print()

youstr =(input("Enter your choice snake , water, gun(s,w, g).."))
computer = random.choice([1, 0, -1])
dict= { "s" : 1 , "w":-1 , "g" : 0}
reversedict={1:"Snake", -1:"Water" , 0:"Gun"}

you = dict[youstr]

print(f"You chose--{reversedict[you]} \nComputer chose-- {reversedict[computer]}")

if (computer-you)==-1 or (computer - you)==2:
    print("You lose..")
else:
    print("you win")

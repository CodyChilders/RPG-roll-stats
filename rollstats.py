#Mars RPG stat roller
#rolls 3d8, takes the best 2 for each stat
#runs for as many stats as the user inputs
import random
diceSize = 8
numToRoll = int(input("How many stats do you want to roll? "))
print("Your rolls are...")
for i in range(0, numToRoll):
    sum = 0
    min = 99999999
    for j in range(0, 3):
        val = random.randint(1, diceSize)
        sum += val
        if val < min:
            min = val
    sum -= min
    print(sum)

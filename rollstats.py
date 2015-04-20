#Mars RPG stat roller
#rolls 3d8, takes the best 2 for each stat
#runs for as many stats as the user inputs
import random
#constants
diceSize = 8
diceCount = 3
#get input
numToRoll = int(input("How many stats do you want to roll? "))
playersToRoll = int(input("How many players do you want to roll for? "))
#run calculations
for player in range(0, playersToRoll):
    print("Your rolls for player", player + 1, "are...")
    for i in range(0, numToRoll):
        sum = 0
        min = 99999999
        #this loop just adds all the rolls together, but records which number was smallest
        #after it runs, it subtracts that from the sum, which effectively is picking the best of the rolls
        for j in range(0, diceCount):
            val = random.randint(1, diceSize)
            sum += val
            if val < min:
                min = val
        sum -= min
        print(sum)
    print("", end="\n")
input("Press enter to exit\n")

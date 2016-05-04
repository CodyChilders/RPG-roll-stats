#Mars RPG stat roller
#rolls 3d8, takes the best 2 for each stat
#runs for as many stats as the user inputs
from random import randint as rand

#constants
diceSize = 6 #setting this to 8 makes it a d8.  It does not necessarily have to be a platonic solid number
diceCount = 4 #how many dice are rolled.  The system will take the best of this number - 1 of the rolls 

class StatBlock:
    def __init__(self):
        self.stats = []

    def AddStat(self, newStat):
        self.stats.append(newStat)

    def GetSum(self):
        return sum(self.stats)

    def PrintStats(self):
        for i in self.stats:
            print(i)

def getInt(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val <= 0:
                print("Please enter a positive integer")
            elif val > 100:
                print("Please use reasonable numbers that are <100")
            else:
                return val
        except ValueError:
            print("Please enter a positive integer")

def printStatBlockList(statBlockList):
    player = 1
    for s in statBlockList:
        print("Your rolls for player", player, "are...")
        s.PrintStats()
        print("The sum of the stats is", s.GetSum(), end="\n\n")
        player += 1

#implements bubble sort, because I'm lazy
def sortStats(statBlockList):
    for passnum in range(len(statBlockList) - 1, 0, -1):
        for i in range(passnum):
            if statBlockList[i].GetSum() > statBlockList[i+1].GetSum():
                temp = statBlockList[i]
                statBlockList[i] = statBlockList[i+1]
                statBlockList[i+1] = temp

def main():
    #setup
    allStatBlocks = []
    #get input
    numToRoll = getInt("How many stats do you want to roll? ")
    playersToRoll = getInt("How many players do you want to roll for? ")
    #run calculations
    for player in range(0, playersToRoll):
        newStatBlock = StatBlock()
        for i in range(0, numToRoll):
            sum = 0
            min = 99999999
            #this loop just adds all the rolls together, but records which number was smallest
            #after it runs, it subtracts that from the sum, which effectively is picking the best of the rolls
            for j in range(0, diceCount):
                val = rand(1, diceSize)
                sum += val
                if val < min:
                    min = val
            sum -= min
            newStatBlock.AddStat(sum)
        allStatBlocks.append(newStatBlock)
    sortStats(allStatBlocks)
    printStatBlockList(allStatBlocks)
    input("Press enter to exit\n")

main()

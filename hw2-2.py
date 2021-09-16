# Author: MOG 9/16/21

freeThrows = 1
twoPts = 0
threePts = 0
totalPts = (freeThrows) + (twoPts * 2) + (threePts * 3)

s = ""
if(totalPts != 1): s = "s"

print("The player scored {} point{} in the game.".format(totalPts, s))
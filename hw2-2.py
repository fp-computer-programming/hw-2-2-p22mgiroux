# Author: MOG 9/16/21

free_Throws = 1
two_Pts = 4
three_Pts = 7
total_Pts = (free_Throws) + (two_Pts * 2) + (three_Pts * 3)

s = ""
if(total_Pts != 1): s = "s"

print("The player scored {} point{} in the game.".format(total_Pts, s))
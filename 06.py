# Array (list) of colors
colors = [["pink", 0xFF1493], ["blue", 0x0000FF], ["red", 0xFF0000], ["green", 0x00FF00]]

# My favorite color
favorite = "blue"

# Print only favorite color number
for color in colors:
	# Check if color is my fovorite one
	if color[0] == favorite:
		print "I like x:{0:x}".format(color[1])
		
# Exercise
# 1. If lolor is not favorite print message like this (if-else statement]
# Don't like pink color
# I like x:ff
# Don't like red color
# Don't like green color
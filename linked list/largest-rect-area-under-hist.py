heights = []
positions = []
hist = [6,2,5,4,5,1,6]
max_height = 0

for idx, height in enumerate(hist):
	if len(heights) == 0 or heights[-1] < height:
		heights.append(height)
		positions.append(idx)
	elif (heights[-1] > height):
		# stack is not empty and tos is smaller than the current element
		while(len(heights) != 0 and heights[-1] > height):
			height_tos = heights.pop(-1)
			pos_tos = positions.pop(-1)
			width = height_tos*(idx-pos_tos)
			if width>max_height:
				max_height = width
		heights.append(height)
		positions.append(pos_tos) # be careful here

print heights
print positions
print max_height
# now do what?
while len(heights) !=0:
	height_tos = heights.pop(-1)
	pos_tos = positions.pop(-1)
	width = height_tos*(idx-pos_tos)
	if width>max_height:
		max_height = width

print max_height

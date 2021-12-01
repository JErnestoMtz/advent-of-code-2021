with open("input_1.txt") as f:
	depths = [int(line.strip()) for line in f]
	l = len(depths)
	count = 0 
	# second part
	#depths = [(depths[i]+depths[i+1]+depths[i+2]) for i in range(0,l-2)]
	for i in range(1,len(depths)):
		if depths[i] - depths[i-1] > 0:
			count += 1
	print(count)
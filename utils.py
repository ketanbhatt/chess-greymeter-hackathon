def calculate_pos(y,o):
	y1, y2 = map(int,y.split('|'))
	o1, o2 = map(int,o.split('|'))
	return y1-1, y2-1, o1-1, o2-1
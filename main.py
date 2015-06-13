from flask import Flask, jsonify, request 
import random
app = Flask(__name__)

board = [[0 for i in xrange(15)] for i in xrange(15)]
data = { }




#################################
#############Functions##############
#################################

def calculate_pos(pos):
	x, y = map(int,pos.split('|'))
	return x-1, y-1

def set_visited(x,y):
	board[x][y] = 1

def calculate_danger(ox, oy):
	danger = []
	danger.append([ox-1,oy])
	danger.append([ox-1,oy+1])
	danger.append([ox,oy+1])
	danger.append([ox+1,oy+1])
	danger.append([ox+1,oy])
	danger.append([ox+1,oy-1])
	danger.append([ox,oy-1])
	danger.append([ox-1,oy-1])

	for i in range(data["grid"]):
		for j in range(data["grid"]):
			if(board[i][j] == 1):
				danger.append([i,j])

	return danger

def calculate_available(yx, yy):
	available = []
	available.append([yx-1,yy])
	available.append([yx-1,yy+1])
	available.append([yx,yy+1])
	available.append([yx+1,yy+1])
	available.append([yx+1,yy])
	available.append([yx+1,yy-1])
	available.append([yx,yy-1])
	available.append([yx-1,yy-1])

	avail = available[:]
	for temp in available:
		i, j = temp[0], temp[1]
		if(i==-1 or i==data["grid"] or j==-1 or j==data["grid"]):
			avail.remove(temp)

	return avail

def  calculate_move(ox, oy):
	danger = calculate_danger(ox, oy)
	available = calculate_available(data["currX"],data["currY"])
	allowed = []

	for possible in available:
		if possible not in danger:
			allowed.append(possible)

	if [ox, oy] in allowed:
		move = [ox, oy]
	else:
		temp = random.randint(0,len(allowed)-1)
		move = allowed[temp]

	return move

def print_board():
	for i in range(data["grid"]):
		for j in range(data["grid"]):
			print board[i][j],
		print "\n"
	



#################################
#############Routes################
#################################

@app.route('/ping')
def ping():
	return jsonify({'ok': 'true'})

@app.route('/start')
def start():
	yx, yy = calculate_pos(request.args.get('y'))
	ox, oy = calculate_pos(request.args.get('o'))
	data["grid"] = int(request.args.get('g'))
	data["currX"] = yx
	data["currY"] = yy

	set_visited(yx, yy)
	set_visited(ox, oy)

	return jsonify({'ok': 'true'})

@app.route('/play')
def play():
	ox, oy = calculate_pos(request.args.get('m'))

	move = calculate_move(ox, oy)
	x, y = move[0], move[1]
	data["currX"] = x
	data["currY"] = y
	board[ox][oy] = 7
	board[x][y] = 5

	print_board()
	set_visited(x, y)
	set_visited(ox, oy)
	response = str(x+1) + '|' + str(y+1)
	return jsonify({'m': response})

if __name__ == '__main__':
	app.run(debug=True)

from flask import Flask, jsonify, request 
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

	print danger

def allowed_moves(ox, oy):
	calculate_danger(ox, oy)





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
	#move = Calculate_move()	
	x, y = calculate_pos(request.args.get('m'))
	set_visited(x, y)

	allowed_moves(x, y)

	response = str(x) + '|' + str(y)
	return jsonify({'m': response})

if __name__ == '__main__':
	app.run(debug=True)

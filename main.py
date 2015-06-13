from utils import *
from flask import Flask, jsonify, request 
app = Flask(__name__)

board = [[0 for i in xrange(15)] for i in xrange(15)]
data = { }

@app.route('/ping')
def ping():
	return jsonify({'ok': 'true'})

@app.route('/start')
def start():
	y1, y2, o1, o2 = calculate_pos(request.args.get('y'), request.args.get('o'))
	data["grid"] = int(request.args.get('g'))
	board[y1][y2] = 1
	board[o1][o2] = 1
	print board
	return jsonify({'ok': 'true'})

@app.route('/play')
def play():
	#move = Calculate_move()	
	x, y = map(int,request.args.get('m').split('|'))
	response = str(x) + '|' + str(y)
	return jsonify({'m': response})

if __name__ == '__main__':
	app.run(debug=True)
from flask import Flask, jsonify, request 
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Chess Bot'

@app.route('/ping')
def ping():
	return jsonify({'ok': 'true'})

@app.route('/start')
def start():
	return jsonify({'ok': 'true'})

@app.route('/play')
def play():
	return jsonify({'m': 'P'})

if __name__ == '__main__':
	app.run(debug=True)
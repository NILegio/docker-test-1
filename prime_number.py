from flask import Flask, jsonify
from random import choice

app = Flask(__name__)

print("Start generate prime list")

primelist = []

for i in range(2, 500):
    for x in primelist:
        if i % x == 0: break
    else: primelist.append(i)

print("End generate prime list")


@app.route('/ping')
def index():
    return "PONG"


@app.route('/number')
def number():
    return jsonify(choice(primelist))


if __name__ == '__main__':
    app.run(debug=False, port=8080)

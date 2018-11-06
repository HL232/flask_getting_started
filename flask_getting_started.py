from flask import Flask, jsonify, request
import math
app = Flask(__name__)


@app.route("/name", methods=["GET"])
def name():
    output = {"name": "Howard"}
    return jsonify(output)


@app.route("/hello/<name>", methods=["GET"])
def hello_name(name):
    output = {
             "message": "Hello there, {}".format(name)
             }
    return jsonify(output)


def distance_input(list):
    point_a = list[0]
    point_b = list[1]
    output = math.sqrt((point_a[0]-point_b[0])**2 + (point_a[1]-point_b[1])**2)
    return output


@app.route("/distance", methods=["POST"])
def distance():
    output = {
             "distance": distance_input(([2, 4], [5, 6])),
             "a": [2, 4],
             "b": [5, 6]
            }
    return jsonify(output)


if __name__ == "__main__":
    app.run(host = "127.0.0.1")

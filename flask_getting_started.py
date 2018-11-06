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
    r = request.get_json()
    print(r)
    output = {
             "distance": distance_input((r["a"], r["b"])),
             "a": r["a"],
             "b": r["b"]
            }
    return jsonify(output)


if __name__ == "__main__":
    app.run(host = "127.0.0.1")

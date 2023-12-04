from flask import Flask, jsonify, request
import json
import http_codes

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route("/")
def welcome():

    return jsonify({"message": "Bem vindo à API"}), http_codes.OK

@app.get("/switchboards/")
@app.get("/switchboards/<id>/")
def switchboards(id = None):

    file = open('switchboards.json')

    switchboards = json.load(file)

    if id:

        for switchboard in switchboards:

            if switchboard["id"] == int(id):

                return jsonify(switchboard), http_codes.OK
            
        return jsonify({"message": "NOT FOUND"}), http_codes.NOT_FOUND

    else:

        if switchboards:

            return jsonify(switchboards), http_codes.OK

        return jsonify({"message": "NOT FOUND"}), http_codes.NOT_FOUND

if __name__ == "__main__":
    app.run(debug=True)
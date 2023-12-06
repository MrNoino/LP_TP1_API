# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, send_file, json
import json, mimetypes
import http_codes

app = Flask(__name__)

app.json.ensure_ascii = False

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

@app.get("/blueprints/<filename>/")
def blueprints(filename):

    full_path = "./blueprints/" + filename

    mime_type = mimetypes.guess_type(full_path)[0]

    print(mime_type)

    return send_file(full_path, mimetype= mime_type), http_codes.OK

if __name__ == "__main__":
    app.run(debug=True)
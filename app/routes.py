from flask import render_template, flash, redirect, url_for
from app import app
import json

@app.route('/search', methods=['GET'])
def search():
    return json.dumps("ping")
    # data = request.args.get("name")
    # output = select_all_items(c, data)
    # return json.dumps(output)


@app.route('/insert', methods=['POST'])
def insert():
    return
    # content = request.json
    # name = content['name']
    # body = content['body']
    # insert_db(c, name, body)
    # return "Successful"
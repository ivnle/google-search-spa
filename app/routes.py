from flask import render_template, flash, redirect, url_for, jsonify
from app import app
from app.models import Post, PostSchema


@app.route('/search', methods=['GET'])
def search():
    post = Post.query.all()
    output = PostSchema(many=True).dump(post).data
    return jsonify(output)


    # return json.dumps([{"name": "thundername", "body": "thunder body"},
    #                    {"name": "andreaname", "body": "andrea body"},
    #                    {"name": "yaya", "body": "yayo"}])

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
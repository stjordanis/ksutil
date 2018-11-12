#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from flask import Flask, jsonify, render_template, request
from scripts.answer import get_answer
from scripts.cat_facts import get_cat_facts

app = Flask(__name__)
 
# default page 
@app.route("/", methods=['GET', 'POST'])
def run_index(): # this function name can be arbitrary.
    if request.method == "POST":
        food = request.form["food_submitted"]
        return "Oh, your favorite food is " + get_answer(food) + "!"
    return render_template("index.html", header="Minimal demo for NLP.")

# run script in backend
@app.route("/scripts/cat_facts", methods=['GET', 'POST'])
def run_cat_facts(): # this function name can be arbitrary.
    if request.method == "GET":
        resp = get_cat_facts()
        text = resp["text"]
        return jsonify(result = text)
    return render_template("index.html", header="HEADER!")

if __name__ == '__main__':
    app.run(host='0.0.0.0')

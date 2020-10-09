from datetime import datetime
from flask import Flask, render_template, jsonify
from . import app
import json

@app.route("/")
def idp():
    return jsonify(
        {
            "providers": ["Dev2TestObject6666.com","Dev2TestObject7777.com","Dev2TestObject8888.com","Dev2TestObject9999.com","Dev2TestObject1000.com"],
        })

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

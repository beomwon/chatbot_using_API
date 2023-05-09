# main.py
#-*- coding:utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
import chatbot

app = Flask(__name__)
board = []
 
@app.route('/')
def index():
    return render_template('main.html', rows=board, qnas=chatbot.src)

@app.route('/question',methods=["POST"])
def question():
    if request.method == "POST":
        board.append([request.form["context"], chatbot.action(request.form["context"])])
        return redirect(url_for("index"))
    else:
        return render_template("main.html", rows=board, qnas=chatbot.src)
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8888)
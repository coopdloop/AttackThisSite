from flask import Flask, render_template, request, send_from_directory, json, make_response
import os
import sys
app = Flask(__name__)

@app.route('/')
@app.route('/home', methods = ['GET','POST'])
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0' ,port=1337)
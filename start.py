from flask import Flask, render_template, request, send_from_directory, json, make_response
import os
import sys
import mysql.connector
app = Flask(__name__)

@app.route('/')
@app.route('/home', methods = ['GET','POST'])
def home():
    if request.args.get('fname') and request.args.get('lname'):
        f = request.args.get('fname')
        l = request.args.get('lname')
        sqlsend(f,l)
        print(f + " " + l)
    return render_template('home.html')
    
def sqlsend(first,last):
    mydb = mysql.connector.connect(
        host="dev1.wallace",
        user="coop",
        passwd="secret"
    )
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO names (first, last) VALUES ({},{})".format(first,last))
    mycursor.commit()
    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0' ,port=1337)
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
        #print(f + " " + l)
    elif request.args.get('searchreq'):
        s = request.args.get('searchreq')
        
        out = sqlsearch(s)
        return render_template('home.html',out=out)
    return render_template('home.html', out='Your results will show here...')
    
def sqlsend(first,last):
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="coop",
        passwd="secret",
        database="db"
        #buffered=True
    )
    mycursor = mydb.cursor()

    # Safe from SQli
    query = "INSERT INTO names(first, last) VALUES (%s, %s)"
    mycursor.execute(query, (first, last))


    # Example of unsafe query
    #unsafequery = "select * from names where id = USERINPUT"
    #unsafequery = unsafequery.replace("USERINPUT", "1 or 1=1")

    #print("Query : {}".format(unsafequery))
    #mycursor.execute(unsafequery)
    #out = mycursor.fetchall()

    #print(out)

    mydb.commit()
    mycursor.close()


def sqlsearch(search):
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="coop",
        passwd="secret",
        database="db"
        #buffered=True
    )

    mycursor = mydb.cursor()
    try:
        unsafequery = "select * from names where id = USERINPUT"
        unsafequery = unsafequery.replace("USERINPUT", search)
        print("Your Query:   " +unsafequery)
        mycursor.execute(unsafequery)
        out = mycursor.fetchall()
        print(out)

        mydb.commit()
        mycursor.close()

        return out

    except:
        print(unsafequery)
        return "error"

        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0' ,port=1337)
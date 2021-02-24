from flask import Flask, render_template,   request
import mysql.connector


app =Flask(__name__)

mydb=mysql.connector.connect(host="localhost", user="root", passwd="root", database="project" )

mycursor=mydb.cursor()


@app.route('/')
def index():
    return render_template('log.html')

@app.route('/bolt', methods=["POST","GET"])
def utopia():
    chemail=request.form['eid']
    chpas=request.form['pas']
    sk= "select * from cred where email_id like '{}' and password like '{}'".format(chemail,chpas)
    mycursor.execute(sk)
    result = mycursor.fetchall()
    if result:
        return render_template('welcome.html')
    else:
        return render_template('logunsucecssful.html')

@app.route('/io')
def zootopia():
    return render_template('registerpage.html')

@app.route('/nuke',methods=["POST","GET"])
def xylem():
    #chname=request.form['name']
    chremail=request.form['reid']
    chrpass=request.form['rpass']
    san="insert into cred values('{}','{}')".format(chremail, chrpass)
    mycursor.execute(san)
    mydb.commit()
    return render_template('reg_suc.html')


@app.route('/veer')
def pholem():
    return render_template('log.html')

if __name__ == '__main__':
    app.run(debug=True)

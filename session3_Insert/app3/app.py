from flask import Flask, render_template, url_for, request
import mysql.connector
app = Flask(__name__)

#create database and table in mysql
#create database python_db;
#create table std_data(id int auto_increment, primary key(id), name varchar(30), email varchar(30),pass varchar(30));

db=mysql.connector.connect(host="localhost",user="root",password="root",database="python_db")
cursor=db.cursor()

@app.route('/test')
def test():
    return "my webpage"

@app.route('/',methods=['GET'])
def index():
	home=request.args
	if request.args.get('register')=='register':
		n=request.args.get('name')
		e=request.args.get('email')
		p=request.args.get('pass')
		sql = "insert into std_data(name,email, pass) values('{0}','{1}','{2}')".format(n,e,p)
		cursor.execute(sql)
		db.commit()
		return render_template('index.html',success="success",args=home)
    
	else:
		return render_template('index.html',x="Mywebsite", args=home)

	
if __name__=="__main__":
  app.run(debug = True)

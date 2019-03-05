from flask import Flask, render_template, url_for, request,make_response,session
import mysql.connector
app = Flask(__name__)

#   ---- create login_details table in python_db -------------
#    create table login_details(id int, email varchar(30), pass varchar(30), timing timestamp default current_timestamp, 
#    foreign key(id) references std_data(id));

db=mysql.connector.connect(host="localhost",user="root",password="root",database="python_db")
cursor=db.cursor()

@app.route('/test')
def test():
    return "my webpage"

@app.route('/details')
def filter():
    return render_template('details.html')

@app.route('/',methods=['GET'])
def index():
	home=request.args
	        #--- Regitered Data -------#
	if request.args.get('register')=='register':
		n=request.args.get('name')
		e=request.args.get('email')
		p=request.args.get('pass')
		sql = "insert into std_data(name,email, pass) values('{0}','{1}','{2}')".format(n,e,p)
		cursor.execute(sql)
		db.commit()
		return render_template('index.html',success="success",args=home)
	
	     #--- Login to view profile -------#
	elif request.args.get('login') =='login':
		e=request.args.get('email')
		p=request.args.get('pass')
		sql = "select * from std_data where email='{0}' and pass='{1}'".format(e,p)
		cursor.execute(sql)
		view_data=cursor.fetchall()
		resp = make_response()
		resp.set_cookie('pass', p)
		cookie = request.cookies.get('pass')
		x=view_data[0]
		print(x[0])
		sql = "insert into login_details(id,email,pass) values('{0}','{1}','{2}')".format(x[0],e,p)
		cursor.execute(sql)
		db.commit()
		return render_template('profile.html',home=view_data, cookie=cookie)
	
	
	elif request.args.get('update') =='update':
		id=request.args.get('id')
		sql = "select * from std_data where id='{0}'".format(id)
		cursor.execute(sql)
		view_data=cursor.fetchall()
		return render_template('update.html',home=view_data) 

	
	elif request.args.get('updatedata') =='updatedata':
		i=request.args.get('id')
		n=request.args.get('name')
		e=request.args.get('email')
		p=request.args.get('pass')
		print(1)
		sql = "update std_data set name='{1}', email='{2}',pass='{3}' where id='{0}'".format(i,n,e,p)
		print(2)
		cursor.execute(sql)
		print(3)
		db.commit()
		print(4)
		sql = "select * from std_data where id='{0}'".format(i)
		cursor.execute(sql)
		view_data=cursor.fetchall()
		db.commit()
		return render_template('profile.html',success="success",home=view_data)
	elif request.args.get('delete') =='delete':
		id=request.args.get('id')
		sql = "delete from std_data where id='{0}'".format(id)
		cursor.execute(sql)
		db.commit()
		success="success"
		return render_template('index.html',dl="success", args=home)
	
	
	    #Filtering Data
	elif request.args.get('details') =='view':
		start=request.args.get('start')
		end=request.args.get('end')
		start=start+" 00-00-01"
		end=end+" 23-59-59"
		print(start)
		print(end)
		sql = "select * from login_details where timing>='{0}' and timing<='{1}'".format(start,end)
		cursor.execute(sql)
		filter_data=cursor.fetchall()
		return render_template('details.html', home=filter_data, success="success")
	
	
	
	
	else:
		return render_template('index.html',x="Mywebsite", args=home)

#Using Cookies

@app.route('/cookie')
def cookie():
    res = make_response("Setting a cookie")
    res.set_cookie('user', 'root', max_age=60*3)
    return res

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('user')
   return '<h1>welcome '+name+'</h1>'


@app.route('/delete-cookie')
def delete_cookie():
    res = make_response("Cookie Removed")
    res.set_cookie('user', 'root', max_age=0)
    return res
#Filtering the data
"""select * 
from login_details where timing >='2019-02-20 15:09:52'
and timing <='2019-02-20 15:10:07'
"""


#Session Handlings
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.route('/setsession')
def addsession():
	session['username']="Guhan Ganesan"
	return "Session is Added"
	#RuntimeError: The session is unavailable because no secret key was set. 

@app.route('/getsession')
def getsession():
	return session['username']

@app.route('/destroy')
def destroy():
	session.pop('username',None)
	return "Session is removed"

if __name__=="__main__":
  app.run(debug = True)

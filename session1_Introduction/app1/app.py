from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/test')
def test():
    return "Hi Raja"

@app.route('/',methods=['GET'])
def index():
	home=request.args
	return render_template('index.html',x="MyWebsite",y="hello", args=home)

	
if __name__=="__main__":
  app.run(debug = True)

"""


@app.route('/')
def home():
    return "Welcome"

@app.route('/hello')
def hello():
    return "hello"


@app.route('/hello/<x>')
def name(x):
    return "hello Mr. %s" %x


@app.route('/hello/<x>/<y>')
def user(x,y):
    return "Hello Mr. {} and your pass is {}".format(x,y)
    

@app.route('/check/<x>/<y>')
def check(x,y):
	if x=="Guhan" and y=="1234":
		return "Hello Mr. {} and your pass is {} you are eligible to access".format(x,y)
	else:
		return "Hello Mr. {} and your pass is {}... But sorry...".format(x,y)

@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/index1')
def index1():
    return render_template("index.html", user="Guhan", password="1234")

    
 """

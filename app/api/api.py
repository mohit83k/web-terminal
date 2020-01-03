from flask import Flask , make_response , request
import database
import account
import command

app = Flask(__name__)

APP_SALT =  "random_12345"

@app.route('/login', methods = ['GET', 'POST'])
def login():
	"""
	if already logged in , go to home page
	if not logged in, login and go to home page
	if invalid user , go to home page
	"""
	resp = make_response("Welcome")
	username = request.form['username']
	password = request.form['password']
	if request.method == "POST":
		cookies = request.cookies
		if account.check_session(cookies,username):
			return "already exists"
		else:

			if account.check_account(username,password):
				resp.set_cookie("session", account.gen_session_key(username))
				return resp
			
			return "Invalid account"

	print("Invalid method")
	return "Invalid method"




@app.route('/' , methods = ['GET' , 'POST'])
def home():
	return "Hello There"

@app.route('/logout' , methods = ['GET' , 'POST'])
def logout():
	account.remove_session(request.cookies)
	resp = make_response("Successfully logged Out")
	resp.set_cookie('session', '', expires=0)
	return resp

@app.route("/execute" , methods = ['POST'])
def execute():
	if not account.check_session(request.cookies):
		return "{}"

	cmd = request.form['execute']
	output = command.execute(cmd)
	resp = make_response(output )
	resp.headers["Content-Type"] = "application/json"
	return resp


if __name__ == '__main__':
   app.run()
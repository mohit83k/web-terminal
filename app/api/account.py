
import security
import uuid
from database import database

#Persistent session cache
session_cache = {}

#session salt , some random string
def gen_session_key(key):
	if key in session_cache:
		return session_cache[key]

	salt = uuid.uuid1()
	session_key = security.sha256_append_salt( key,str(salt) )
	session_cache[session_key] = key
	return session_key

def check_session(cookie,username = None):
	if "session" not in cookie:
		return False

	if username != None:
		return cookie["session"] in session_cache and username == session_cache[cookie["session"]]

	return cookie["session"] in session_cache


def remove_session(cookie):
	if "session" in cookie:
		session_cache.pop(cookie["session"],None)




password_hash = {}
def get_password_hash(password , salt):
	#Don't Do this. Not a good to idea to store user's password.
	pass


def check_account(username,password):
	_ , user_hash , salt = database.fetch_user(username)
	
	if user_hash == security.sha256_append_salt(password, salt):
		return True

	return False

def add_account(username,password):
	database.add_user( username ,password, str( uuid.uuid1() ) )






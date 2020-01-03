
import framework ,  utils , security

class Database(object):
	"""
	Class to perform database operations. It hides the implementation details.
	Chooses the database dynamically based on configuration. 
	New database can be added by:
		a) Implementing DbFramework in framework.py in a submodule
		b) Adding name of submodule in config.json
		c) submodule is imported and confiuration details are passed as
		argument to constructor
	"""

	#setup the database configuration
	def __init__(self,config_file = "config.json"):
		super(Database, self).__init__()
		self.setup(config_file)

	#read db config  and load the database
	def setup(self,config_file):
		db_type , config_data = self.read_file(config_file)
		self.load(db_type,config_data)

	#reads and validate json data from file
	def read_file(self,config_file):
		json_data = utils.read_json_file(config_file)
		name = json_data["database"]
		config_data = json_data[name]
		return name , config_data

	#loads the instance of the underlying database wrapper
	def load(self,db_type,config_data):
		print("Read file and valid DB conf object\n")
		
		try:
			_database = __import__(db_type,fromlist = ["Database"])
			if not issubclass(_database.Database, framework.DbFramework):
				print(type(_database.Database))
				raise Exception("Database needs to implement framework")

			self.obj = _database.Database(config_data)

		except Exception as error:
			print(error)
			raise error


db = Database()

 
		

def fetch_user(username):
	print(username)
	print(db.obj.fetch_user(username))


if __name__ == "__main__":
	db.obj.add_user( "Random", security.sha256_append_salt("bad_password" , "bad_salt") )
	fetch_user("Random")
	db.obj.save_progress()


# db.obj.add_user( "Mohit", security.sha256_append_salt("password" , "123") )
# fetch_user("Mohit")
# db.obj.save_progress()
# print(__name__)


from database import framework
import utils

class Database(framework.DbFramework):
	"""docstring for Database"""
	def __init__(self,args):
		super (Database, self).__init__()
		print("Loading database configuration ...\n")
		self.file_name = ""

		if "file_name" in args:
			self.file_name = args["file_name"]

		json_obj = self.load(self.file_name)

		#Json Db 
		self.db = {}

		#Store the available db in the memory
		for username , secrete in json_obj.items() :
			self.db[username] = secrete


	def add_user(self,name,secrete,salt):
		self.db[name] = [secrete,salt]

	def load(self,filename):
		return utils.read_json_file(filename)

	def write_file(self,filename,data):
		utils.write_json_file(filename,data)

	def fetch_user(self,username):

		if username in self.db:
			return username , self.db[username][0] , self.db[username][1]

		return username , "" ,""


	def save_progress(self):
		self.write_file(self.file_name , self.db)

	def blocklist(self, list_cmd = []):
		#add the list in database
		#returns the list of blocked command after adding new commands
		pass

	def remove_blocklist(self, list_cmd = []):
		pass

	def add_user_data(self, username , data = {}):
		#Add data about user
		pass






	


	




		
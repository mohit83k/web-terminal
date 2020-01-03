from abc import ABC , abstractmethod

class DbFramework(object):
	"""docstring for DbFramework"""
	def __init__(self):
		super(DbFramework, self).__init__()
	

	@abstractmethod
	def fetch_user(self,username):
		pass


	@abstractmethod
	def add_user(self,name,secrete,salt):
		pass

	@abstractmethod
	def save_progress(self):
		pass

	@abstractmethod
	def blocklist(self, list_cmd = []):
		pass

	@abstractmethod
	def remove_blocklist(self, list_cmd = []):
		pass

	@abstractmethod
	def add_user_data(self, username , data = {}):
		#Add data about user
		pass


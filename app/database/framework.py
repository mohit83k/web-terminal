from abc import ABC , abstractmethod

class DbFramework(object):
	"""docstring for DbFramework"""
	def __init__(self):
		super(DbFramework, self).__init__()
	

	@abstractmethod
	def fetch_user(self,username):
		pass


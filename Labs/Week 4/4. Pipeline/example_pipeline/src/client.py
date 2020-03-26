from sqlalchemy import create_engine


class Client:
	"""
	Connection to database.
	"""

	def __init__(self, params):
		self.engine = create_engine(params.url_string)
		self.conn = self.engine.connect()
from cherrypy import expose, quickstart, server, tools, request
from request_api import RequestAPI

class Converter(object):
	
	# Cherrypy listening IP
	server.socket_host = '127.0.0.1'

	# Supported methods
	methods = {'host.get', 'trend.get', 'trigger.get'}

	@expose
	def index(self):
		""" Index Page """
		return "Welcome to Zabbix API URL"

	@expose
	@tools.json_in()
	@tools.json_out()
	def request(self, method, **kwargs):
		"""Request api from zabbix via cherry."""
		if method in self.methods:
			req = RequestAPI()
			
			# Check which method in 3 methods.
			if method == 'host.get':
				req_id = 'hostid'
			elif method == 'trend.get':
                                req_id = 'itemid'
			elif method == 'trigger.get':
                                req_id = 'triggerid'

			# Check output is single or multiple.
			if type(kwargs['output']) is not list:
				kwargs['output'] = [req_id, kwargs['output']]

			# Request with requests.
			res = req.post_rest(method, kwargs)
			return res
		else:
			return "Error..."


quickstart(Converter())

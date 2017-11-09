from cherrypy import expose, quickstart, server, tools, request
from request_api import RequestAPI
import json

class Converter(object):
	
	server.socket_host = '10.10.130.224'
	methods = {'host.get', 'trend.get', 'trigger.get'}

	@expose
	def index(self):
		return "Hello"

	@expose
	@tools.json_in()
	@tools.json_out()
	def request(self, method, **kwargs):
		if method in self.methods:
			req = RequestAPI()

			if method == 'host.get':
				req_id = 'hostid'
			elif method == 'trend.get':
                                req_id = 'itemid'
			elif method == 'trigger.get':
                                req_id = 'triggerid'

			if type(kwargs['output']) is not list:
				kwargs['output'] = [req_id, kwargs['output']]

			res = req.post_rest(method, kwargs)
			return res
		else:
			return "Error..."


quickstart(Converter())

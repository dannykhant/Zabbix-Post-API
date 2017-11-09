from cherrypy import expose, quickstart, server, tools, request
from request_api import RequestAPI
import json

class Converter(object):
	
	server.socket_host = '10.11.95.68'
	methods = {'host.get', 'trend.get', 'trigger.get'}

	@expose
	def index(self):
		return "Hello"

	@expose
	@tools.json_in()
	@tools.json_out()
	def request(self, method, output, **kwargs):
		if method in self.methods:
			req = RequestAPI()

			if type(output) is not list:
				output = [output]
			
			if method == 'trend.get':
				params = {"output": output, "time_from":kwargs['timefrom'], "time_till":kwargs['timetill'], "limit": 10}
			elif method == 'host.get':
				params = {"output": output, "groupids": kwargs['groupids'], "limit": 10}  
			elif method == 'trigger.get':
				params = {"output": output, "groupids": kwargs['groupids'], "limit": 10}
			

			res = req.post_rest(method, params)
			return res
		else:
			return "Error..."


quickstart(Converter())

import requests, json

class RequestAPI(object):

	def __init__(self):

		self.sess = requests.Session()

		# Zabbix API header
		self.sess.headers.update({'content-type': 'application/json-rpc'})
		
		# Zabbix Server URL
		self.url = u'http://127.0.0.1/zabbix/api_jsonrpc.php'
		
		# Post data for auth_sess
		self.data = json.dumps({"jsonrpc": "2.0", "method": "user.login", "params": {"user": "Admin","password": "zabbix"},"id": 1,"auth": None})


	def auth_sess(self):
		"""Authenticate to zabbix."""

		resp = self.sess.post(self.url, data=self.data)

		# Get Session ID
		sessid = json.loads(resp.text)

		return sessid['result'] 

	def post_rest(self, method, params):
		"""Post API from cherrypy"""

		data =  json.dumps({"jsonrpc": "2.0", "method": method, "params": params,"id": 1,"auth": self.auth_sess()})
		
		# Get response
		resp = self.sess.post(self.url, data=data)	

		return resp.text


import requests, json

class RequestAPI(object):

	def __init__(self):
		self.sess = requests.Session()
		self.sess.headers.update({'content-type': 'application/json-rpc'})

		self.url = u'http://10.11.95.68/zabbix/api_jsonrpc.php'
		self.data = json.dumps({"jsonrpc": "2.0", "method": "user.login", "params": {"user": "Admin","password": "zabbix"},"id": 1,"auth": None})


	def auth_sess(self):
		resp = self.sess.post(self.url, data=self.data)
		sessid = json.loads(resp.text)
		return sessid['result'] 

	def post_rest(self, method, params):
		data =  json.dumps({"jsonrpc": "2.0", "method": method, "params": params,"id": 1,"auth": self.auth_sess()})
		resp = self.sess.post(self.url, data=data)	
		return resp.text


session = RequestAPI()
print(session.post_rest("host.get", {"output": ["hostid"], "groupids": 4}))


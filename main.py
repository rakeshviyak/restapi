#To create the REST server, the code in server.py will also be trivial:

import webapp2
import logging
import json
from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel

class Data(EndpointsModel):
    #Models what we send to the server
    tag = ndb.StringProperty();
    name = ndb.StringProperty();

class Rest(webapp2.RequestHandler):
	def post(self):
		tag=self.request.get('tag')
		name=self.request.get('name')
		if tag or name:
			a=Data(tag=tag,name=name)
			a.put()
			logging.error(a)
			self.response.headers["Content-Type"] = "application/json; charset=UTF-8"
			self.response.write(json.dumps(a.to_dict()))
		else:
			self.response.write("Pls use atleast one of the query string(tag,name) in following format '/?tag=tagname&name=yourname'")
		
	def get(self):
        #pop off the script name ('/api')
		tag=self.request.get('tag')
		name=self.request.get('name')
		q=Data.query()
		if tag:q=q.filter(Data.tag==tag)
		if name:q=q.filter(Data.name==name)
		a=json.dumps([p.to_dict() for p in q.fetch()])
		logging.error(a)
		self.response.headers["Content-Type"] = "application/json; charset=UTF-8"
		self.response.write(a)
	
	def delete(self):
		tag=self.request.get('tag')
		name=self.request.get('name')
		msg="There is no such data"
		if tag:
			datakey=ndb.gql("SELECT * FROM Data WHERE tag=:1",tag).get()
		if name:
			datakey=ndb.gql("SELECT * FROM Data WHERE name=:1",name).get()
		if tag or name:
			if datakey:
				logging.error(datakey)
				self.response.write("Following data is deleted<br>")
				self.response.headers["Content-Type"] = "application/json; charset=UTF-8"
				
				datakey.key.delete()
				msg=datakey.to_dict()
		
		self.response.write(msg)
    
app = webapp2.WSGIApplication([('/*', Rest)], debug=True)
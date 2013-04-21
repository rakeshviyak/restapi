# If you have not yet seen the source in basic/main.py, please take a look.

from google.appengine.ext import endpoints
from google.appengine.ext import ndb
from protorpc import remote
from main import Data
import logging
@endpoints.api(name='myapi', version='v1', description='REST API')
class MyApi(remote.Service):
	
	@Data.method(path='data', http_method='POST', name='data.insert')
	def DataInsert(self, my_model):
		logging.error(my_model)
		my_model.put()
		return my_model
		
	@Data.query_method(query_fields=('name','tag'),path='data', name='data.list')
	def DataList(self, query):
		return query		
	
	@Data.method(path='data', http_method='DELETE', name='data.delete')
	def DataDelete(self,query):
		logging.error(query)
		
		
		if query.tag:
			datakey=Data.query(Data.tag==query.tag).get()
		if query.name:
			datakey=Data.query(Data.name==query.name).get()
		logging.error(datakey)
		if query.tag or query.name:
			
			if datakey:
			
				logging.error(datakey)
				datakey.key.delete()
				return(datakey)
		
		
	
		
		

application = endpoints.api_server([MyApi], restricted=False)
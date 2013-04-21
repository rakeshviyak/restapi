restapi
=======
I have deployed this website based on the REST API and it could add, delete, list all /particular records in json format. 

http://restapi1.appspot.com/

Testing Tool : https://chrome.google.com/webstore/detail/rest-console/cokgbflfommojglbmbpenpphppikmonn?hl=en (to test get, post, delete of the REST API request method)


In order to test, I have created the DB of 2 columns (name and tag):

Class DATA(DB):
        Name (String Property)
        Tag (String Property)

I had some difficulty in installing DJANGO path  to my PYTHONPATH for importing libraries in the app engine. So I used the webapp2 framework.


Scenarios:

i) List all Records: (list the name and tag of all records available in DB in json)
URL: http://restapi1.appspot.com/
Request Method: GET

ii) List Particular Records: (list the name and tag record based on name and/or tag context)
URL: http://restapi1.appspot.com/?name=rakesh&tag=unittest
Request Method: GET
It will list only the record name: "Rakesh" and tag: "unittest" in json

iii) adding a record:
URL: http://restapi1.appspot.com/?name=googlecloud&tag=endpoints
Request Method: POST
It will create a new record in the DB with the name as "goooglecloud" and tag as "endpoints"

iv) Delete a record
URL: http://restapi1.appspot.com/?name=googlecloud&tag=endpoints
Request Method: DELETE
It will delete records with name "googlecloud" and tag "endpoint"


Apart from this, I have created each of these function as an API using the google API infrastructure. 

http://restapi1.appspot.com/_ah/api/explorer

This will redirect to google api console. 
Go to Service > myapi API >

I created 3 API as below to do the same above tasks:

myapi.data.delete  
myapi.data.insert	
myapi.data.list
 
The API console has a inbuilt testing, need to go to each API to test it individually. All the results are in JSON format. These API can be called directly from JS, ANDROID, IOS.

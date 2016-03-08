# haldus.py
# 185.94.112.88
# https://github.com/laurivosandi/ldap2rest#ldap-to-restful-api-bridge

# IMPORTS
import falcon
import ldap
import config

from classes.index import Index
from classes.user import User
 
 

 
# Create paths depeding on user access level
 
app = falcon.API()
#app.add_route('/quote', QuoteResource())

# Fire up the engine
if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.make_server('0.0.0.0', 80, app)
    httpd.serve_forever()
	

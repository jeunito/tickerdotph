import webapp2
from tickerdotph.institutions import bpi
import json

class MainPage(webapp2.RequestHandler):
    def get(self):
        funds = bpi.funds()
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(funds))

app = webapp2.WSGIApplication([
    ('/health', MainPage)
], debug=True)

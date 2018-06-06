import webapp2
from tickerdotph.institutions import bpi
import json

class FundsController(webapp2.RequestHandler):
    def get(self):
        funds = bpi.funds()
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(funds))

class FundController(webapp2.RequestHandler):
    def get(self, fund_ticker):
        funds = bpi.funds()
        fund_price = funds.get(fund_ticker, None)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(dict(name=fund_ticker, price=fund_price )))


app = webapp2.WSGIApplication([
    ('/funds', FundsController),
    ('/funds/([A-Za-z]+)', FundController)
], debug=True)

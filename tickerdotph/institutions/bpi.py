from lxml import html
import urllib2

FUND_PAGE = "https://www.bpiexpressonline.com/p/1/689/investment-funds-daily-prices"
FUND_NAME = 0
FUND_PRICE = 1

def funds():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}
    req = urllib2.Request(FUND_PAGE, {}, headers) 
    doc = urllib2.urlopen(req).read()
    html_page = html.document_fromstring(doc)
    bpi_funds = {}
    for row in html_page.cssselect("table tbody tr")[3:14]:
        row_elements = row.cssselect("td")
        fund_name = row_elements[FUND_NAME].text_content()
        fund_ticker = filter(str.isupper, fund_name)
        fund_price = float(row_elements[FUND_PRICE].text_content())

        bpi_funds[fund_ticker] = fund_price

    return bpi_funds

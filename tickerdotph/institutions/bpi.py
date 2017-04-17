from lxml import html
import urllib2

FUND_PAGE = "https://www.bpiexpressonline.com/p/1/689/investment-funds-daily-prices"
FUND_NAME = 0
FUND_PRICE = 1

def funds():
    doc = urllib2.urlopen(FUND_PAGE).read()
    html_page = html.document_fromstring(doc)
    bpi_funds = {}
    for row in html_page.cssselect("table tbody tr")[3:14]:
        row_elements = row.cssselect("td")
        fund_name = row_elements[FUND_NAME].text_content()
        fund_ticker = filter(str.isupper, fund_name)
        fund_price = float(row_elements[FUND_PRICE].text_content())

        bpi_funds[fund_ticker] = fund_price

    return bpi_funds

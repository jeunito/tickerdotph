from tickerdotph.institutions import bpi
import json

def main(*args):
    funds = bpi.funds()
    if len(args) == 0:
        return funds
    elif len(args) == 2:
        fund_name = args[0].get("name", None)
        return dict(name=fund_name, price=funds.get(fund_name))

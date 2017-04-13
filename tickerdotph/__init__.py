from tickerdotph.institutions import bpi
import json

def main(*args):
    print json.dumps(bpi.funds())

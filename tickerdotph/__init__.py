from tickerdotph.institutions import bpi
import json

def main():
    print json.dumps(bpi.funds())

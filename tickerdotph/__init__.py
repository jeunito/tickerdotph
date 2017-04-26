from tickerdotph.institutions import bpi
import json

def main(*args):
    return bpi.funds() if len(args) == 0 else None

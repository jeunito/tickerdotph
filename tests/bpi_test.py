from tickerdotph.institutions import bpi

import unittest
import vcr

class TestBPI(unittest.TestCase):
    def test_extract(self):
        with vcr.use_cassette("fixtures/cassettes/institutions/bpi.yaml"):
            daily_prices = bpi.funds()

            self.assertEqual(daily_prices["BPIPEIF"], 100.54)

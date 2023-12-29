import unittest
from .data_processing import read_csv

class TestCSVHeaders(unittest.TestCase):

    def test_bills_csv_headers(self):
        expected_fields = ['id', 'title', 'sponsor_id']
        data = read_csv('data/bills.csv', expected_fields)
        self.assertEqual(list(data[0].keys()), expected_fields)

    def test_legislators_csv_headers(self):
        expected_fields = ['id', 'name']
        data = read_csv('data/legislators.csv', expected_fields)
        self.assertEqual(list(data[0].keys()), expected_fields)

    def test_votes_csv_headers(self):
        expected_fields = ['id', 'bill_id']
        data = read_csv('data/votes.csv', expected_fields)
        self.assertEqual(list(data[0].keys()), expected_fields)

    def test_vote_results_csv_headers(self):
        expected_fields = ['id', 'legislator_id', 'vote_id', 'vote_type']
        data = read_csv('data/vote_results.csv', expected_fields)
        self.assertEqual(list(data[0].keys()), expected_fields)

if __name__ == '__main__':
    unittest.main()

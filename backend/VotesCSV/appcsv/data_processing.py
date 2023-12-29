import csv
from collections import defaultdict

bills_path = 'data/bills.csv'
legislators_path = 'data/legislators.csv'
votes_path = 'data/votes.csv'
vote_results_path = 'data/vote_results.csv'

def verify_csv_headers(data, expected_headers, file_path):
    if not data:
        raise ValueError(f"The CSV file '{file_path}' is empty")
    
    actual_headers = data[0].keys()
    if set(actual_headers) != set(expected_headers):
       raise ValueError(f"The CSV file '{file_path}' does not contain the expected fields. Expected fields: {expected_headers}")


def read_csv(file_path, expected_headers):
    with open(file_path, mode='r', encoding='utf-8') as file:
        data = list(csv.DictReader(file))
        verify_csv_headers(data, expected_headers, file_path)
        return data
    
bills_headers = ['id', 'title', 'sponsor_id']
legislators_headers = ['id', 'name']
votes_headers = ['id', 'bill_id']
vote_results_headers = ['id', 'legislator_id', 'vote_id', 'vote_type']

bills = read_csv(bills_path, bills_headers)
legislators = read_csv(legislators_path, legislators_headers)
votes = read_csv(votes_path, votes_headers)
vote_results = read_csv(vote_results_path, vote_results_headers)

def process_data():
    bill_map = {bill['id']: bill for bill in bills}
    legislator_map = {legislator['id']: legislator for legislator in legislators}
    vote_map = {vote['id']: vote for vote in votes}

    legislator_votes = defaultdict(lambda: {'yes': 0, 'no': 0, 'name': None})
    bill_votes = defaultdict(lambda: {'supporters': 0, 'opposers': 0, 'bill_name': None, 'primary_sponsor': None})

    for vote_result in vote_results:
        vote_type = 'yes' if vote_result['vote_type'] == '1' else 'no'
        vote_id = vote_result['vote_id']
        legislator_id = vote_result['legislator_id']
        
        if vote_id in vote_map and legislator_id in legislator_map:
            bill_id = vote_map[vote_id]['bill_id']

            if bill_id in bill_map:
                vote_type_key = 'supporters' if vote_type == 'yes' else 'opposers'
                bill_votes[bill_id][vote_type_key] += 1

                bill_votes[bill_id]['bill_name'] = bill_map[bill_id]['title']
                sponsor_id = bill_map[bill_id]['sponsor_id']
                if sponsor_id in legislator_map:
                    bill_votes[bill_id]['primary_sponsor'] = legislator_map[sponsor_id]['name']

                legislator_votes[legislator_id]['name'] = legislator_map[legislator_id]['name']
                legislator_votes[legislator_id][vote_type] += 1

    return legislator_votes, bill_votes
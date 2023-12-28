import csv
from collections import defaultdict

bills_path = 'C:/GIT/csv-python/VotesCSV/data/bills.csv'
legislators_path = 'C:/GIT/csv-python/VotesCSV/data/legislators.csv'
votes_path = 'C:/GIT/csv-python/VotesCSV/data/votes.csv'
vote_results_path = 'C:/GIT/csv-python/VotesCSV/data/vote_results.csv'

def read_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        return list(csv.DictReader(file))

bills = read_csv(bills_path)
legislators = read_csv(legislators_path)
votes = read_csv(votes_path)
vote_results = read_csv(vote_results_path)

def process_data():
    bill_map = {bill['id']: bill for bill in bills}
    legislator_map = {legislator['id']: legislator for legislator in legislators}
    vote_map = {vote['id']: vote for vote in votes}

    legislator_votes = defaultdict(lambda: {'yes': 0, 'no': 0})
    bill_votes = defaultdict(lambda: {'yes': 0, 'no': 0, 'sponsor': None})

    for vote_result in vote_results:
        vote_type = 'yes' if vote_result['vote_type'] == '1' else 'no'
        vote_id = vote_result['vote_id']
        legislator_id = vote_result['legislator_id']
        
        if vote_id in vote_map and legislator_id in legislator_map:
            bill_id = vote_map[vote_id]['bill_id']

            if bill_id in bill_map:
                legislator_votes[legislator_id][vote_type] += 1
                bill_votes[bill_id][vote_type] += 1

    for bill_id, bill in bill_map.items():
        sponsor_id = bill['sponsor_id']
        if sponsor_id in legislator_map:
            bill_votes[bill_id]['sponsor'] = legislator_map[sponsor_id]['name']

    return legislator_votes, bill_votes

legislator_votes, bill_votes = process_data()
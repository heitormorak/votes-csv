from django.http import JsonResponse
from .data_processing import process_data

def legislator_votes_view(request):
    legislator_votes, _ = process_data()
    return JsonResponse(legislator_votes)

def bill_votes_view(request):
    _, bill_votes = process_data()
    return JsonResponse(bill_votes)

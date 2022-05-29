from django.http import HttpResponse
from .db import get_data as get_db_data
from .json import dumps

def get_data(request):
    results = get_db_data()
    return HttpResponse(dumps(results))
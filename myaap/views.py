import requests
from requests import quote_plus
from django.shortcuts import render
from bs4 import BeautifulSoup
# Create your views here.

BASE_WEB_URL = 'https://chandigarh.craigslist.org/search/?query={}'

def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    response = requests.get('https://chandigarh.craigslist.org/search/bbb?query=python&areaAbb=chandigarh')
    print(quote_plus(search))
    search_result = {
        'search': search,
    }
    return render(request, 'myaap/new_search.html', search_result)
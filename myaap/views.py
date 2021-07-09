from django.shortcuts import render
# from requests.api import post
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from . import models
# Create your views here.

BASE_WEB_URL = 'https://chandigarh.craigslist.org/search/lss?query={}'

def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(Search=search)
    final_url = BASE_WEB_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')

    post_listings = soup.find_all('li', {'class': 'result-row'})

    # post_title = post_listings[0].find(class_='result-title').text
    # post_url = post_listings[0].find('a').get('href')

    # if post_listings.find(class_='result-price'):
    #     post_price = post_listings[0].find(class_='result-price').text
    # else:
    #     post_price = 'N/A'

    final_postings = []
    for post in final_postings:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        if post_listings.find(class_='result-price'):
            post_price = post_listings[0].find(class_='result-price').text
        else:
            post_price = 'N/A'


        final_postings.append(post_title, post_url, post_price)
        

    search_result = {
        'search': search,
        'final_postings': final_postings
    }
    return render(request, 'myaap/new_search.html', search_result)
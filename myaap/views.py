from django.shortcuts import render
# from requests.api import post
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from . import models
# Create your views here.

BASE_WEB_URL = 'https://chandigarh.craigslist.org/search/{}?query={}'
# BASE_EX_URL = 'https://chandigarh.craigslist.org/search/{}?query={}'
BASE_IMG_URL ='https://images.craigslist.org/{}_300x300.jpg'

def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    # print(request.POST.get('category'))
    if request.POST.get('category'):
        category = request.POST.get('category')
    else:
        category = 'bbb'

    models.Search.objects.create(Search=search)
    models.Search.objects.create(category=category)

    final_url = BASE_WEB_URL.format(category,quote_plus(search))
    print(category)
    print(final_url)

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

    for post in post_listings:

        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')

        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'N/A'

        if post.find(class_='result-image').get('data-ids'):
            post_img_id = post.find(class_= 'result-image').get('data-ids').split(',')[0].split(':')[1]
            post_img_url = BASE_IMG_URL.format(post_img_id)
            
        else:
            post_img_url = 'https://craigslist.org/images/peace.jpg'
            

        final_postings.append((post_title, post_url, post_price,post_img_url))
        

    search_result = {
        'search': search,
        'final_postings': final_postings,
    }
    
    # print(search_result['final_postings'])
        
    return render(request, 'myaap/new_search.html', search_result)
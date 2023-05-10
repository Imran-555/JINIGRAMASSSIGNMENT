from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from urllib.parse import urlencode
from django.http import JsonResponse
import requests
import json
from bs4 import BeautifulSoup
from django.http import HttpResponse
from urllib.parse import urlparse


def get_word_frequencies(request):   
    url = request.POST.get('url', request.GET.get('url', ''))   # Get the URL 
        
    if not url:
        return render(request, 'index.html', {'url': url})   #return JsonResponse({'error': 'Missing  URL parameter'})  
        
    

    if not urlparse(url).scheme:
        url = 'https://' + url if url.startswith('www.') else 'https://www.' + url      # Check if the URL, if not, add it and make the URL valid
    

    response = requests.get(url)      # Make a request to the URL and get the response from url
    

    if response.status_code != 200:
        return JsonResponse({'error': 'Could not get the URL'})      # If the response is not, an return an error
    

    html = response.text          # Extract the HTML from the response
    

    soup = BeautifulSoup(html, 'html.parser')       # Parse the HTML using BeautifulSoup
    

    text = soup.get_text()       # Extract the text from the HTML
    

    words = text.split()       # Split the text into words
    

    word_detail = {}       # Create a dictionary 
    

    for word in words:
        if word not in word_detail:           # If the word is not in the dictionary, add it with a frequency of 0 initially
            word_detail[word] = 0
        word_detail[word] += 1               # Increment the frequency of the word by 1
    

    return JsonResponse(word_detail)        # Return the data as JSON








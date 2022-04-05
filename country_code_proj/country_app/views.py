from django.shortcuts import render
import requests


# Create your views here.

def country(request):
    data = requests.get("https://restcountries.com/v3.1/all").json()
    # print(data)
    return render(request, "country_app/country_data.html", {'data': data})

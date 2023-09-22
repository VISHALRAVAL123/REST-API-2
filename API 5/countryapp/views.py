import countryinfo
from django.shortcuts import render

def country_search(request):
    if request.method == 'POST':
        country_name = request.POST.get('country_name')
        country = countryinfo.CountryInfo(country_name)

        if country_name:
            country_data = {
                'name': country_name,
                'capital': country.capital(),
                'population': country.population(),
                # Add other details as needed
            }
        else:
            country_data = None
    else:
        country_data = None

    return render(request,'country_search.html', {'country_data': country_data})

def country_detail(request, country_name):
    country = countryinfo.CountryInfo(country_name)

    country_data = {
        'name': country_name,
        'capital': country.capital(),
        'population': country.population(),
        # Add other details as needed
    }

    return render(request,'country_detail.html', {'country_data': country_data})

import os
from dataclasses import dataclass

import requests


@dataclass
class Location:
    name: str
    formatted_address: str
    lat: float
    lng: float


if __name__ == '__main__':
    api_key = os.environ.get('API_KEY')
    print(api_key)
    query = '7-Eleven Thailand'
    url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={api_key}'

    resp = requests.get(url)
    data = resp.json()

    error_message = data.get('error_message')
    next_page_token = data.get('next_page_token')
    results = data.get('results')

    for each in results:
        name = each.get('name')
        formatted_address = each.get('formatted_address')
        geometry = each.get('geometry')
        location = geometry.get('location')
        lat = location.get('lat')
        lng = location.get('lng')

        location = Location(
            name=name,
            formatted_address=formatted_address,
            lat=lat,
            lng=lng
        )
        print(location)

    print(next_page_token)
    print(error_message)

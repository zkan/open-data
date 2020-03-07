import os
import time
from dataclasses import dataclass

import requests


@dataclass
class Location:
    name: str
    formatted_address: str
    lat: float
    lng: float


def get_data_from_api(url, query, api_key, pagetoken=None):
    if pagetoken:
        url += f'&pagetoken={pagetoken}'
        print(url)

    resp = requests.get(url)
    return resp.json()


def get_locations(results):
    locations = []

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
        locations.append(location)

    return locations


if __name__ == '__main__':
    api_key = os.environ.get('API_KEY')
    query = '7-Eleven Thailand'
    url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={api_key}'

    data = get_data_from_api(url, query, api_key)

    status = data.get('status')
    error_message = data.get('error_message')
    next_page_token = data.get('next_page_token')
    results = data.get('results')
    locations = get_locations(results)

    print(locations)
    print(len(locations))
    print(next_page_token)
    print(error_message)

    while next_page_token:
        data = get_data_from_api(url, query, api_key, pagetoken=next_page_token)

        status = data.get('status')
        if status == 'INVALID_REQUEST':
            time.sleep(5)
            continue

        error_message = data.get('error_message')
        next_page_token = data.get('next_page_token')
        results = data.get('results')
        locations = locations + get_locations(results)

        print(locations)
        print(len(locations))
        print(next_page_token)
        print(error_message)

import json
from haversine import haversine as h
import sys
import os


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf8') as file:
            return json.load(file)


def get_biggest_bar(bars):
    return max(bars, key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(bars):
    return min(bars, key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_closest_bar(bars, longitude, latitude):
    my_coords = [longitude, latitude]
    return min(bars, key=lambda x: h(my_coords, x['geometry']['coordinates']))


def get_bar(bars):
    if sys.argv[1] == 'get_biggest_bar':
        print(get_biggest_bar(bars))
    elif sys.argv[1] == 'get_smallest_bar':
        print(get_smallest_bar(bars))
    elif sys.argv[1] == 'get_closest_bar':
        print(get_closest_bar(bars, float(sys.argv[2]), float(sys.argv[3])))
    else:
        print('ERROR: Unknown operation type.')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            bars = load_data('bars.json')
            get_bar(bars['features'])
        except IndexError:
            print('ERROR: Set your longitude and latitude.')
        except ValueError:
            print('ERROR: Check your coordinates type: float expected.')
    else:
        print('ERROR: Operation expected.')

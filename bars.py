import json
from haversine import haversine
import sys
import os


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf8') as file:
            return json.load(file)


def get_biggest_bar(bars):
    seats_count_dict = {k: bars['features'][k]['properties']['Attributes']['SeatsCount'] for k in
                        range(len(bars['features']))}
    return bars['features'][max(seats_count_dict, key=seats_count_dict.get)]['properties']['Attributes']['Name']


def get_smallest_bar(bars):
    seats_count_dict = {k: bars['features'][k]['properties']['Attributes']['SeatsCount'] for k in
                        range(len(bars['features']))}
    return bars['features'][min(seats_count_dict, key=seats_count_dict.get)]['properties']['Attributes']['Name']


def get_closest_bar(bars, longitude, latitude):
    my_coordinates = [longitude, latitude]
    distances_dict = {k: haversine(my_coordinates, bars['features'][k]['geometry']['coordinates']) for k in
                      range(len(bars['features']))}
    return bars['features'][min(distances_dict, key=distances_dict.get)]['properties']['Attributes']['Name']


if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            bars = load_data('bars.json')
            if sys.argv[1] == 'get_biggest_bar':
                print(get_biggest_bar(bars))
            elif sys.argv[1] == 'get_smallest_bar':
                print(get_smallest_bar(bars))
            elif sys.argv[1] == 'get_closest_bar':
                print(get_closest_bar(bars, float(sys.argv[2]), float(sys.argv[3])))
        except IndexError:
            print('Set your longitude and latitude!')
        except ValueError:
            print('ERROR: Check, that bars file exists and it is valid json file.')
        except:
            print('Unexpected error: ', sys.exc_info()[0])
            raise
    else:
        print('Path to json file expected!')

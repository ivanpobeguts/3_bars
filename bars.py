import json
from haversine import haversine
import sys


def load_data(filepath):
    with open(filepath, 'r', encoding='utf8') as file:
        parsed = json.load(file)
    return parsed


def get_biggest_bar(bars_json):
    bars_ammount = [i for i in range(len(bars_json['features']))]
    seats_count_dict = {k: bars_json['features'][k]['properties']['Attributes']['SeatsCount'] for k in bars_ammount}
    return bars_json['features'][max(seats_count_dict, key=seats_count_dict.get)]['properties']['Attributes']['Name']


def get_smallest_bar(bars_json):
    bars_ammount = [i for i in range(len(bars_json['features']))]
    seats_count_dict = {k: bars_json['features'][k]['properties']['Attributes']['SeatsCount'] for k in bars_ammount}
    return bars_json['features'][min(seats_count_dict, key=seats_count_dict.get)]['properties']['Attributes']['Name']


def get_closest_bar(bars_json, longitude, latitude):
    my_coordinates = [longitude, latitude]
    bars_ammount = [i for i in range(len(bars_json['features']))]
    distances_dict = {k: haversine(my_coordinates, bars_json['features'][k]['geometry']['coordinates']) for k in bars_ammount}
    return bars_json['features'][min(distances_dict, key=distances_dict.get)]['properties']['Attributes']['Name']



if __name__ == '__main__':
    bars_json = load_data("bars.json")
    # if len(sys.argv) == 1:
    #     print('Choose the operation: "get_biggest_bar", "get_smallest_bar" or "get_closest_bar"!')
    # if ''.join(sys.argv[1]) == 'get_biggest_bar':
    #     print(get_biggest_bar(bars_json))
    # elif str(sys.argv[1]) == 'get_smallest_bar':
    #     print(get_smallest_bar(bars_json))
    # elif str(sys.argv[1]) =='get_closest_bar':
    #     if str(sys.argv[2]) != None and str(sys.argv[3]) != None:
    #         print(get_closest_bar(bars_json, sys.argv[2], sys.argv[3]))
    #     else:
    #         print('Set your longitude and latitude!')
    # else:
    #     print('Choose the operation: "get_biggest_bar", "get_smallest_bar" or "get_closest_bar"!')
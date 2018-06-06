import json
from haversine import haversine as h
import argparse


def load_data(filepath):
    with open(filepath, 'r', encoding='utf8') as file:
        return json.load(file)


def get_biggest_bar(bars):
    return max(bars, key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(bars):
    return min(bars, key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_closest_bar(bars, longitude, latitude):
    user_coords = [longitude, latitude]
    return min(bars, key=lambda x: h(user_coords, x['geometry']['coordinates']))


def print_bar(bar):
    print('Name: ', bar['properties']['Attributes']['Name'])
    print('Address: ', bar['properties']['Attributes']['Address'])
    print('Area: ', bar['properties']['Attributes']['AdmArea'])
    print('District: ', bar['properties']['Attributes']['District'])
    print('Phone: ', bar['properties']['Attributes']['PublicPhone'][0]['PublicPhone'])
    print('Seats count: ', bar['properties']['Attributes']['SeatsCount'])
    print('Coordinates: ', bar['geometry']['coordinates'])


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='Path to json file')
    parser.add_argument('command', choices=function_map.keys())
    parser.add_argument('longitude', type=float, nargs='?', const=None)
    parser.add_argument('latitude', type=float, nargs='?', const=None)
    return parser


if __name__ == '__main__':
    function_map = {'get_biggest_bar': get_biggest_bar,
                    'get_smallest_bar': get_smallest_bar,
                    'get_closest_bar': get_closest_bar}
    args = get_parser().parse_args()
    try:
        bars = load_data(args.filepath)['features']
        if args.command == 'get_closest_bar' and args.longitude and args.latitude:
            bar = function_map[args.command](bars, args.longitude, args.latitude)
        else:
            bar = function_map[args.command](bars)
        print_bar(bar)
    except json.decoder.JSONDecodeError:
        print('File is not json.')
    except FileNotFoundError:
        print('File not found.')
    except TypeError:
        print('Set your longitude and latitude.')

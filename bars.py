import json
from haversine import haversine as h
import sys
import os
import argparse


def load_data(filepath):
    with open(filepath, 'r', encoding='utf8') as file:
        return json.load(file)


def get_biggest_bar(bars):
    return max(bars, key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(bars):
    return min(bars, key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_closest_bar(bars, longitude, latitude):
    if not longitude or not latitude:
        return None
    user_coords = [longitude, latitude]
    return min(bars, key=lambda x: h(user_coords, x['geometry']['coordinates']))


def pretty_print_json(raw_json):
    print(json.dumps(raw_json, indent=5, sort_keys=True, ensure_ascii=False))


def print_bar(bar):
    if not bar:
        print('Set your longitude and latitude.')
    else:
        print('Bar:')
        pretty_print_json(bar)


FUNCTION_MAP = {'get_biggest_bar': get_biggest_bar,
                'get_smallest_bar': get_smallest_bar,
                'get_closest_bar': get_closest_bar}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='Path to json file')
    parser.add_argument('command', choices=FUNCTION_MAP.keys())
    parser.add_argument('longitude', type=float, nargs='?', const=None)
    parser.add_argument('latitude', type=float, nargs='?', const=None)
    args = parser.parse_args()
    try:
        bars = load_data(args.filepath)['features']
        if args.command == 'get_closest_bar':
            bar = FUNCTION_MAP[args.command](bars, args.longitude, args.latitude)
        else:
            bar = FUNCTION_MAP[args.command](bars)
        print_bar(bar)
    except json.decoder.JSONDecodeError:
        print('Файл не в формате json.')
    except FileNotFoundError:
        print('Файл не найден.')

#!/usr/bin/env python
from polyline.codec import PolylineCodec

import json
import pprint
from datetime import datetime
from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader(__name__, 'templates'))

pp = pprint.PrettyPrinter(indent=2)

def geojson(coordinates):
    rev = list()
    for el in coordinates:
        rev.append([el[1], el[0]])
    return {'type': 'LineString',
            'coordinates': rev
           }

with open('/tmp/act.json') as f:
    data = json.load(f)

years = dict()
for el in data:
    date = datetime.strptime(el['start_date_local'], '%Y-%m-%dT%H:%M:%SZ')
    try:
        years[date.year]
        years[date.year]['coords']
        years[date.year]['distance']
    except KeyError:
        years[date.year] = dict()
        years[date.year]['coords'] = list()
        years[date.year]['distance'] = list()

    years[date.year]['distance'].append((el['distance']))
    years[date.year]['coords'].append(geojson(PolylineCodec().decode(el['map']['summary_polyline'])))


for year in years.keys():
    i = 0
    year_string = ""
    year_string += "var cyclelines = ["
    end = len(years[year]['coords'])
    for el in years[year]['coords']:
        year_string += json.dumps(el)
        print(el)

        if not i == end-1:
            year_string += ","
        i += 1

    year_string += "];"

    year_total = round(sum(years[year]['distance'])/1000, 2)

    template = env.get_template('index.html')
    with open("/tmp/{}_index.html".format(year), 'w') as f:
        f.write(template.render(theLines=year_string, distance=year_total))

    print("Wrote: {}".format(year))
    print("Total Distance: {}".format(year_total))

# pp.pprint(years)

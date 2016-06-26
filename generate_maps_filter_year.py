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
    except KeyError:
        years[date.year] = list()

    years[date.year].append(geojson(PolylineCodec().decode(el['map']['summary_polyline'])))


for year in years.keys():
    i = 0
    year_string = ""
    year_string += "var cyclelines = ["
    end = len(years[year])
    for el in years[year]:
        year_string += json.dumps(el)
        if not i == end-1:
            year_string += ","
        i += 1
    year_string += "];"

    template = env.get_template('index.html')
    with open("/tmp/{}_index.html".format(year), 'w') as f:
        f.write(template.render(theLines=year_string))

    print("Wrote: {}".format(year))

# pp.pprint(years)

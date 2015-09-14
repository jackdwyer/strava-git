from polyline.codec import PolylineCodec

import json


def geojson(coordinates):
    print(coordinates)
    rev = list()
    for el in coordinates:
        rev.append([el[1], el[0]])
    return {'type': 'LineString',
            'coordinates': rev}


with open('/tmp/act.json') as f:
    data = json.load(f)

for el in data:
    with open('generated_maps/' + el['start_date_local'] + '.geojson', 'w') as f:
        json.dump(geojson(PolylineCodec().decode(el['map']['summary_polyline'])), f)

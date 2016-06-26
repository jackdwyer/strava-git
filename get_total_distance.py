import json


with open('/tmp/act.json') as f:
    data = json.load(f)

total = 0.0
for el in data:
    # print el['distance']
    total += el['distance']
    # with open('generated_maps/' + el['start_date_local'] + '.geojson', 'w') as f:
    # #     json.dump(geojson(PolylineCodec().decode(el['map']['summary_polyline'])), f)
print("{} km".format(total/1000))

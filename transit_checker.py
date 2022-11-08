import requests
import json
import time as tm
from datetime import datetime

timestamps = []
routes_that_matter = [2, 6, 9, 10, 102, 106, 31, 32, 33, 34, 13]

while floor(datetime.now().timestamp()):
    json_file = requests.get('http://gtfs.ltconline.ca/Vehicle/VehiclePositions.json')
    site_json = json.loads(json_file.text)
    timestamp = site_json.get('header').get('timestamp')

    if timestamp not in timestamps:
        timestamps.append(timestamp)
        for item in site_json.get('entity'):
            if item.get('vehicle').get('trip').get('route_id') in str(routes_that_matter):
                with open('transit_data.txt', 'a') as datafile:
                    datafile.write(str(item))
    with open('transit_data.txt', 'a') as datafile:
        datafile.write('\n')
    tm.sleep(30)


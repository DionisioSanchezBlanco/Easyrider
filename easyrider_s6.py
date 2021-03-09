import json
import re
import collections

json_data = [
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "08:12"
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 5,
        "stop_type": "O",
        "a_time": "08:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
    },
    {
        "bus_id": 256,
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "09:20"
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "10:12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]

# Regexp for hours "hh:mm"
template_hour = r"^([0-2]{1}[0-9]{1}|2[0-3])\:[0-5]{1}[0-9]{1}$"
template_street = r"^[A-Z]\w+\s?\w+?\s?(Avenue|Street|Road|Boulevard)+$"
 
counter = [0, 0, 0, 0, 0, 0]
bus_lines = {"128": 0, "256": 0, "512": 0, "1024": 0}
start_stops = {"128": "Prospekt Avenue", "256": "Pilotow Street", "512": "Bourbon Street"}
transfer_stops = {"128": ["Elm Street", "Sunset Boulevard"], "256": "Elm Street", "512": None}
finish_stops = {"128": "Sesame Street", "256": "Sesame Street", "512": "Sunset Boulevard"}
wrong_stops = []


def stops(jdata_dict, bus_lines):
    global start_stops, transfer_stops, finish_stops, wrong_stops

    for line in jdata_dict:
        if line["stop_type"] == "O":
            if line["stop_name"] in transfer_stops[str(line["bus_id"])]:
                wrong_stops.append(line["stop_name"])
            else:
                for keys, values in start_stops.items():
                    if line["stop_name"] == values:
                        wrong_stops.append(line["stop_name"])

                for keys, values in finish_stops.items():
                    if line["stop_name"] == values:
                        wrong_stops.append(line["stop_name"])

    wrong_stops.sort()
  
# Data imported from input
jdata_end = json.loads(input())

#jdata_dict = json.dumps(json_data)
#jdata_end = json.loads(jdata_dict)

#number_stops(jdata_dict, bus_lines)
stops(jdata_end, bus_lines)

print("On demand stops test:")
if wrong_stops == []:
    print("OK")
else:
    print(f"Wrong stop type: {wrong_stops}")

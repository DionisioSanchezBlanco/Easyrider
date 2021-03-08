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
        "stop_type": "",
        "a_time": "08:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:17"
    },
    {
        "bus_id": 128,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:07"
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
        "stop_type": "",
        "a_time": "09:44"
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
 
counter = [0, 0, 0, 0, 0, 0]
bus_lines = {"128": "", "256": "", "512": "", "1024": ""}
bus_lines_past = {"128": "", "256": "", "512": "", "1024": ""}
bus_checked = {}
bus_checked_list = []

def check_hours(jdata_dict, bus_lines, bus_lines_past):
    checker = 0
    
    for lines in jdata_dict:
        bus_lines_past[str(lines['bus_id'])] = bus_lines[str(lines['bus_id'])]
        # Current time
        bus_lines[str(lines['bus_id'])] = lines['a_time']
            
        if bus_lines[str(lines['bus_id'])] <= bus_lines_past[str(lines['bus_id'])]:
            checker += 1
            #bus_checked = dict(bus_checked_aux)
            if lines['bus_id'] in bus_checked_list:
                pass
            else:
                bus_checked_list.append(lines['bus_id'])
                bus_checked[str(lines['bus_id'])] = lines['stop_name']
            
            #if bus_checked[str(lines['bus_id'])] != bus_lines[str(lines['bus_id'])] or bus_checked[str(lines['bus_id'])] is False:
            #    bus_checked[str(lines['bus_id'])] = lines['stop_name']
            #print(bus_checked_list)
            #print(bus_checked)
            
    for keys, values in bus_checked.items():
        print(f"bus_id line {keys}: wrong time on station {values}")
            #print(f"bus_id line {lines['bus_id']}: wrong time on station {lines['stop_name']}")
            #print(bus_checked)

    if checker == 0:
        print('OK')
        #print(bus_lines)

# Data imported from input
# jdata_end = json.loads(input())

#Data imported from variable
jdata_dict = json.dumps(json_data)
jdata_end = json.loads(jdata_dict)

print("Arrival time test:")
check_hours(jdata_end, bus_lines, bus_lines_past)
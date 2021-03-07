import json
import re
import collections

json_data = [{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Fifth Avenue", "next_stop" : 4, "stop_type" : "S", "a_time" : "08:12"},
 {"bus_id" : 128, "stop_id" : 4, "stop_name" : "Abbey Road", "next_stop" : 5, "stop_type" : "", "a_time" : "08:19"},
 {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Santa Monica Boulevard", "next_stop" : 8, "stop_type" : "O", "a_time" : "08:25"},
 {"bus_id" : 128, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 11, "stop_type" : "", "a_time" : "08:37"},
 {"bus_id" : 128, "stop_id" : 11, "stop_name" : "Beale Street", "next_stop" : 12, "stop_type" : "", "a_time" : "09:20"},
 {"bus_id" : 128, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 14, "stop_type" : "", "a_time" : "09:45"},
 {"bus_id" : 128, "stop_id" : 14, "stop_name" : "Bourbon Street", "next_stop" : 19, "stop_type" : "O", "a_time" : "09:59"},
 {"bus_id" : 128, "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"},
 {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:13"}, 
 {"bus_id" : 256, "stop_id" : 3, "stop_name" : "Startowa Street", "next_stop" : 8, "stop_type" : "", "a_time" : "08:16"},
 {"bus_id" : 256, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 10, "stop_type" : "", "a_time" : "08:29"}, 
 {"bus_id" : 256, "stop_id" : 10, "stop_name" : "Lombard Street", "next_stop" : 12, "stop_type" : "", "a_time" : "08:44"}, 
 {"bus_id" : 256, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 13, "stop_type" : "O", "a_time" : "08:46"},
 {"bus_id" : 256, "stop_id" : 13, "stop_name" : "Orchard Road", "next_stop" : 16, "stop_type" : "", "a_time" : "09:13"},
 {"bus_id" : 256, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 17, "stop_type" : "", "a_time" : "09:26"}, 
 {"bus_id" : 256, "stop_id" : 17, "stop_name" : "Khao San Road", "next_stop" : 20, "stop_type" : "O", "a_time" : "10:25"}, 
 {"bus_id" : 256, "stop_id" : 20, "stop_name" : "Michigan Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "11:26"}, 
 {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Arlington Road", "next_stop" : 7, "stop_type" : "S", "a_time" : "11:06"},
 {"bus_id" : 512, "stop_id" : 7, "stop_name" : "Parizska Street", "next_stop" : 8, "stop_type" : "", "a_time" : "11:15"},
 {"bus_id" : 512, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 9, "stop_type" : "", "a_time" : "11:56"}, 
 {"bus_id" : 512, "stop_id" : 9, "stop_name" : "Niebajka Avenue", "next_stop" : 15, "stop_type" : "", "a_time" : "12:20"},
 {"bus_id" : 512, "stop_id" : 15, "stop_name" : "Jakis Street", "next_stop" : 16, "stop_type" : "", "a_time" : "12:44"}, 
 {"bus_id" : 512, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 18, "stop_type" : "", "a_time" : "13:01"},
 {"bus_id" : 512, "stop_id" : 18, "stop_name" : "Jakas Avenue", "next_stop" : 19, "stop_type" : "", "a_time" : "14:00"},
 {"bus_id" : 1024, "stop_id" : 21, "stop_name" : "Karlikowska Avenue", "next_stop" : 12, "stop_type" : "S", "a_time" : "13:01"}, 
 {"bus_id" : 1024, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:00"},
 {"bus_id" : 512, "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:11"}]


# Regexp for hours "hh:mm"
template_hour = r"^([0-2]{1}[0-9]{1}|2[0-3])\:[0-5]{1}[0-9]{1}$"
template_street = r"^[A-Z]\w+\s?\w+?\s?(Avenue|Street|Road|Boulevard)+$"
 
counter = [0, 0, 0, 0, 0, 0]
bus_lines = {"128": 0, "256": 0, "512": 0, "1024": 0}
start_stops = []
transfer_stops = []
finish_stops = []
transfer_stops_f = []

def streets(jdata_dict, bus_lines):
    global start_stops, transfer_stops, finish_stops, transfer_stops_f

    for line in jdata_dict:
        if line["stop_type"] == 'S':
            start_stops.append(line['stop_name'])
            bus_lines[str(line['bus_id'])] += 1
        if line["stop_type"] == 'F':
            finish_stops.append(line['stop_name'])
            bus_lines[str(line['bus_id'])] += 1           
        if line["stop_type"] == '':
            transfer_stops.append(line['stop_name'])

    #Intersections
    rep_starts = [x for x, y in collections.Counter(start_stops).items() if y > 1]
    rep_finish = [x for x, y in collections.Counter(finish_stops).items() if y > 1]
    rep_transfer = [x for x, y in collections.Counter(transfer_stops).items() if y > 1]

    for street in start_stops:
        for street_t in transfer_stops:
            if street_t == street:
                transfer_stops_f.append(street)
    
    for street in finish_stops:
        for street_t in transfer_stops:
            if street_t == street:
                transfer_stops_f.append(street)

    for street in rep_starts:
        if street:
            transfer_stops_f.append(street)

    for street in rep_finish:
        if street:
            transfer_stops_f.append(street)

    for street in rep_transfer:
        if street:
            transfer_stops_f.append(street)



    #Remove duplicates

    start_stops = sorted(list(dict.fromkeys(start_stops)))
    transfer_stops = sorted(list(dict.fromkeys(transfer_stops)))
    transfer_stops_f = sorted(list(dict.fromkeys(transfer_stops_f)))
    finish_stops = sorted(list(dict.fromkeys(finish_stops)))

def check_SF(bus_lines):
    for keys, values in bus_lines.items():
        if values % 2 != 0:
            return keys

 
# Data imported from input
jdata_end = json.loads(input())

#jdata_dict = json.dumps(json_data)
#jdata_end = json.loads(jdata_dict)

#number_stops(jdata_dict, bus_lines)
streets(jdata_end, bus_lines)
line_fail = check_SF(bus_lines)
if line_fail:
    print(f"There is no start or end stop for the line: {line_fail}.")
else:
    print(f"Start stops: {len(start_stops)} {start_stops}")
    print(f"Transfer stops: {len(transfer_stops_f)} {transfer_stops_f}")
    print(f"Finish stops: {len(finish_stops)} {finish_stops}")

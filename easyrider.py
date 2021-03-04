import json
import re

# Regexp for hours "hh:mm"
template_hour = r"^([0-2]{1}[0-9]{1}|2[0-3])\:[0-5]{1}[0-9]{1}$"
template_street = r"^[A-Z]\w+\s?\w+?\s?(Avenue|Street|Road|Boulevard)+$"
 
counter = [0, 0, 0, 0, 0, 0]
bus_lines = {"128": 0, "256": 0, "512": 0, "1024": 0}

def number_stops(jdata_dict, bus_lines):

    for line in jdata_dict:
        if line["bus_id"] == 128:
            bus_lines["128"] += 1
        if line["bus_id"] == 256:
            bus_lines["256"] += 1
        if line["bus_id"] == 512:
            bus_lines["512"] += 1
        if line["bus_id"] == 1024:
            bus_lines["1024"] += 1

    for keys, values in bus_lines.items():
        print(f"bus_id: {keys}, stops: {values}") 
# Data imported from input
jdata_dict = json.loads(input())
number_stops(jdata_dict, bus_lines)
'''
for line in jdata_dict:
    if type(line['bus_id']) != int or line['bus_id'] == False:
        counter[0] += 1
    if type(line['stop_id']) != int or line['stop_id'] == False:
        counter[1] += 1
    if type(line['stop_name']) != str or line['stop_name'] == "" or re.match(template_street, line['stop_name']) is None:
        counter[2] += 1
    if type(line['next_stop']) != int:
        counter[3] += 1
    if type(line['stop_type']) != str or line['stop_type'] not in ['O', 'S', 'F', '']:
        counter[4] += 1 
    if type(line['a_time']) != str or line['a_time'] == "" or re.match(template_hour, line['a_time']) is None:
        counter[5] += 1


print(f"Format validation: {sum(counter)} errors")
print(f"stop_name: {counter[2]}")
print(f"stop_type: {counter[4]}")
print(f"a_time: {counter[5]}")
#i = 0
#for errors in jdata_dict[0]:
#    if counter[i] > 0:
#        print(f"{errors}: {counter[i]}")
#    i += 1
'''        
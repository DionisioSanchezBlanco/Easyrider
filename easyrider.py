import json
 
counter = [0, 0, 0, 0, 0, 0]

# Data imported from input
jdata_dict = json.loads(input())
for line in jdata_dict:
    if type(line['bus_id']) != int or line['bus_id'] == False:
        counter[0] += 1
    if type(line['stop_id']) != int or line['stop_id'] == False:
        counter[1] += 1
    if type(line['stop_name']) != str or line['stop_name'] == "":
        counter[2] += 1
    if type(line['next_stop']) != int:
        counter[3] += 1
    if type(line['stop_type']) != str or line['stop_type'] not in ['O', 'S', 'F', '']:
        counter[4] += 1 
    if type(line['a_time']) != str or line['a_time'] == "":
        counter[5] += 1


print(f"Type and required field validation: {sum(counter)} errors")
i = 0
for errors in jdata_dict[0]:
    print(f"{errors}: {counter[i]}")
    i += 1
        
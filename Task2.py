"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def add_to_list(list_to_add, new_list, dur):
    for item in new_list:
        if item in list_to_add:
            cur_duration = list_to_add[item]
            list_to_add[item] = int(cur_duration) + int(dur)

        else:
            list_to_add[item] = int(dur)


coll = {}
max_duration = 0
max_number = ""
for e in calls:
    p_number1 = e[0]
    p_number2 = e[1]
    duration = e[3]
    add_to_list(coll, [p_number1,p_number2],duration)
    if max_duration < int(coll[p_number1]):
        max_duration = int(coll[p_number1])
        max_number = p_number1

    if max_duration < int(coll[p_number2]):
        max_duration = int(coll[p_number2])
        max_number = p_number2

print(str(max_number) + " spent the longest time, " + str(max_duration) + " seconds, on the phone during September 2016.")


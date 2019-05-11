"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
originated = []
destination = []

for num in calls:
    if num[0] not in destination and num[0] not in originated:
        originated.append(num[0])

    if num[1] not in destination:
        destination.append(num[1])

    if num[1] in originated:
        originated.remove(num[1])


print("These numbers could be telemarketers: ")
originated.sort()

for i in originated:
    print(i)
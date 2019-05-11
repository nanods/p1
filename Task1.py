def addToList(listToadd, numToadd):
    if numToadd not in listToadd:
        listToadd.append(numToadd)

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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

uniqueNumbers = []
# add  numbers in texts both sending and receiving
for text in texts:
    addToList(uniqueNumbers, text[0])
    addToList(uniqueNumbers, text[1])

# add calls number both calling and receiving
for call in calls:
    addToList(uniqueNumbers, call[0])
    addToList(uniqueNumbers, call[1])

print("There are %d different telephone numbers in the records." % len(uniqueNumbers))

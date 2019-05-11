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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""


def get_area_code(p_bumber):
    if "(" in p_bumber and ")" in p_bumber:
        return p_bumber[1:p_bumber.index(")")]
    elif " " in p_bumber:
        return p_bumber[:4]
    elif p_bumber.index("140") == 0:
        return "140"

    return None


def find_called_destinations(calling_number_code):
    area_codes = []

    for call in calls:
        call_number = call[0]
        destination = call[1]

        if calling_number_code in call_number:
            a_code = get_area_code(destination)
            area_codes.append(a_code)
    area_codes.sort()
    return area_codes


print("The numbers called by people in Bangalore have codes:")
filtered_codes = find_called_destinations("(080)")
duplicate_check = []
for i in filtered_codes:
    if i not in duplicate_check:
        print(i)
        duplicate_check.append(i)

"""
(022)28952819
(022)47410783
(080)33118033
(080)35121497
(04344)322628
90365 06212

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

total_calls_bang = len(filtered_codes)
bang_only = 0
for i in filtered_codes:
    if "080" in i:
        bang_only += 1


percent = bang_only/total_calls_bang


print("{0:.2f}".format(percent * 100) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
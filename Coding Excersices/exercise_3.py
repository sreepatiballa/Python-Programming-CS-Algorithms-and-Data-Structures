## Challenge exercise - list, tuple, dictionary and functions.
# Sample execution code is provided at the bottom, you may run it now
# to see and get a feel for the existing output then build each function
# and re-run the script.
from collections import Counter
import os
buckets = [ ('john.doe@example.com',{'first_name':'john','last_name':'doe'}),
            ('jane.doe@example.com',{'first_name':'jane','last_name':'doe'}),
            ('derek.zoo@example.com',{'first_name':'derek','last_name':'zoolander'}),
            ('murph.cooper@example.com',{'first_name':'murph','last_name':'cooper'}),
            ('ned.stark@example.com',{'first_name':'ned','last_name':'stark'})
            ]


# Question 1: Create a function that returns all last names in the list
# with the number of occurances of that last name, example 'doe': 2, 'stark': 1
# use the Counter function from collections module to count the occurances with ease.
def get_last_name_count(list_of_records):
    """
    Function that returns all last names in the list with the number of occurances of that last name
    """
    lastnames = []
    for i in range(len(list_of_records)):
        lastnames.append(list_of_records[i][1]['last_name'])
    return Counter(lastnames)

    # list_of_last_names = []
    # for item in list_of_records:
    #     email, full_name = item
    #     list_of_last_names.append(full_name['last_name'])
    # return Counter(lastnames), Counter(list_of_last_names)

    ## end of function ##


# Question 2: Create a function that compares first and last names of records
# given the email address, first and last names to compare. Exact matches only,
# ignore case. Return True if exact match, return False otherwise.
def compare_full_name(list_of_records, email, first_name, last_name):
    """
    Funciton that compares the first and last names of records give the email address, first and last names
    """
    ## Write code below ##
    for i in list_of_records:
        email_temp, full_name_temp = i
        if email == email_temp:
            return first_name == full_name_temp['first_name'] and last_name == full_name_temp['last_name']
    return False
    ## end of function ##



# (CHALLENGE) Question 3: Create a function that can reset the value for first_name
# and last_name for a record found with a specific email address
# while leaving the rest of the list unchanged, if the email address
# does not exist, then append a new record to the list with the new email
# address, first name and last name.
# Hint: Solutions use the enumerate function to track index of a record.
def update_record(list_of_records, email, first_name, last_name):
    """
    fill in docstring
    """
    ## Write code below ##
    found_email = False
    for i,j in enumerate(list_of_records):
        email_temp, full_name_temp = j
        if email_temp == email:
            found_email = True
            break
    if found_email == True:
        full_name_temp['first_name'] = first_name
        full_name_temp['last_name'] = last_name
    else:
        list_of_records.append((email,{'first_name':first_name,'last_name':last_name}))

    ## end of function ##

def divider():
    print()
    print("-"*40)
    print()

print("The last names and their counts are as follows:")
result = get_last_name_count(buckets)
# un-comment the code below once your get_last_name_count function works
for k, v in result.items():
    print(f"{k}: {v}")
divider()

print("Does ned's first and last name match our records?")
print(compare_full_name(buckets,'ned.stark@example.com','ned','stark'))
divider()

print("Changing john's first name to jon and last name to snow")
update_record(buckets,'john.doe@example.com','jon','snow')
divider()

print("Adding new record ironman@example.com")
update_record(buckets,'ironman@example.com','iron','man')
divider()

print("Updated last names and their count are as follows:")
result = get_last_name_count(buckets)
# un-comment the code below once your get_last_name_count function works
for k, v in result.items():
    print(f"{k}: {v}")
divider()

print("Full list")
for item in buckets:
    record_email, full_name = item
    print(f"Email: {record_email}, first name: {full_name['first_name']}, last_name: {full_name['last_name']}")

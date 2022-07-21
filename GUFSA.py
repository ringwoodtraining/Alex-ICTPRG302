# this program is for Shut Up and Listen Education Services
# this program is generating usernames for staff accounts
# Python program for ICTPRG302 - Alex Cojocariu 21/7/2022

# put the names from the txt file into a list
import sys
try:
    staff = open("SULES_Staff.txt", "r")
    staff_list = []
    for line in staff:
        single_line = line.strip()
        staff_list.append(single_line)
    staff.close()
except FileNotFoundError:
    print("SULES_Staff.txt file is not found")
    sys.exit()
else:
    staff = open("SULES_Staff.txt", "r")
    staff_list = []
    for line in staff:
        single_line = line.strip()
        staff_list.append(single_line)
    staff.close()

# grab the first letter of staff names in the staff_list
part1 = []
def firstLetter():
    firstLetter = [x[0] for x in staff_list]
    return firstLetter
part1 = firstLetter()

# get the last name of the staff
staff_list_joined = ' '.join(staff_list)
def ConvertToList(string):
    li = list(string.split(" "))
    return li
seperated = ConvertToList(staff_list_joined)
part2 = seperated[1::2] #start:end:step

# generate 10 random 4 digit numbers
import random
part3 = []
for ten in range(10):
    randomNumber = random.randint(1000,9999)
    part3.append(randomNumber)

# create the usernames for each respective staff
usernames = []
for i in range(10):
    part_1 = part1[i]
    part_2 = part2[i]
    part_3 = part3[i]
    concatinated = part_1.lower() + part_2.lower() + str(part_3)
    usernames.append(concatinated)

# write list to txt file SULES_Usernames
with open("SULES_Usernames.txt", "w") as f:
    for line in usernames:
        f.write(line)
        f.write('\n')
f.close



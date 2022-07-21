# this program is for Shut Up and Listen Education Services
# this program is generating usernames for staff accounts
# Python program for ICTPRG302

#put the names from the txt file into a list
staff = open("SULES_Staff.txt", "r")
staff_list = []
for line in staff:
    single_line = line.strip()
    staff_list.append(single_line)
#print(staff_list)
staff.close()

# grab the first letter of staff names in the staff_list
part1 = []
def firstLetter():
    firstLetter = [x[0] for x in staff_list]
    return firstLetter
part1 = firstLetter()
#print(part1)

# perpare to get the last name of the staff
staff_list_joined = ' '.join(staff_list)
def ConvertToList(string):
    li = list(string.split(" "))
    return li
seperated = ConvertToList(staff_list_joined)
#print(ConvertToList(staff_list_joined))

#get every last name of the staff
part2 = seperated[1::2] #start:end:step
#print(part2)

#generate 10 random 4 digit numbers
import random
part3 = []
for ten in range(10):
    randomNumber = random.randint(1000,9999)
    part3.append(randomNumber)
#print(part3)

#create the usernames for each respective staff
usernames = []
for i in range(10):
    part_1 = part1[i]
    #print(part_1)
    part_2 = part2[i]
    #print(part_2)
    part_3 = part3[i]
    #print(part_3)
    concatinated = part_1 + part_2 + str(part_3)
    usernames.append(concatinated)
#print(usernames)

# write list to txt file SULES_Usernames
with open("SULES_Usernames.txt", "w") as f:
    for line in usernames:
        f.write(line)
        f.write('\n')
f.close



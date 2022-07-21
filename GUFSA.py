# this program is for Shut Up and Listen Education Services
# this program is generating usernames for staff accounts
# Python program for ICTPRG302

#put the names from the txt file into a list
staff = open("SULES_Staff.txt", "r")
staff_list = []
for line in staff:
    the_line = staff.readline()
    staff_list.append(the_line)
staff.close()

def abbrevName(name):
xs = (name)
name_list = xs. split()
# print(name_list)
​
first = name_list[0][0]
second = name_list[1][0]

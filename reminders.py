import sns
from CommitteeMember import CommitteeMember

committee_members = []

# Pull in group members
config_file = open("config.txt", "r")
if ("Members" in config_file.readline()):
    line = config_file.readline()
    while(line[0].isspace() or line[0] == '#'):
        line = config_file.readline()
    while(not line[0].isspace()):
        items = line.split(",")
        name = items[0]
        first_name = name.split(" ")[0]
        last_name = name.split(" ")[1]
        number = items[1]
        committee_members.append(CommitteeMember(full_name=name, first_name=first_name, last_name=last_name, phone_number=number))
        line = config_file.readline()
else:
    print("Bad config file.")

print("ok")


# Get current week of the month
import datetime
day_of_month = datetime.datetime.now().day
week_number = (day_of_month - 1) // 7 + 1
print(week_number)
import sns
from CommitteeMember import CommitteeMember

committee_members = []

def BadConfig():
    print("Bad config file.")
    exit(0)

def RemindSetup(member_list):
    numbers = []
    for member in member_list:
        numbers.append("+1" + member.phone_number)
    message = (
        "Hi " + member.first_name + ", "
        "this is your reminder that you're scheduled to help set up for institute "
        "this week! Make sure and be at the MSB at 6:50 tomorrow. "
        "If you can't make it, make sure and find someone to replace you! "
        "Thanks!"
    )
    sns.sendText(numbers, message)

def RemindFacebook(member):
    number = "+1" + member.phone_number
    message = (
        "Hi " + member.first_name + "! "
        "This is your reminder that you're scheduled to post the institute "
        "reminder on Facebook this week!"
    )
    sns.sendText([number], message)

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
    BadConfig()


# Get current week of the month
import datetime
day_of_month = datetime.datetime.now().day
week_number = (day_of_month - 1) // 7 + 1


# Do what you need to do based on the week of the month
line = config_file.readline()
while(("Week " + str(week_number)) not in line):
    line = config_file.readline()
line = config_file.readline()
if ("Setup" not in line):
    BadConfig()
names = line.split(":")[1]
setup_list = []
for member in committee_members:
    if (member.full_name in names):
        setup_list.append(member)
RemindSetup(setup_list)

line = config_file.readline()
if ("Facebook" not in line):
    BadConfig()
names = line.split(":")[1]
for member in committee_members:
    if (member.full_name in names):
        RemindFacebook(member)
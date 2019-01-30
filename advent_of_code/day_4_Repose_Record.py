import re
from collections import defaultdict
from datetime import datetime, timedelta, time

with open("/Users/Bharathan/projects/python_practise/advent_of_code/04_input1.txt", "r") as file:
    input1 = list(filter(None, file.read().splitlines()))

print(input1)


# algoritham
# arrange the data in chronological order
# create a object that has time and guard details
# map a day to guard
# allocate each day to a guard if the day has already got a guard assign the guard to the next day
# calculate highest amount of sleep for each guard and the get guard of slept most


class daywise_guard_details():
    guard_name = ""

    def __init__(self, str=""):
        date_str = re.findall(r'\[.+\]+', str)
        self.guard_str = re.findall(r'\]\s(.+)', str)
        self.set_date_time(date_str[0])
        self.set_guard_name(self.guard_str[0])

    def set_date_time(self, str):
        self.date_object = datetime.strptime(str, "[%Y-%m-%d %H:%M]")
        self.date_object_str = self.date_object.strftime("%Y-%m-%d")
        self.year = self.date_object.year
        self.month = self.date_object.month
        self.day = self.date_object.day
        self.hour = self.date_object.hour
        self.minute = self.date_object.minute

    def print_guard_time(self):
        print(self.year)
        print(self.month)
        print(self.day)
        print(self.guard_name)
        print(self.date_object_str)
        print(str(str(self.date_object)))

    def set_guard_name(self, guard_str=""):
        if "Guard #" in guard_str:
            self.guard_name = re.findall(r'\d+', guard_str)[0]

    def set_time_asleep(self,intvalue):
        self.asleep_time = intvalue


previous_guard_name = ""
date_guard_dict = {}
guard_name_set = set()
guard_asleep_dict = {}
guard_effort_fall_asleep = []
guard_effort_wakes_up = []
def compute_sleep_time(guard_effort_fall_asleep, guard_effort_wakes_up):
    temp_asleep = 0
    for i in range(len(guard_effort_fall_asleep)):
        temp_asleep += (guard_effort_wakes_up[i] - guard_effort_fall_asleep[i])
    return temp_asleep

for x in input1:
    guard_data = daywise_guard_details(x)
    if "1518-03-09" in x:
        print("***")
    if guard_data.guard_name and not date_guard_dict.get(guard_data.date_object):
        if guard_data.date_object.hour == 00:
            # temp_date_object = datetime.combine(temp_date_object, time())
            date_guard_dict[guard_data.guard_name]= [guard_data.date_object.strftime("%Y-%m-%d")]
        elif guard_data.date_object.hour == 23:
            temp_date_object = guard_data.date_object + timedelta(days=1)
            temp_date_object = datetime.combine(temp_date_object, time())
            date_guard_dict[guard_data.guard_name] = [guard_data.guard_name]


for key, value in date_guard_dict.items():
    guard_name_set.add(value)

# for x in input1:

for x in date_guard_dict.items():
    print(x)


for x in guard_name_set:
    for y in input1:
        guard_data = daywise_guard_details(y)
        if "727" in x:
            print("******")
        if date_guard_dict[guard_data.date_object_str] == x:
            if "falls asleep" in guard_data.guard_str:
                guard_effort_fall_asleep.append(guard_data.date_object.minute)
            if "wakes up" in guard_data.guard_str:
                guard_effort_wakes_up.append(guard_data.date_object.minute)
    guard_asleep_dict[x]= compute_sleep_time(guard_effort_fall_asleep,guard_effort_wakes_up)

for x,value in guard_asleep_dict.items():
    print(x,value)


import re
from collections import defaultdict
from datetime import datetime, timedelta

with open("/Users/Bharathan/projects/python_practise/advent_of_code/04_sample_input.txt", "r") as file:
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
        guard_str = re.findall(r'\]\s(.+)', str)
        self.set_date_time(date_str[0])
        self.set_guard_data(guard_str[0])

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

    def set_guard_data(self, guard_str="None"):
        if "Guard #" in guard_str:
                self.guard_name = re.findall(r'\d+', guard_str)[0]


previous_guard_name = ""
date_guard_dict = {}
for x in input1:
    guard_data = daywise_guard_details(x)
    guard_data.print_guard_time()
    if guard_data.guard_name and not date_guard_dict.get(guard_data.date_object):
        date_guard_dict[guard_data.date_object]= guard_data.guard_name
    elif guard_data.guard_name and date_guard_dict.get(guard_data.date_object):
        temp_date_object = guard_data.date_object + timedelta(days=1)
        date_guard_dict[temp_date_object] = guard_data.guard_name

# for x in input1:


print(date_guard_dict)

from datetime import datetime


# today = datetime.date.today()

# print("Current date =", today)

input1 = ["[1518-11-01 00:00]","[1518-11-01 00:05]","[1518-11-01 00:25]","[1518-11-01 00:30]","[1518-11-01 00:55]","[1518-11-01 23:58]"]

date_list = []
for x in input1:
    date_object = datetime.strptime(x, "[%Y-%m-%d %H:%M]")
    date_list.append(date_object)

for x in date_list:
    print("class: ",type(x))
    print("year: ",x.year)
    print("year: ",x.month)
    print("year: ",x.day)
    print("year: ",x.hour)
    print("year: ",x.minute)
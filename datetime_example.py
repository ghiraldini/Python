#!/usr/bin/env python3

import datetime
# time
# time(hour = 0, minute = 0, second = 0, microsecond = 0)
# date
# date(year, month, day)
# datetime
# datetime(year, month, day, hour = 0, minute = 0, second = 0, microsecond = 0)


def main():
    # time
    t = datetime.time(1,23,59,302)
    print(t)
    print(t.hour, t.minute, t.second, t.microsecond)
    t = t.replace(hour = 3)
    print(t)

    # date
    d = datetime.date(2017,3,18)
    print(d)
    print(d.year, d.month, d.day)
    d = d.replace(day=19)
    print(d)
    today = datetime.date.today()
    print(today)

    # datetime
    dt = datetime.datetime(year = 2014, month = 1, day = 3, hour = 15, minute = 1)
    print(dt)
    dt = dt.replace(year = 2018)
    print(dt)
    t = datetime.time(hour = 1, minute = 23)
    d = datetime.date(2018, 4, 20)
    dt = datetime.datetime.combine(d,t)
    print(dt)
    dt_today = datetime.datetime.today()
    print(dt_today)



if __name__ == "__main__":
    main()

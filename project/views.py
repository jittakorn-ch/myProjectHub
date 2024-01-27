from django.shortcuts import render
from datetime import datetime, date
import calendar

def get_calendar_info(year=None, month=None):
    if year is None or month is None:
        year, month = datetime.now().year, datetime.now().month

    month_calendar = calendar.monthcalendar(year, month)
    _, number_of_days = calendar.monthrange(year, month)

    month_list = [day for week in month_calendar for day in week]
    month_list.insert(0, 0)

    week_sublists = []
    for i in range(0, number_of_days, 7):
        sublist = month_list[i:i+7]
        sublist += [0] * (7 - len(sublist))
        week_sublists.append(sublist)

    # Get day name from day
    weekdays = [date(2024, 1, i).strftime('%A') for i in range(7, 14)]

    calendar_info = {
        'weekdays': weekdays,
        'week_sublists': week_sublists
    }
    return calendar_info

def project(request):
    return render(request, 'project/index.html')

def todolist(request):

    calendar_info = get_calendar_info()

    context = {
        'calendar_info': calendar_info
    }

    return render(request, 'project/todolist.html', context)

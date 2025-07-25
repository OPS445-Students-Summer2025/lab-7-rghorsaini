#!/usr/bin/env python3
# Student ID: 144843224
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    total = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total)


def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

def change_time(time, seconds):
    total = time_to_sec(time) + seconds
    updated = sec_to_time(total)
    time.hour, time.minute, time.second = updated.hour, updated.minute, updated.second


def time_to_sec(time):
    '''convert a time object to total seconds since midnight'''
    return time.hour * 3600 + time.minute * 60 + time.second

def sec_to_time(seconds):
    '''convert seconds since midnight to a time object'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

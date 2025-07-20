#!/usr/bin/env python3
# Student ID: 144843224

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
       function attributes: __init__, format_time, sum_times, change_time, time_to_sec, valid_time
    """
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        '''Used by print() and str()'''
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        '''Used by interpreter output'''
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'


    def format_time(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def time_to_sec(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    def sum_times(self, t2):
        total = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total)

    def change_time(self, seconds):
        total = self.time_to_sec() + seconds
        updated = sec_to_time(total)
        self.hour, self.minute, self.second = updated.hour, updated.minute, updated.second

    def valid_time(self):
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

    def __add__(self, t2):
        """Allow use of + operator to add two Time objects"""
        return self.sum_times(t2)



def sec_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

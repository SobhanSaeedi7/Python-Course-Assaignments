

class Time:
    def __init__(self, h, m, s, hs):
        self.hour = h
        self.min = m
        self.sec = s
        self.hun_sec = hs

    def plus(self):
        self.hun_sec += 1
        if self.hun_sec >= 10:
            self.hun_sec -= 10
            self.sec += 1
        if self.sec >= 60:
            self.sec -= 60
            self.min += 1
        if self.min >= 60:
            self.min -= 60
            self.hour += 1

    def mines(self):
        if self.hour > 0 or self.min > 0 or self.sec > 0:
            self.sec -= 1
        if self.sec <= 0:
            if self.hour > 0 or self.min > 0:
                self.sec += 60
                self.min -= 1
        if self.min <= 0:
            if self.hour > 0:
                self.min += 60
                self.hour -= 1
        

    def time_to_sec(self):
        result = (self.hour * 60 + self.min) * 60 + self.sec
        return result

    def sub(self, other):
        hun_sec = self.hun_sec - other.hun_sec
        sec = self.sec - other.sec
        min = self.min - other.min
        hour = self.hour - other.hour

        result = Time(hour, min, sec, hun_sec)
        result.fix()
        return result
    
    def sum (self, other):
        sec = self.sec + other.sec
        min = self.min + other.min
        hour = self.hour + other.hour

        result = Time(hour, min, sec, 0)
        self.fix()
        return result

    def sub_clock(self, other):
        hun_sec = self.hun_sec - other.hun_sec
        sec = self.sec - other.sec
        min = self.min - other.min
        hour = self.hour - other.hour

        result = Time(hour, min, sec, hun_sec)
        result.fix()
        if result.hour <= 0:
            time = Time(24, 0, 0, 0)
            clock = result.sum(time)
            return clock
        else:
            return result

    def same_time(self, other):
        if self.hour == other.hour and self.min == other.min:
            return True
        else:
            return False

    def fix(self):
        if self.hun_sec >= 10:
                while True:
                    if self.hun_sec >= 10:
                        self.hun_sec -= 10
                        self.sec += 1
                    else:
                        break
        if self.sec >= 60:
            while True:
                if self.sec >= 60:
                    self.sec -= 60
                    self.min += 1
                else:
                    break
        if self.min>=60:
            while True:
                if self.min >= 60:
                    self.min -= 60
                    self.hour += 1
                else:
                    break
        if self.hun_sec < 0:
            while True:
                if self.hun_sec < 0:
                    self.hun_sec += 10
                    self.sec -= 1
                else:
                    break
        if self.sec < 0:
            while True:
                if self.sec < 0:
                    self.sec += 60
                    self.min -= 1
                else:
                    break
        if self.min < 0:
            while True:
                if self.min < 0:
                    self.min += 60
                    self.hour -= 1
                else:
                    break

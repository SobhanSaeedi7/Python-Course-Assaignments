class time:
    #properties
    def __init__(self,h,m,s,f):
        self.hour = h
        self.colon1 = ":"
        self.minute = m
        self.colon2 = ":"
        self.second = s
        self.time_format = f # "a.m","p.m","24hour"
    #methods
    def time_to_min(self):
        ...
    def time_to_sec(self):
        ...
    def how_much_left_to_midnight(self):
        ...
    def difference_between_times(self):
        ...
    def chek_time(self):
        ...
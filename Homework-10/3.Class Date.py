class date:
    #properties
    def __init__(self,y,m,d,t):
        self.year = y
        self.comma1 = ","
        self.month = m
        self.comma2 = ","
        self.day = d
        self.date_type = t #"AD","Solar","Lunar"
    #methods
    def AD_to_solar(self):
        ...
    def AD_to_lonar(self):
        ...
    def solar_to_AD(self):
        ...
    def solar_to_lunar(self):
        ...
    def lunar_to_AD(self):
        ...
    def lunar_to_solar(self):
        ...
    def how_much_left(self):
        ...
    def date_to_day(self):
        ...
    def date_to_week(self):
        ...
    def difference_between_dates(self):
        ...
    def check(self):
        ...

class Time:
    def __init__(self,h,m,s):
        self.hour = h
        self.min = m
        self.sec = s
        self.fix()

    def show(self):
        print(self.hour,":",self.min,":",self.sec)

    def sum (self, other):
        sec = self.sec + other.sec
        min = self.min + other.min
        hour = self.hour + other.hour

        result = Time(hour, min, sec)
        self.fix()
        return result

    def sud(self,other):
        sec = self.sec - other.sec
        min = self.min - other.min
        hour = self.hour - other.hour
        
        result = Time(hour, min, sec)
        self.fix()
        return result
    
    def time_to_sec(self):
        result = (self.hour * 60 + self.min) * 60 + self.sec
        return result
    @staticmethod
    def sec_to_time(second):
        secs = second
        hour = secs//3600
        min = (secs - hour * 3600) // 60
        sec = (secs - hour * 3600) - min * 60
        result = Time(hour, min, sec)
        return result
    def thr_to_gmt(self):
        tehran_time = Time(3, 30, 0)
        result = Time.sum(self, tehran_time)
        return result
    def fix(self):
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
            
def show_menu():
    print("Fraction Class")
    print("1.Summation Times")
    print("2.Subtraction Times")
    print("3.Time to Second")
    print("4.Seconds to Time")
    print("5.GMT to Tehran")

while True:
    show_menu()
    choose = input("\nEnter number of your choice : ")

    if choose == "1":
        sec1 = int(input("Enter first second : "))
        min1 = int(input("Enter first minute : "))
        hour1 = int(input("Enter first hour : "))
        sec2 = int(input("Enter second second : "))
        min2 = int(input("Enter second minute : "))
        hour2 = int(input("Enter second hour : "))
        time1 = Time(hour1, min1, sec1)
        time2 = Time(hour2, min2, sec2)
        result = time1.sum(time2)
        result.show()
    elif choose == "2":
        sec1 = int(input("Enter first second : "))
        min1 = int(input("Enter first minute : "))
        hour1 = int(input("Enter first hour : "))
        sec2 = int(input("Enter second second : "))
        min2 = int(input("Enter second minute : "))
        hour2 = int(input("Enter second hour : "))
        time1 = Time(hour1, min1, sec1)
        time2 = Time(hour2, min2, sec2)
        result = time1.sum(time2)
        result.show()
    elif choose == "3":
        sec = int(input("Enter second : "))
        min = int(input("Enter minute : "))
        hour = int(input("Enter hour : "))
        time = Time(hour, min, sec)
        result = time.time_to_sec()
        print(result)
    elif choose == "4":
        second = int(input("Enter seconds : "))
        result = Time.sec_to_time(second)
        result.show()
    elif choose == "5":
        sec = int(input("Enter second : "))
        min = int(input("Enter minute : "))
        hour = int(input("Enter hour : "))
        time = Time(hour, min, sec)
        result = time.thr_to_gmt()
        result.show()
    elif choose == "exit":
        exit()
    else:
        print("Please just enter number of your choice or enter 'exit' to exit\n\n")
        

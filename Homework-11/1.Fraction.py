import math

class Fraction:
    def __init__(self,num,den):
        self.numerator = num
        self.denominator = den

    def sum(self,other):
        result_num = self.numerator * other.denominator + self.denominator * other.numerator
        result_den = self.denominator * other.denominator
        result = Fraction(result_num, result_den)
        return result

    def sub(self,other):
        result_num = self.numerator * other.denominator - self.denominator * other.numerator
        result_den = self.denominator * other.denominator
        result = Fraction(result_num, result_den)
        return result

    def multiplication(self, other):
        result_num = self.numerator * other.numerator
        result_den = self.denominator * other.denominator
        result = Fraction(result_num, result_den)
        return result

    def division(self,other):
        result_num = self.numerator * other.denominator
        reselt_den = self.denominator * other.numerator
        result = Fraction(result_num, reselt_den)
        return result

    def frac_to_num(self):
        number = self.numerator / self.denominator
        return number
    
    def simplify_frac(self):
        gcd = math.gcd(self.numerator,self.denominator)
        result_num = int(self.numerator/gcd)
        result_den = int(self.denominator/gcd)
        result = Fraction(result_num,result_den)
        return result

    def show(self):
        print(self.numerator,"/",self.denominator)



def show_menu():
    print("Fraction Class")
    print("1.Summation Fractions")
    print("2.Subtraction Fractions")
    print("3.Multiplication Fractions")
    print("4.Division Fractions")
    print("5.Fraction to Number")
    print("6.Simplify the fraction Fractions")


while True:
    show_menu()
    choose = input("\nEnter number of your choice : ")

    if choose == "1":
        num1 = int(input("Enter first numerator : "))        
        den1 = int(input("Enter first denominator : "))
        num2 = int(input("Enter first numerator : "))
        den2 = int(input("Enter second denominator : "))
        frac1 = Fraction(num1, den1)
        frac2 = Fraction(num2, den2)
        result = frac1.sum(frac2)
        print("\n\n Result : ")
        result.show()
        break
    elif choose == "2":
        num1 = int(input("Enter first numerator : "))        
        den1 = int(input("Enter first denominator : "))
        num2 = int(input("Enter first numerator : "))
        den2 = int(input("Enter second denominator : "))
        frac1 = Fraction(num1, den1)
        frac2 = Fraction(num2, den2)
        result = frac1.sub(frac2)
        print("\n\n Result : ")
        result.show()
        break
    elif choose == "3":
        num1 = int(input("Enter first numerator : "))        
        den1 = int(input("Enter first denominator : "))
        num2 = int(input("Enter first numerator : "))
        den2 = int(input("Enter second denominator : "))
        frac1 = Fraction(num1, den1)
        frac2 = Fraction(num2, den2)
        result = frac1.multiplication(frac2)
        print("\n\n Result : ")
        result.show()
        break
    elif choose == "4":
        num1 = int(input("Enter first numerator : "))        
        den1 = int(input("Enter first denominator : "))
        num2 = int(input("Enter first numerator : "))
        den2 = int(input("Enter second denominator : "))
        frac1 = Fraction(num1, den1)
        frac2 = Fraction(num2, den2)
        result = frac1.division(frac2)
        print("\n\n Result : ")
        result.show()
    elif choose == "5":
        num1 = int(input("Enter numerator : "))
        den1 = int(input("Enter denominator : "))
        frac = Fraction(num1, den1)
        result = frac.frac_to_num()
        print("Result : ",result)

    elif choose == "6":
        num = int(input("Enter numerator : "))
        den = int(input("Enter denominator : "))
        frac = Fraction(num, den)
        result = frac.simplify_frac()
        result.show()

    elif choose == "exit":
        exit()
    else:
        print("Please just enter number of your choice or enter 'exit' to exit\n\n")
        
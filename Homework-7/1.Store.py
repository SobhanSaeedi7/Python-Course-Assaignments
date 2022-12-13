#Store
import qrcode
#Functions
PRODUCTS = []
bell = []
def read_from_database():
    f = open("database.txt", "r")

    for line in f :

        r = line.split(",")
        dict = {"code": r[0],"name": r[1],"price": r[2],"count": r[3]}

        PRODUCTS.append(dict)

    f.close()

def write_to_database():
    data = open("database.txt", "w")
    for line in PRODUCTS:
        data.write(str(line["code"])+","+str(line["name"])+","+str(line["price"])+","+str(line["count"]))
    
    data.close()


def show_menu():
    print("1-add➕")
    print("2-edit🖊")
    print("3-remove❌")
    print("4-search🔎")
    print("5-show list📜")
    print("6-buy🛒")
    print("7-make qrcode📅")
    print("8-exit🏃")
    

def add():
    while True:
        password = input("Enter password : ")
        if password == "1234":
            code = input("enter new code : ")
            name = input("enter name : ")
            price = input("enter price'﷼': ")
            count = input("enter count : ")
            new_dict = {"code": code,"name": name,"price": price,"count":count}
            PRODUCTS.append(new_dict)
            print("Added successfully")
            break
        elif password == "exit":
            break
        else :
            print("Wrong password!!try again or writ 'exit' to exit")

def edit():
    while True:
        password = input("Enter password : ")
        if password == "1234" :
            code = input("Enter code or name to find product : ")
            for p in PRODUCTS:
                    if p["code"] == code or p["name"] == code:
                        print(p["code"],"\t\t",p["name"],"\t\t",p["price"],"\t\t",p["count"])
                        print ("Wich one do you want to edit?")
                        print("1.name\n2.price\n3.count")
                        choice = input("Enter number of your choice : ")
                        if choice == 1:
                            new_name = input("Enter new name : ")
                            p["name"] = new_name
                            print("Updated✅")
                            break
                        elif choice == 2:
                            new_price = input("Enter new price : ")
                            p["price"] = new_price
                            print("Updated✅")
                            break
                        elif choice == 3:
                            new_count = input("Enter new count : ")
                            p["count"] = new_count
                            print("Updated✅")
                            break
                        else :
                            print("Choose 1, 2, 3")

            else :
                print("Not found")
                break
        elif password == "exit":
            break
        else :
            print("Password wrond!!!Try again or write 'exit' to exit")

def remove():
    while True:
        password = input("Enter password : ")
        if password == "1234" :
            input_code = input("Enter a code or name to find : ")
            for p in PRODUCTS:
                    if p["code"] == input_code or p["name"] == input_code:
                        print(p["code"],"\t\t",p["name"],"\t\t",p["price"],"\t\t",p["count"])
                        while True:
                            okey = input("Are you sure that you want to remove this??Y/N ; ")
                            if okey == "Y":
                                PRODUCTS.remove(p)
                                print("Removed successfully")
                                break
                            elif okey == "N":
                                break
                            else :
                                print("Just enter Y(yes) or N(no)")
            else :
                print("Not found")
                break
        elif password == "exit":
            break
        else :
            print("Wrong password!!!Try again or write 'exit' to exit")
def search():
    while True:
        who = input("Are you user or staff?")
        if who == "staff":
            while True:
                password = input("Enter password : ")
                if password == "1234":
                    user = input("Enter name or code to search :")
                    for p in PRODUCTS:
                        if p["code"] == user or p["name"] == user:
                            
                            break
                    else:
                        break
                elif password == "exit":
                    break
                else :
                    print("Wrong password!!try again or writ 'exit' to exit")
        elif who == "user":
            user = input("Enter name or code to search :")
            for p in PRODUCTS:
                if p["code"] == user or p["name"] == user:
                    print(p["code"],"\t\t",p["name"],"\t\t",p["price"])
                    break
            else:
                print("not found")
        elif who == "exit":
            break
        else:
            print("Just enter 'user' , 'staff' or 'exit'")
    

def show_list():
    who = input("Are you user or staff?")
    if who == "staff":
        while True:
            password = input("Enter password : ")
            if password == "1234" :
                for p in PRODUCTS:
                   print(p["code"],"\t\t",p["name"],"\t\t",p["price"],"\t\t",p["count"])
            elif password == "exit":
                break
            else :
                print("Wrong password!!try again or writ 'exit' to exit")
    elif who == "user":
        for p in PRODUCTS:
                   print(p["code"],"\t\t",p["name"],"\t\t",p["price"])
    else:
        print("Just enter 'user' or 'staff'")
    
def buy():
    while True:
        input_code = input("Enter a code or name to find : ")
        for p in PRODUCTS:
            if p["code"] == input_code or p["name"] == input_code:
                print(p["code"],"\t\t",p["name"],"\t\t",p["price"],"\t\t")
                count_user = int(input("How many do you want?(enter -1 to exit) "))
                if count_user == -1 :
                    break
                else:
                    while True :
                        if int(p["count"]) > count_user :
                            p["count"] = int(p["count"])-count_user
                            buy = {"code":p["code"],"name":p["name"],"price":p["price"],"count":count_user}
                            bell.append(buy)
                            print("Your order has been registered")
                            break
                        elif int(p["count"]) < count_user :
                            print("The number of available choosed product is not enough")
                            print("There are just :",p["count"])
                            print("Choose again or write 'exit' to exit")
                            break
                        
            elif input_code == "exit":
                break
        else:
            print("Not found")
            break
        
def Qrcode():
    while True:
        input_code = input("Enter a code or name to find : ")
        for p in PRODUCTS:
            if p["code"] == input_code or p["name"] == input_code:
                print(p["code"],"\t\t",p["name"],"\t\t",p["price"],"\t\t")
                product = str(p["code"]) + "\t\t" + str(p["name"]) + "\t\t" +str(p["price"])
                Qrcodeu = qrcode.make(product)
                Qrcodeu.save("Qrcode.png")
                print("Qrcode saved")
                break
        else:
            print("Not found")

def show_bell():
    print("Your bell")
    print("code\t\tname\t\tprice\t\tcount")
    total = 0
    for i in bell:
        print(i["code"],"\t\t",i["name"],"\t\t",i["price"],"\t\t",i["count"])
        total = (int(i["price"])*int(i["count"]))+total
    print("Total : ",total)




#Play
while True:
    print("Wellcome to your store🛒")
    print("Please wait few seconds⌛")
    read_from_database()
    print("loaded✨")
    show_menu()
    choice = input("Enter your choice : ")

    if choice == "1":
        add()
    elif choice == "2":
        edit()
    elif choice == "3":
        remove()
    elif choice == "4":
        search()
    elif choice == "5":
        show_list()
    elif choice == "6":
        buy()
    elif choice == "7":
        Qrcode()
    elif choice == "8":
        write_to_database()
        show_bell()
        exit() 
    else:
        print("Just enter number of your choice😶")
  
import sqlite3


bill = []


def load_database():
    global connection
    global cursor
    connection = sqlite3.connect("store.db")
    cursor = connection.cursor()


def show_menu():
    print("1-show list📜")
    print("2-add➕")
    print("3-search🔎")
    print("4-edit🖊")
    print("5-remove❌")
    print("6-buy🛒")
    print("7-exit🏃")
    
def show_list():
    list = cursor.execute('SELECT * FROM products')
    products = list.fetchall()
    print("ID  Name\tPrice\tCount")
    for product in products:
        print(product[0],".",product[1],"\t\t",product[2],"\t\t",product[3])


def add():
        name = input("enter name : ")
        price = input("enter price : ")
        count = input("enter count : ")
        cursor.execute(f"INSERT INTO products(Name, Price, Count) VALUES('{name}', {int(price)}, {int(count)})")
        connection.commit()


def search():
    user_input = input("Enter product`s name or id to search : ")
    for product in cursor.execute(f"SELECT * FROM products"):
        if str(product[0]) == user_input or product[1] == user_input:
            print("ID  Name\t\tPrice\t\tCount")
            print(product[0],".",product[1],"\t\t",product[2],"\t\t",product[3])
            break
    else:
        print("Not Found!")


def edit():
    user_input = input("Enter name or id of product to edit : ")
    for product in cursor.execute("SELECT * FROM products"):
        if str(product[0]) == user_input or product[1] == user_input:
            print("ID  Name\t\tPrice\t\tCount")
            print(product[0],".",product[1],"\t\t",product[2],"\t\t",product[3])
            name = input("enter name : ")
            price = input("enter price : ")
            count = input("enter count : ")
            cursor.execute(f"UPDATE products Set Name= '{name}', Price= {int(price)}, Count= {int(count)} WHERE Name= '{product[1]}'")
            connection.commit()
            break
    else:
        print("Not Found!")


def remove():
    user_input = input("Enter name or id of product to search : ")
    for product in cursor.execute("SELECT * FROM products"):
        if str(product[0]) == user_input or product[1] == user_input:
            print("ID  Name\t\tPrice\t\tCount")
            print(product[0],".",product[1],"\t\t",product[2],"\t\t",product[3])
            accept = input("Are you sure?(yes/no) : ")
            if accept == "yes":
                cursor.execute(f"DELETE FROM products WHERE Name= '{product[1]}'")
                connection.commit()
                print("Deleted succesfuly!")
                break
            else:
                break
    else:
        print("Not Found!")
    

def buy():
    user_input = input("Enter name or id of product to search : ")
    for product in cursor.execute("SELECT * FROM products"):
        if str(product[0]) == user_input or product[1] == user_input:
            print("ID  Name\t\tPrice\t\tCount")
            print(product[0],".",product[1],"\t\t",product[2],"\t\t",product[3])
            count = int(input("How many do you want? :"))
            if product[3] < count:
                print(f"Not enough available!There are just {product[3]}")
                break
            else:
                order = [product[0], product[1], product[2], count, product[2]*count]
                bill.append(order)
                cursor.execute(f"UPDATE products SET count=count-{count} WHERE Name= '{product[1]}'")
                connection.commit()
                print("Order registered✅")
                break
    else:
        print("Not Found!")



def show_bill():
    print("Your bill")
    print("ID  Name\t\tPrice\t\tCount\t\tTotal price")
    total = 0
    for i in bill:
        print(i[0],".",i[1],"\t\t",i[2],"\t\t",i[3],"\t\t",i[4])
        total = int(i[4])+total
    print("Total : ",total)




while True:
    print("Wellcome to your store🛒")
    load_database()
    show_menu()
    choice = input("Enter your choice : ")

    if choice == "1":
        show_list()
    elif choice == "2":
        add()
    elif choice == "3":
        search()
    elif choice == "4":
        edit()
    elif choice == "5":
        remove()
    elif choice == "6":
        buy()
    elif choice == "7":
        show_bill()
        exit() 
    else:
        print("Just enter number of your choice😶")
  
input_list = []

while True:
    
    num = input('Enter a number to add to list or enter "done" to check : ')

    if num == "done":
        break

    elif num.isnumeric():
        input_list.append(int(num))

    else:
        print('Please just enter a number or "done" to check')


for i in range(len(input_list)//2):
        if input_list[i] != input_list[-(i+1)]:
            print("List isn`t symmetric")

        else:
            print("It`s symmetric")

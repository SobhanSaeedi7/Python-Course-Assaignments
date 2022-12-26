def make_rug(number):
    shapes = ["🌑","🌒","🌓","🌖","🌕","🌖","🌗","🌘","🌑"]
    middle = (number - 1) / 2
    if number%2 == 1 and number < 0:
        print("Input number should be even and greater than 0!!!")
    else :
        rug = []
        for i in range(number):
            texture = []
            for j in range(number):
                num = int(max(abs(i - middle), abs(j - middle)))
                texture.append(shapes[num%len(shapes)])
            rug.append(texture)
    for row in rug:
        for shape in row:
            print(shape , end = " ")
        print()

input_user = int(input("Enter number : "))
make_rug(input_user)
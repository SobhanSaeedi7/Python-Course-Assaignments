import gtts

user_suggestions = []

def read_from_file():
    global words_bank
    f = open("translate.txt", "r")

    temp = f.read().split("\n")

    words_bank = []

    for i in range(0, len(temp), 2):
        my_dict = {"en":temp[i], "fa":temp[i+1]}
        words_bank.append(my_dict)

    f.close()

def shoe_menu():
    print("Wellcome to Your Assistant Translator🔁")
    print("1.Translate English to Persian En ⇒ Fa")
    print("2.Translate Persian to English Fa ⇒ En")
    print("3.Add new word to dictionary ➕")
    print("4.Check user suggestion 👀")
    print("5.Exit🏃")

def english_to_persian():
    user_text = input("Enter your English text : ")

    user_words0 = user_text.split(" ")
    user_words = []
    for word in user_words0:
        user_words.append(word.split("."))

    output = ""

    for splited_list in user_words:
        for user_word in splited_list:
         for word in words_bank:
             if user_word == word["en"]:
                 output = output + word["fa"] + " "
                 break
        
         else:
             output = output + user_word + " "

    voice = gtts.gTTS(output, lang="ar", slow=False)

    voice.save("persian.mp3")
    print (output)

def persian_to_english():
    user_text = input("Enter your Persian text : ")

    user_words0 = user_text.split(" ")
    user_words = []
    for word in user_words0:
        user_words.append(word.split("."))

    output = ""

    for splited_list in user_words:
        for user_word in splited_list:
         for word in words_bank:
             if user_word == word["fa"]:
                 output = output + word["en"] + " "
                 break
        
         else:
             output = output + user_word + " "

    voice = gtts.gTTS(output, lang="en", slow=False)

    voice.save("English.mp3")
    print (output)

def add_word() :
            en_word = input("Enter word in English : ")
            fa_word = input("Enter word in Persian : ")

            dict = {"en":en_word,"fa":fa_word}
            user_suggestions.append(dict)

            print("Your suggestion sended for developer and it`ll check✅")
            print("Thanks for your suggestion🙏")

def check_suggestion():
    while True:
        password = input("Enter password : ")
        if password == "1234":
            for suggestion in user_suggestions:
                print(suggestion["en"]," : ",suggestion["fa"])
                add_or_no = input("Do you want to add this one(Y) to dictionary or no(N)? : ")
                if add_or_no == "N" :
                    user_suggestions.remove(suggestion)
                    print("Removed from suggestions❌")
                elif add_or_no == "Y":
                    dictionary = open("translate.txt", "a")
                    dictionary.write("\n"+suggestion["en"]+"\n"+suggestion["fa"])
                    dictionary.close()
                    user_suggestions.remove(suggestion)
                    print("Added successfully✅")
                elif add_or_no == "exit":
                    break
                else :
                    print("Just enter 'Y' or 'N',or enter 'exit' to exit")
        elif password == "exit":
            break
        else:
            print("Wrong password!!!Try again or enter 'exit' to exit")

        


while True:
    read_from_file()
    shoe_menu()
    choice = input("Enter number of your choice : ")

    if choice == "1":
        english_to_persian()
    elif choice == "2":
        persian_to_english()
    elif choice == "3":
        add_word()
    elif choice == "4":
        check_suggestion()
    elif choice == "5":
        print("Good luck🤗")
        exit()
    else:
        print("Just enter number of your chice")    
    


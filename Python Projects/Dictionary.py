def word_definetion():

    word_dictionary = {

        "Hi" : "A way of greeting.",
        "Eye" : "An organ for seening.",
        "Learn" : "Gain or acquire knowledge of or skill in(something) by study, experience, or being taught.",
        "Angry" : "Feeling or showing stron annoyance,displeasure,or hostilliy.",
        "Code" : "A system of words,letters,figures,ro symbols used to represent others, especially for the purposes of secrecy.",
        "Program" : "A set of related measures or activities with a particular long-term aim.",
        "Algorithm" : "A process or set of rules to be followed in calcutations or other problem-solving operations,especially by a computer."
    }

    run = True
    while run:
        greeting = input("Hello do you want to use our dictionary (yes/no): ")
        print("#"*50)
        if greeting.lower() == "yes":
                print("#"*50)
                word = input("Type a word to know it's meaning: ")
                for key,value in word_dictionary.items():
                    if word.lower() == key.lower():
                        print(value)
                        print("#"*50)
        elif greeting.lower() == "no":
            print("Thank you for using our program")
            break
        else:
            print("Invild entry. Please type yes or no")

word_definetion()
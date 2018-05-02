from translate import translate

print("Welcome in word reference\n")

while(True):
    word = raw_input("Enter a word or press X for exit: ")

    if word == "X" or word == "x":
        break

    elif type(word) != str:
        continue

    else:
        result = translate(word)

        if type(result) == str:
            print(result)
            print("\n")

        else:
            i = 1
            for item in result:
                print("Definition %d: " %i + item)
                i += 1

            print("\n")

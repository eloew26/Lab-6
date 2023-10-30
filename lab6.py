#Elan Loewinger
def encode(password):
    split = list(password)
    out = ""
    i = 0
    while (i < len(split)):
        split[i] = str(int(split[i]) + 3)
        out = out + str(split[i])
        i = i + 1
    return out

if __name__ == "__main__":
    option = 0
    while (option != 3):
        print("1. Encode password")
        print("2. Decode password")
        print("3. Exit")
        option = int(input('Select option: '))
        if(option == 1):
            password = input("Enter password: ")
            encoded = encode(password)
            print(encoded)
            option = 0
            print("1. Encode password")
            print("2. Decode password")
            print("3. Exit")
            option = int(input('Select option: '))
        if (option == 2):
            option = 0
            print("1. Encode password")
            print("2. Decode password")
            print("3. Exit")
            option = int(input('Select option: '))


#Elan Loewinger
#Thomas Zhao
def encode(password):
  split = list(password)
  out = ""
  i = 0
  while (i < len(split)):
      split[i] = str(int(split[i]) + 3)
      out = out + str(split[i])
      i = i + 1
  return out
def decode(password):
  decoded_pass = ""
  a = 0
  for a in range(len(password)):
    if int(password[a])-3<0:
      decoded_pass += str(int(password[a])+7)
    else:
      decoded_pass += str(int(password[a])-3)
  return decoded_pass
if __name__ == "__main__":
  option = 0
  while (option != 3):

      print('Menu')
      print(13*'-')
      print("1. Encode password")
      print("2. Decode password")
      print("3. Exit")
      encoded = ''
      option = int(input('Select option: '))
      if(option == 1):
          password = input("Enter password: ")
          encoded = encode(password)
          print("Your password has been encoded and stored!")
          print()
          option = 0
          print('Menu')
          print(13*'-')
          print("1. Encode password")
          print("2. Decode password")
          print("3. Exit")
          option = int(input('Select option: '))
      if (option == 2):
          print("The ecoded password is,", encoded, end = ' ')
          print("and the original password is,", decode(encoded))
          print()
          option = 0
          print('Menu')
          print(13*'-')
          print("1. Encode password")
          print("2. Decode password")
          print("3. Exit")
          option = int(input('Select option: '))


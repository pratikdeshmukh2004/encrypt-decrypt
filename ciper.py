def encrypt(message):
  if ord(message)>119:
    ascii_message = [ord(char)-23 for char in message]
    encrypt_message = [ chr(char) for char in ascii_message]  
  else:
    ascii_message = [ord(char)+3 for char in message]
    encrypt_message = [ chr(char) for char in ascii_message]  
  return ''.join(encrypt_message)
def decrypt(message):
  if ord(message)<100:
    ascii_message = [ord(char)+23 for char in message]
    decrypt_message = [ chr(char) for char in ascii_message]  
  else:
    ascii_message = [ord(char)-3 for char in message]
    decrypt_message = [ chr(char) for char in ascii_message]  
  return ''.join(decrypt_message)

flag = True
while flag:
    choice = str(input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter e or e respectively!"))
    if choice == 'e':
        message = str(input("Enter the message you want to ecrypt"))
        add=""
        for letter in message:
          add+=encrypt(letter)
        print (add)
    elif choice == 'd':
        message = str(input("Enter the message you want to decrypt"))
        add=""
        for letter in message:
          add+=decrypt(letter)
        print (add) 
    play_again = str(input("Do you want to try agian or Do you want to exit? (Y/N)"))
    if play_again == "n":
        break
    elif play_again == "y":
        continue

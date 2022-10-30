from tkinter import messagebox, simpledialog, Tk

#This function checks if a number is even or odd
def is_even(number):
 return number % 2 == 0

#This function will get the letters that are
#in even positions of the message and add them into a list 
def get_even_letters(message):
 even_letters = []
 for counter in range(0, len(message)):
     if is_even(counter):
         even_letters.append(message[counter])
 return even_letters

#This function will get the letters that are
#in odd positions of the message and add them into a list
def get_odd_letters(message):
 odd_letters = []
 for counter in range(0, len(message)):
     if not is_even(counter):
         odd_letters.append(message[counter])
 return odd_letters

#This function gets even letters from the encrypted message
#and it is used for decryption
def get_even_letters_dec(message):
    even_letters_dec = []
    for counter in range(0, int(len(message)/2)):
        even_letters_dec.append(message[counter])
    return even_letters_dec

#This function gets odd letters from the encrypted message
#and it is used for decryption
def get_odd_letters_dec(message):
    odd_letters_dec = []
    for counter in range(int(len(message)/2), int(len(message))):
        odd_letters_dec.append(message[counter])
    return odd_letters_dec


#This function checks if the letter is vowel
def is_vowel(letter):
        if (letter == 'A' or
            letter == 'E' or
            letter == 'I' or
            letter == 'O' or
            letter == 'U' or
            letter == 'Y' or
            letter == 'a' or
            letter == 'e' or
            letter == 'i' or
            letter == 'o' or
            letter == 'u' or
            letter == 'y'):
            return True
    


#This function will encrypt the message
def encrypt(message):
 letter_list = []
 
 if not is_even(len(message)):
     message = message + ' '
     
 even_letters = get_even_letters(message)
 odd_letters = get_odd_letters(message)

#Add the odd letters at the beginning of the encrypted message,
#also add a dot(.) if the letter is vowel 
 for counter in range(0, int(len(message)/2)):
     letter_list.append(odd_letters[counter])
     if (is_vowel(odd_letters[counter]) == True):
         letter_list.append('.')
         
#Add the even letters at the end of the encrypted message,
#also add a dot(.) if the letter is vowel
 for counter in range(0, int(len(message)/2)):
     letter_list.append(even_letters[counter])
     if (is_vowel(even_letters[counter]) == True):
         letter_list.append('.')

#Join the letters to the new message and reverse it
 new_message = ''.join(letter_list)
 reversed_encrypted_message = ''.join(reversed(new_message))
 
 return reversed_encrypted_message

#This function will decrypt the message
def decrypt(message):
 letter_list = []
 
 unreversed_message = ''.join(reversed(message))

 if not is_even(len(unreversed_message)):
     unreversed_message = unreversed_message + ' '
 
 #This code removes the dots from the message
 reversed_message = unreversed_message.replace(".", "")
         
 even_letters = get_even_letters_dec(reversed_message)
 odd_letters = get_odd_letters_dec(reversed_message)
 
 for counter in range(0, int(len(reversed_message)/2)):
     letter_list.append(odd_letters[counter])   
     letter_list.append(even_letters[counter])
     
 new_message = ''.join(letter_list)
 
 return new_message

def get_task():
 task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?')
 return task

def get_message():
 message = simpledialog.askstring('Message', 'Enter the secret message: ')
 return message

root = Tk()
root.withdraw()

while True:
 task = get_task()
 if task == 'encrypt':
     message = get_message()
     encrypted = encrypt(message)
     messagebox.showinfo('Ciphertext of the secret message is:', encrypted)
 elif task == 'decrypt':
     message = get_message()
     decrypted = decrypt(message)
     messagebox.showinfo('Plaintext of the secret message is:', decrypted)
 else:
     break

root.mainloop()

import random
import string
import pyautogui
Choices= string.ascii_letters + string.digits + string.punctuation
Choice_list = list(Choices)

Password=pyautogui.password("Enter your password - ") 
Guess=''

while Guess!=Password:
    Guess=random.choices(Choice_list, k=len(Password))
    print ("<------------"+ str(Guess) +"------------>")
    if Guess==list(Password):
        print("Cracked.\n The password is " + ''.join(Guess))
        input()
        break
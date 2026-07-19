import string
import random
def password_generator():
    while True:
        try:
            password_length= int(input("Enter length of password = "))
        except ValueError:
            print("Enter a number ")
            continue

        values = string.ascii_letters + string.digits +string.punctuation
        password = " "
        for i in range (password_length):
            password += random.choice(values)
            
        print(password)
        
password_generator()
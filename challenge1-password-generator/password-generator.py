import random

password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()-+{}:?~"
length_password = int(input("Enter the length of the password: "))
a = "".join(random.sample(password,length_password))

if length_password >= 8:
    print(f"Your password is {a}")
else:
    print("Password Length is too short please retry")
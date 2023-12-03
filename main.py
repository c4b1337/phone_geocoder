import phonenumbers
from phonenumbers import geocoder

def phone_number(phone_number):
    while True:
        phone_number = input("Enter your phone number: ")
        number = phonenumbers.parse(phone_number)
        description = geocoder.description_for_number(number, "en")
        print(description)
        print("Do you want to enter another number?")


phone_number(phone_number)





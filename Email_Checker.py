import json
import time
from urllib.request import urlopen

intro ='''
Email checker :)
'''
print(intro)
while True:
    email = input("Email : ")

    key = "YdJMzmBP6hkHxQsWcjwbZT8nLf7rVFUq"

    url = "https://emailverifierapi.com/v2/?apiKey=" + key + "&email=" + email
    response = urlopen(url)
    data = json.load(response)
    details=data['details']
    if details == "The mailbox exists.":
        print("Email Valide !")
    else:
        print("Email Invalide !")


response = urlopen(url)
data = json.load(response)
details=data['details']

if details == "The mailbox exists.":
    print("Email Valide !")
else:
    print("Email Invalide !")

time.sleep(5)



